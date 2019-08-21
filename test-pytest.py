""" pytest test-pytest.py """
import pytest
import tasks

def test():
    task = tasks.slowly_reverse_string.s(string="qwerty").apply()
    print(task)
    assert task.status == 'SUCCESS'