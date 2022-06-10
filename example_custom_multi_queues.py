"""Post messages to a specific queue dependent on their load."""
from task_queuing.queues import custom_exchange
import task_queuing.celery_app as app


def send_custom_message(producer=None):
    """Send a custom message to our exchange with routing key high."""
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
            routing_key="high")
        return id


if __name__ == "__main__":
    id = send_custom_message()
    print(f"task {id} on queue")
