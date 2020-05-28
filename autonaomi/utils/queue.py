import pika

class rabbit_mq_uploader:
    def __init__(self, host, port):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, port))

    def publish(self, data, exchange):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type="fanout", durable=True)
        channel.basic_publish(exchange=exchange,
                      routing_key='',
                      body=data)

    def consume(self, queue, callback, exchange=""):
        channel = self.connection.channel()
        channel.queue_declare(queue)
        def mq_callback(channel, method, props, message):
            callback(message)
            channel.basic_ack(delivery_tag=method.delivery_tag)
        if exchange:
            channel.exchange_declare(exchange=exchange, exchange_type="fanout", durable=True)
            channel.queue_bind(exchange=exchange, queue=queue)
        channel.basic_consume(on_message_callback=mq_callback, auto_ack=False, queue=queue)
        channel.start_consuming()

queues = {'rabbitmq': rabbit_mq_uploader}

class queue_uploader:
    def __init__(self, queue_type, host, port):
        self.queue = queues[queue_type](host=host, port=port)

    def publish(self, data, exchange):
        self.queue.publish(data=data, exchange=exchange)

    def consume(self, queue, callback, exchange=""):
        self.queue.consume(queue=queue, callback=callback, exchange=exchange)
