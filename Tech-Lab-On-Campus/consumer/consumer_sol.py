import pika
import os
from consumer_interface import mqConsumerInterface


class mqConsumer(mqConsumerInterface):
    def __init__(
        self, binding_key: str, exchangeName: str, queueName: str
    ) -> None:
        # Save parameters to class variables
        self.binding_key = binding_key
        self.exchangeName = exchangeName
        self.queueName = queueName
        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=self.con_params)
        # Establish Channel
        self.channel = self.connection.channel()
        # Create Queue if not already present
        self.channel.queue_declare(queue="Queue Name")
        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange="Exchange Name")
        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(
            queue="Queue Name",
            routing_key="Routing Key",
            exchange="Exchange Name",
            )
        # Set-up Callback function for receiving messages
        self.channel.basic_consume(
            "Queue Name", self.on_message_callback, auto_ack=False
            )

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # Acknowledge and print message
        channel.basic_ack(method_frame.delivery_tag, False)
        print(header_frame, body)
        # Close channel and connection
        channel.close()
        self.connection.close()

    def startConsuming(self) -> None:
        # Start consuming messages
        self.channel.start_consuming()
