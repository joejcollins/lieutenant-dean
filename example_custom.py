import celery_app.task_broker as broker
from kombu import Queue
from datetime import datetime


def send_me_a_message(producer=None):
    """Send a custom message as per Scott's instructions."""
    queue = Queue("custom_queue")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    body = {"text": "Secret text to encode", "Time": current_time, "task": "make_secret"}

    with broker.broker_config.producer_or_acquire(producer) as producer:
        producer.publish(
            body=body,
            serializer="json",
            exchange=queue.exchange,
            routing_key="custom_queue",
            declare=[queue],
            retry=True,
        )
    print("on queue")


if __name__ == "__main__":
    send_me_a_message()
