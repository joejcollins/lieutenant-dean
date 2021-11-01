""" Test slow running text tasks. """
import task_queue.text as text_tasks


def test_slowly_reverse_string():
    """ Since the task starts immediately you have to wait for it to end """
    task = text_tasks.slowly_reverse_string.s(string_to_reverse="qwerty").apply()
    # Once the task is over it should indicate success.
    assert task.status == 'SUCCESS'
