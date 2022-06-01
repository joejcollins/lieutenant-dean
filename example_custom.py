import task_queuing.celery_app as app
import celery
from kombu import Queue
from datetime import datetime


def send_me_a_message(producer=None):
    """Send a custom message as per Scott's instructions."""
    queue = Queue("custom_queue")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    id = celery.uuid()
    headers = {"task": "task_queuing.tasks.custom.shit", "id": id}
    body = {"text": "Secret text to encode", "Time": current_time}

    with app.queue_broker.producer_or_acquire(producer) as producer:
        producer.publish(
            headers=headers,
            body=body,
            serializer="json",
            exchange=queue.exchange,
            routing_key="custom_queue",
            declare=[queue],
            retry=True,
        )
    print(f"Custom task {id} on queue")


if __name__ == "__main__":
    send_me_a_message()
