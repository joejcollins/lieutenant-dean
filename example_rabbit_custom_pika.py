""" Scratch pad. """
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672))
channel = connection.channel()

channel.queue_declare(queue="text_queue", durable=True)  # durable = true: queue will survive rabbitmq restart

message = {
    "Body": {"Type": "environment", "Alias": "{{alias}}", "Properties": {}},
    "Topic": "{{alias}}.environment.{{action}}",
    "CallContext": {},
}

channel.basic_publish(
    exchange="",
    routing_key="text_queue",
    body=json.dumps(message),
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ),  # saves message to disk to prevent message loss
)

print(" [x] Sent %r" % message)
connection.close()

print("Chain of tasks now on the Rabbit broker.")
