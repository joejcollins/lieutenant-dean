"""Post messages to a specific queue dependent on their load."""
import celery
from kombu import Exchange, Queue

import task_queuing.celery_app as app

@app.queue_broker.task()
def send_to_text_reverse(producer=None):
    """Send a reverse_text task to our exchange with routing key low."""
    my_queue = Queue("zengenti-cloud-high", Exchange("contensis", type='topic'), routing_key="alias.environment.action")
    id = celery.uuid()
    message = {
        "task": "task_queuing.tasks.text.slowly_reverse_string",
        "id": id,
        "args": ["reverse me again"],
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


@app.queue_broker.task()
def send_custom_message(producer=None):
    """Send a custom message to our exchange with routing key high."""
    # my_queue = Queue("zengenti-cloud-low", Exchange("zengenti-cloud-low"), routing_key="zengenti-cloud-low")
    my_queue = Queue("zengenti-cloud-high", Exchange("contensis", type='topic'), routing_key="alias.environment.action")
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
            routing_key=my_queue.routing_key,
            retry=True)


if __name__ == "__main__":
    task2 = send_to_text_reverse.si()
    # task2 = send_custom_message.si()
    print(f"tasks {task2} on queue")
