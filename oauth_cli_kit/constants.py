"""Default provider settings and constants."""

from __future__ import annotations

from oauth_cli_kit.models import OAuthProviderConfig

SUCCESS_HTML = (
    "<!doctype html>"
    "<html lang=\"en\">"
    "<head>"
    "<meta charset=\"utf-8\" />"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />"
    "<title>Authentication successful</title>"
    "</head>"
    "<body>"
    "<p>Authentication successful. Return to your terminal to continue.</p>"
    "</body>"
    "</html>"
)

OPENAI_CODEX_PROVIDER = OAuthProviderConfig(
    client_id="app_EMoamEEZ73f0CkXaXp7hrann",
    authorize_url="https://auth.openai.com/oauth/authorize",
    token_url="https://auth.openai.com/oauth/token",
    redirect_uri="http://localhost:1455/auth/callback",
    scope="openid profile email offline_access",
    jwt_claim_path="https://api.openai.com/auth",
    account_id_claim="chatgpt_account_id",
    default_originator="nanobot",
    token_filename="codex.json",
)
