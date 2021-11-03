""" Test slow running arithmetic tasks. """
import task_queue.numbers as number_tasks


def test_slowly_add_two_numbers():
    """ Since the task starts immediately you have to wait for it to end. """
    task = number_tasks.slowly_add_two_numbers.s(1, 2).apply()
    # Once the task is over it should indicate success.
    assert task.status == 'SUCCESS'
