from __future__ import annotations

import json

from oauth_cli_kit.models import OAuthToken
from oauth_cli_kit.storage import FileTokenStorage, _load_token_file, _save_token_file


def test_save_and_load_token_file_roundtrip(tmp_path) -> None:
    path = tmp_path / "auth.json"
    token = OAuthToken(access="a", refresh="r", expires=123, account_id="acct")
    _save_token_file(path, token)

    loaded = _load_token_file(path)
    assert loaded is not None
    assert loaded.access == "a"
    assert loaded.refresh == "r"
    assert loaded.expires == 123
    assert loaded.account_id == "acct"


def test_load_token_file_invalid_json_returns_none(tmp_path) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not-json", encoding="utf-8")
    assert _load_token_file(path) is None


def test_file_token_storage_uses_data_dir(tmp_path) -> None:
    storage = FileTokenStorage(
        token_filename="oauth.json",
        app_name="oauth-cli-kit-test",
        data_dir=tmp_path,
        import_codex_cli=False,
    )
    token = OAuthToken(access="a", refresh="r", expires=123, account_id=None)
    storage.save(token)

    loaded = storage.load()
    assert loaded is not None
    assert loaded.access == "a"
    assert loaded.refresh == "r"
    assert loaded.expires == 123


def test_storage_writes_expected_json_shape(tmp_path) -> None:
    storage = FileTokenStorage(
        token_filename="oauth.json",
        app_name="oauth-cli-kit-test",
        data_dir=tmp_path,
        import_codex_cli=False,
    )
    token = OAuthToken(access="a", refresh="r", expires=123, account_id=None)
    storage.save(token)

    raw = storage.get_token_path().read_text(encoding="utf-8")
    payload = json.loads(raw)
    # 约束落盘字段，避免无意引入敏感/冗余信息
    assert set(payload.keys()) == {"access", "refresh", "expires"}

