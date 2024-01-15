"""Custom celery task to capitalize text."""
import celery_queue_rabbit.celery_app as app


class Capitalize(app.queue_broker.Task):
    """Custom task without the decorator."""

    def run(self, text):
        """Capitalize the text."""
        capitalized = text.upper()
        return capitalized


@app.queue_broker.task(base=Capitalize)
def shit(x):
    """Do some shit."""
    print('shit')
    return "val"


# app.queues.tasks.register(Capitalize)
