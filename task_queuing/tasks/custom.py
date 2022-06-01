"""Custom celery task to capitalize text"""
import task_queuing.celery_app as app


class Capitalize(app.queue_broker.Task):
    """Custom task without the decorator"""

    def run(self, text):
        capitalized = text.upper()
        return capitalized


@app.queue_broker.task(base=Capitalize)
def shit(x):
    return "val"


# app.queues.tasks.register(Capitalize)
