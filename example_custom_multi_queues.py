"""Post messages to a specific queue dependent on their load."""
import celery
from kombu import Exchange, Queue

import task_queuing.celery_app as app


def send_custom_message(producer=None):
    """Send a custom message to our exchange with routing key high."""
    my_queue = Queue("zengenti-cloud-high", Exchange("zengenti-cloud-high"), routing_key="zengenti-cloud-high")
    id = celery.uuid()
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
            declare=[my_queue],
            retry=True)
        return id


def send_to_text_reverse(producer=None):
    """Send a reverse_text task to our exchange with routing key low."""
    my_queue = Queue("zengenti-cloud-low", Exchange("zengenti-cloud-low"), routing_key="zengenti-cloud-low")
    id = celery.uuid()
    message = {
        "task": "task_queuing.tasks.text.slowly_reverse_string",
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
            routing_key=my_queue.routing_key,
            declare=[my_queue],  # declares exchange, queue and binds.
            retry=True)
        return id


if __name__ == "__main__":
    task1 = send_to_text_reverse()
    task2 = send_custom_message()
    print(f"tasks {task1} and {task2} on queue")
