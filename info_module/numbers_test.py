""" Test arithmetic. """
import info_module.numbers as numbers


def test_method_is_present():
    """ Confirm that the methods are present. """
    assert "add_two_numbers" in dir(numbers)


def test_add_two_numbers():
    """ Confirm the text is reversed. """
    first_number = 1
    second_number = 2
    total = numbers.add_two_numbers(first_number, second_number)
    assert total == 3
