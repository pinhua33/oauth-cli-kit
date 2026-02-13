from __future__ import annotations

import os

import pytest


@pytest.fixture(autouse=True)
def _clear_token_path_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """测试里避免被用户环境变量影响 token 路径。"""
    monkeypatch.delenv("OAUTH_CLI_KIT_TOKEN_PATH", raising=False)

