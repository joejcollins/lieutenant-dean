""" Celery text manipulations. """
import logging

from task_queues.celery_app import queue

@queue.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def run_playbook(self, playbook_name):
    """Run a playbook"""
    logger = logging.getLogger(self.request.id)
    logger.info('running playbook.')
    # Spawn something
