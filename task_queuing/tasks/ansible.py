"""Tasks for running ansible commands."""
import logging

import celery
import task_queuing.celery_app as app
import task_queuing.tasks.text as text_tasks


@app.queue_broker.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def run_playbook(self, playbook, alias):
    return "nothing"