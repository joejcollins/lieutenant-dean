""" Test text manipulations. """
import my_module.text as text


def test_method_is_present():
    """ Confirm that the methods are present. """
    assert "reverse_text" in dir(text)


def test_reverse_text():
    """ Confirm the text is reversed. """
    string_to_reverse = 'qwerty'
    reversed_text = text.reverse_text(string_to_reverse)
    assert reversed_text == 'ytrewq'
