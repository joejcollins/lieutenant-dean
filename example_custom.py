import celery_apps.redis_broker as broker
from kombu import Exchange, Queue, Consumer
from celery import bootsteps

my_queue = Queue("text_queue", Exchange("custom"), "routing_key")

body = {
    "Body": {"Type": "environment", "Alias": "joes-test", "Properties": {}},
    "Topic": "joes-test.environment.delete",
    "CallContext": {},
}


class MyConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [Consumer(channel, queues=[my_queue], callbacks=[self.handle_message], accept=["json"])]

    def handle_message(self, body, message):
        print("Received message: {0!r}".format(body))
        message.ack()


broker.redis_queues.steps["consumer"].add(MyConsumerStep)


def send_me_a_message(producer=None):
    """test custom message"""
    with broker.redis_queues.producer_or_acquire(producer) as producer:
        producer.publish(
            body=body,
            serializer="json",
            exchange=my_queue.exchange,
            routing_key="routing_key",
            declare=[my_queue],
            retry=True,
        )


if __name__ == "__main__":
    send_me_a_message()
