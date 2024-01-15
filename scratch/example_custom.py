"""Post a message to the custom queue."""
from datetime import datetime

import celery
from kombu import Exchange, Queue

import celery_queue_rabbit.celery_app as app


def send_to_shit(producer=None):
    """Send a custom message as per Scott's instructions."""
    my_queue = Queue("custom_queue", Exchange("custom_queue"), "custom_queue")
    eta = str(datetime.now())
    id = celery.uuid()
    # headers = {"task": "celery_queue_rabbit.tasks.custom.shit", "id": id}
    # body = {"text": "Secret text to encode", "Time": current_time}

    message = {
        "task": "celery_queue_rabbit.tasks.custom.shit",
        "id": id,
        "args": [id],
        "kwargs": {},
        "retries": 0,
        "eta": eta,
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
        return id


def send_to_custom_consumer(producer=None):
    """Send a custom message as per Scott's instructions."""
    # For Celery the queue and routing key should match.
    my_queue = Queue(name="text_queue", routing_key="text_queue")

    message = {
        "Body": {"Type": "environment", "Alias": "{{alias}}", "Properties": {}},
        "Topic": "{{alias}}.environment.{{action}}",
        "CallContext": {},
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
        return id


def send_to_text_reverse(producer=None):
    my_queue = Queue("text_queue", Exchange("text_queue"), "text_queue")
    eta = str(datetime.now())
    id = celery.uuid()
    # headers = {"task": "celery_queue_rabbit.tasks.custom.shit", "id": id}
    # body = {"text": "Secret text to encode", "Time": current_time}

    message = {
        "task": "celery_queue_rabbit.tasks.text.slowly_reverse_string",
        "id": id,
        "args": ["reverse me"],
        "kwargs": {},
        "retries": 0
    }

    with app.queue_broker.producer_or_acquire(producer) as producer:
        producer.publish(
            message,
            serializer="json",
            exchange=my_queue.exchange,
            routing_key="text_queue",
            declare=[my_queue],
            retry=True,
        )
        return id


if __name__ == "__main__":
    id = send_to_text_reverse()
    print(f"task {id} on queue")
