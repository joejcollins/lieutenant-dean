""" Test slow running arithmetic tasks. """
import task_queue.numbers as number_tasks


def test_slowly_add_two_numbers_without(monkeypatch):
    """ Patch over the update state so we can test just the function on
    it's own, so the broker doesn't need to be running. """
    monkeypatch.setattr(
        number_tasks.slowly_add_two_numbers,
        "update_state",
        lambda state, meta: None
    )
    result = number_tasks.slowly_add_two_numbers(1, 2)
    assert result == 3


def test_slowly_add_two_numbers_with():
    """ Test the method with Celery but calling immediately rather than using
    a worker, so we can still debug it. """
    task = number_tasks.slowly_add_two_numbers.s(1, 2).apply()
    # Once the task is over it should indicate success.
    assert task.status == 'SUCCESS'
