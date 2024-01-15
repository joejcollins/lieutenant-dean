"""Custom consumers for celery_rabbit."""""
from celery import bootsteps
from celery_queue_rabbit.queues import my_queues
from kombu import Consumer


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher."""

    def handle_message(self, body, message):
        """Handle the message."""
        print('Received message: {0!r}'.format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        """Get the consumers."""
        print(f"Registering custom consumer: {__class__}")
        return [Consumer(channel,
                         queues=my_queues,
                         callbacks=[self.handle_message],
                         accept=['json'])]
