""" Test slow running text tasks without queuing. """
import task_queues.text as text_tasks


def test_slowly_reverse_string_without(monkeypatch):
    """ Patch over the update state so we can test just the function on
    it's own, so the broker doesn't need to be running. """
    monkeypatch.setattr(
        text_tasks.slowly_reverse_string,
        "update_state",
        lambda state, meta: None
    )
    result = text_tasks.slowly_reverse_string("qwerty")
    assert result == "ytrewq"


def test_slowly_reverse_string():
    """ Test the method with Celery but calling immediately rather than using
    a worker, so we can still debug it. """
    task = text_tasks.slowly_reverse_string.s(
        string_to_reverse="qwerty"
        ).apply()
    # Once the task is over it should indicate success.
    assert task.status == 'SUCCESS'
