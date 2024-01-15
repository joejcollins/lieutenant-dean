"""Test text manipulations."""
from pkg_shared import text


def test_method_is_present() -> None:
    """Confirm that the methods are present."""
    assert "reverse_string" in dir(text)


def test_reverse_text() -> None:
    """Confirm the text is reversed."""
    string_to_reverse = "qwerty"
    reversed_text = text.reverse_string(string_to_reverse)
    assert reversed_text == "ytrewq"
