"""Post messages to a specific queue dependent on their load."""
from task_queuing.queues import custom_exchange
import task_queuing.celery_app as app
import celery


def send_custom_message(producer=None):
    """Send a custom message to our exchange with routing key high."""
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
            exchange=custom_exchange,
            declare=[custom_exchange],
            routing_key="high_load",
            retry=True)
        return id


def send_to_text_reverse(producer=None):
    """Send a reverse_text task to our exchange with routing key low."""
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
            exchange=custom_exchange,
            declare=[custom_exchange],  # declares exchange, queue and binds.
            routing_key="low_load")
        return id


if __name__ == "__main__":
    task1 = send_to_text_reverse()
    task2 = send_custom_message()
    # result = celery.group(task1, task2)()
    print(f"tasks {task1} and {task2} on queue")
