from celery import bootsteps
from kombu import Consumer, Exchange, Queue


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher"""

    my_queue = Queue('custom', Exchange('custom'), 'routing_key')

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        print(f"Registering custom consumer: {__class__}")
        return [Consumer(channel,
                         queues=[self.my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]
