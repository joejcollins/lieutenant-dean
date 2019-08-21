""" Run a simple pytest with `pytest test-pytest.py` """
import tasks

def test_slowly_reverse_string():
    """ Since the task starts immediately you have to wait for it to end """
    task = tasks.slowly_reverse_string.s(string="qwerty").apply()
    # Once the task is over it should indicate success.
    assert task.status == 'SUCCESS'
