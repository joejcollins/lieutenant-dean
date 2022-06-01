""" Rabbit consumer - message handler """
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("amqp://the_user:the_password@localhost:5672/the_vhost")
)
channel = connection.channel()

channel.queue_declare(queue="text_queue", durable=True)
print("Consumer is running and waiting for messages.")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)

channel.start_consuming()
