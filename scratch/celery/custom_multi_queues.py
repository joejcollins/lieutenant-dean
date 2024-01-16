"""Post messages to a specific queue dependent on their load."""
import celery
import celery_queue_rabbit.celery_app as app
from celery_queue_rabbit.queues import custom_exchange


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
            exchange=custom_exchange,
            declare=[custom_exchange],  # declares exchange, queue and binds.
            routing_key="low_load")
        return id


if __name__ == "__main__":
    id = send_to_text_reverse()
    print(f"task {id} on queue")
