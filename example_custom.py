import task_queuing.celery_app as app
import celery
from kombu import Exchange, Queue
from datetime import datetime


def send_me_a_message(producer=None):
    """Send a custom message as per Scott's instructions."""
    my_queue = Queue('custom', Exchange('custom'), 'routing_key')
    eta = str(datetime.now())
    id = celery.uuid()
    # headers = {"task": "task_queuing.tasks.custom.shit", "id": id}
    # body = {"text": "Secret text to encode", "Time": current_time}

    message = {
        'task': 'task_queuing.tasks.custom.shit',
        'id': id,
        'args': [id],
        "kwargs": {},
        "retries": 0,
        "eta": eta
    }

    with app.queue_broker.producer_or_acquire(producer) as producer:
        producer.publish(
            message,
            serializer="json",
            exchange=my_queue.exchange,
            routing_key="custom_queue",
            declare=[my_queue],
            retry=True,
        )
    print(f"Custom task {id} on queue")


if __name__ == "__main__":
    send_me_a_message()
