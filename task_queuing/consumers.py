from celery import bootsteps
from kombu import Consumer, Exchange, Queue


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher"""

    queue = Queue("custom_queue", Exchange("custom_queue"), routing_key="custom_queue")

    def on_message(self, body, message):
        print("Received message: {0!r}".format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        print(f"Registering custom consumer: {__class__}")
        consumers = []
        my_consumer = Consumer(
            channel,
            queues=[self.queue],
            on_message=self.on_message,
        )
        consumers.append(my_consumer)
        return consumers
