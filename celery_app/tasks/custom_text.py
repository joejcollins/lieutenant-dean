from celery import bootsteps
from kombu import Consumer, Exchange, Queue


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher"""

    queue = Queue("custom", Exchange("custom"), "routing_key")

    def handle_message(self, body, message):
        print("Received message: {0!r}".format(body))
        message.ack()  # so it doesn't get redelivered.

    def on_raw_message(body):
        print(body)

    def get_consumers(self, channel):
        print("Registering the new consumer")
        consumers = []
        my_consumer = Consumer(
            channel,
            queues=[self.queue],
            callbacks=[self.handle_message],
            accept=["json"],
            on_message=self.on_raw_message,
        )
        consumers.append(my_consumer)
        return consumers
