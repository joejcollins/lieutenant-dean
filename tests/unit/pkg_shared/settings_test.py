"""Tests for the settings module."""
import os.path

from _pytest.monkeypatch import MonkeyPatch

from pkg_shared import settings
from pkg_shared.settings import CAPTAIN_BLACK
from tests.unit.mock_built_in_file import MockFile


def mock_file_open(
    file: str, mode: str, encoding: str | None = None  # pylint: disable=unused-argument
) -> MockFile:
    """Return a mock file with some dummy content."""
    return MockFile('{"redis_host":  "my-dev-box.somewhere.com", "redis_db": 3}')


def test_method_is_present() -> None:
    """Confirm that the methods are present."""
    assert "this_directory" in dir(settings)
    assert "load_local_settings" in dir(settings.CaptainBlackSettings)


def test_settings() -> None:
    """Test that the static settings are correct."""
    # ARRANGE
    captain_black = settings.CAPTAIN_BLACK
    # ASSERT
    assert captain_black.app_name.startswith("Captain Black")
    assert captain_black.redis_host == "127.0.0.1"


def test_get_settings_file_present(monkeypatch: MonkeyPatch) -> None:
    """Test what happens when the settings file is not there."""
    # ARRANGE
    # Patch over isfile so the file is found even if it is not there.
    monkeypatch.setattr(os.path, "isfile", lambda filename: True)
    # Patch over the file open so the mock file is found.
    monkeypatch.setattr("builtins.open", mock_file_open)
    # ACT
    the_settings = CAPTAIN_BLACK._get_settings_file(  # pylint: disable=protected-access
        "dummy_file.json"
    )
    # ASSERT
    assert "my-dev-box.somewhere.com" in the_settings
