""" Scratch pad. """
import pika
import json
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672))
channel = connection.channel()

channel.queue_declare(queue="text_queue", durable=True)  # durable = true: queue will survive rabbitmq restart

channel.exchange_declare(exchange="kats_exchange", exchange_type="direct")

message_type = sys.argv[1:]
if not message_type:
    sys.stderr.write("Usage: %s [environment] [virtualhost]\n" % sys.argv[0])
    sys.exit(1)

messages = [
    {
        "Body": {"Type": "environment", "Alias": "{{alias}}", "Properties": {}},
        "Topic": "{{alias}}.environment.{{action}}",
        "CallContext": {},
    },
    {
        "Body": {
            "ObjectId": "www.google.com",
            "Type": "virtualhost",
            "ProjectId": "{{projectguid}}",
            "ProjectApiId": "{{projectapiid}}",
            "Alias": "{{alias}}",
            "Properties": {
                "virtualhost": "www.google.com",
            },
        },
        "Topic": "{{alias}}.{{projectapiid}}.virtualhost.{{action}}",
        "CallContext": {},
    },
]


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
