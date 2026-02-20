"""
Small helper to load a Hugging Face token from a local `.env` file and
configure common libraries (huggingface_hub, transformers, diffusers).

Usage inside a notebook cell:

    from notebooks_token_helper import setup_hf_token
    setup_hf_token(verbose=True)

This will:
- Load `.env` if present (using python-dotenv if available; otherwise env only).
- Pick `HUGGINGFACE_HUB_TOKEN` if set, else fall back to `HF_TOKEN`.
- Set `HUGGINGFACE_HUB_TOKEN` in `os.environ` for downstream libs.
- Try to log in to the hub via `huggingface_hub.login` if available.
"""

from __future__ import annotations

import os
from typing import Optional


def _load_dotenv_if_available() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
    except Exception:
        # dotenv is optional; we silently continue if it's not installed
        pass


def _pick_token() -> Optional[str]:
    # Prefer the standard key used by huggingface_hub
    token = os.getenv("HUGGINGFACE_HUB_TOKEN")
    if token:
        return token.strip()
    token = os.getenv("HF_TOKEN")
    return token.strip() if token else None


def setup_hf_token(verbose: bool = False) -> Optional[str]:
    """Load token from env/.env and log in with huggingface_hub if possible.

    Returns the token string if found, else None.
    """
    _load_dotenv_if_available()

    token = _pick_token()
    if not token:
        if verbose:
            print(
                "No Hugging Face token found. Set HUGGINGFACE_HUB_TOKEN in a .env file."
            )
        return None

    # Ensure the canonical env var is set for downstream libs
    os.environ["HUGGINGFACE_HUB_TOKEN"] = token

    # Try to authenticate with huggingface_hub if available
    try:
        from huggingface_hub import login  # type: ignore

        login(token=token, add_to_git_credential=False)
        if verbose:
            print("Authenticated with huggingface_hub.")
    except Exception:
        # huggingface_hub not installed or auth failed; proceed with env only
        if verbose:
            print("huggingface_hub not available; relying on env variable only.")

    return token


__all__ = ["setup_hf_token"]

