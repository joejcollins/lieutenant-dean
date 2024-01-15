"""Tests for the settings module."""

from pkg_shared import settings


def test_method_is_present() -> None:
    """Confirm that the methods are present."""
    assert "this_directory" in dir(settings)
    assert "load_local_settings" in dir(settings.CaptainBlackSettings)

