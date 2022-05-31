""" Celery RabbitMQ queue text manipulations. """
import logging
import time

import info_module.text as info_module_text
from celery import bootsteps
from celery_apps.rabbit_broker import rabbit_queues
from kombu import Consumer


@rabbit_queues.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def slowly_reverse_string(self, string_to_reverse):
    """Reverse the string but take 10 seconds to do it."""
    logger = logging.getLogger(self.request.id)
    logger.info(f"RabbitMQ: Reversing {string_to_reverse}.")
    counter = 10
    for i in range(0, counter):
        self.update_state(state="PROGRESS", meta={"done": i, "total": counter})
        logger.info(f"RabbitMQ: Reversing stage {i} of counter.")
        time.sleep(1)
    return info_module_text.reverse_string(string_to_reverse)


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher"""

    def get_consumers(self, channel):
        return [Consumer(channel, queues=[my_queue], callbacks=[self.handle_message], accept=["json"])]

    def handle_message(self, body, message):
        print("Received message: {0!r}".format(body))
        message.ack()
