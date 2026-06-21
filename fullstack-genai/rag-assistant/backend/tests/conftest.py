"""Pytest config."""

import pytest


@pytest.fixture(autouse=True)
def _use_temp_chroma(monkeypatch, tmp_path):
    monkeypatch.setenv("CHROMA_PERSIST_DIR", str(tmp_path / "chroma"))
    monkeypatch.setenv("UPLOAD_DIR", str(tmp_path / "uploads"))
    from app.core.config import get_settings
    get_settings.cache_clear()
