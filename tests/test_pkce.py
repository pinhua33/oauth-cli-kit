from __future__ import annotations

import base64
import hashlib

from oauth_cli_kit.pkce import _generate_pkce, _parse_authorization_input


def _b64url_no_pad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def test_generate_pkce_challenge_matches_verifier() -> None:
    verifier, challenge = _generate_pkce()

    # verifier/challenge 都应该是 base64url（无 '=' padding）
    assert "=" not in verifier
    assert "=" not in challenge

    expected = _b64url_no_pad(hashlib.sha256(verifier.encode("utf-8")).digest())
    assert challenge == expected


def test_parse_authorization_input_from_full_url() -> None:
    raw = "http://localhost:1455/auth/callback?code=abc123&state=st"
    code, state = _parse_authorization_input(raw)
    assert code == "abc123"
    assert state == "st"


def test_parse_authorization_input_from_query_string() -> None:
    raw = "code=abc123&state=st"
    code, state = _parse_authorization_input(raw)
    assert code == "abc123"
    assert state == "st"


def test_parse_authorization_input_from_bare_code() -> None:
    code, state = _parse_authorization_input("abc123")
    assert code == "abc123"
    assert state is None


def test_parse_authorization_input_from_hash_format() -> None:
    # 兼容极简 “code#state” 形式（历史遗留解析逻辑）
    code, state = _parse_authorization_input("abc123#st")
    assert code == "abc123"
    assert state == "st"

