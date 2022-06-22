from celery import bootsteps
from kombu import Consumer
import time

from task_queuing.queues import my_queues


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher"""

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        print(f"Registering custom consumer: {__class__}")
        return [Consumer(channel,
                         queues=my_queues,
                         callbacks=[self.handle_message],
                         accept=['json'])]
