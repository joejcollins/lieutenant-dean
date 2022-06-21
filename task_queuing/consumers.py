from celery import bootsteps
from kombu import Consumer, Exchange, Queue


class SubstitutionCypher(bootsteps.ConsumerStep):
    """Custom handling of substitution cypher"""
    my_queue = Queue("custom_queue", Exchange("custom_queue"), routing_key="custom_queue")

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        print(f"Registering custom consumer: {__class__}")
        return [Consumer(channel,
                         queues=self.my_queue,
                         callbacks=[self.handle_message],
                         accept=['json'])]


class HighConsumer(bootsteps.ConsumerStep):
    """Handles tasks sent to high load queue"""
    my_queue = Queue("zengenti-cloud-high", Exchange("zengenti-cloud-high"), routing_key="zengenti-cloud-high")

    def handle_message(self, body, message):
        print('High load worker: Received message: {0!r}'.format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        print(f"Registering custom consumer: {__class__}")
        return [Consumer(channel,
                         queues=self.my_queue,
                         callbacks=[self.handle_message],
                         accept=['json'])]


class LowConsumer(bootsteps.ConsumerStep):
    """Handles tasks sent to low load queue"""
    my_queue = Queue("zengenti-cloud-high", Exchange("contensis", type='topic'), routing_key="*.environment.*")

    def handle_message(self, body, message):
        print('Low load worker: Received message: {0!r}'.format(body))
        message.ack()  # so it doesn't get redelivered.

    def get_consumers(self, channel):
        print(f"Registering custom consumer: {__class__}")
        return [Consumer(channel,
                         queues=self.my_queue,
                         callbacks=[self.handle_message],
                         accept=['json'])]
