""" RabbitMQ consumer - message handler """
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672))
channel = connection.channel()

channel.queue_declare(queue="text_queue", durable=True)
print("Consumer is running and waiting for messages.")


def text_callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="text_queue", on_message_callback=text_callback)

channel.start_consuming()
