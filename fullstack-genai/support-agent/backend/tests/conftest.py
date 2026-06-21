import pytest


@pytest.fixture(autouse=True)
def _use_temp_data(monkeypatch, tmp_path):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "data"))
