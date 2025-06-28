import pika
import os
from producer_interface import mqProducerInterface
from stock import Stock  # pylint: disable=import-error

class Produce(mqProducerInterface):
    def __init__(self, exchange_name: str) -> None:
        # Save parameters to class variables
        exchange_name = "topic"
        self.exchange_name = exchange_name
        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=self.con_params)
        # Establish Channel
        self.channel = self.connection.channel()
        # Create the topic exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange="Exchange Name")

    def publishOrder(self, sector: str, stock: Stock) -> None:
        # Create Appropiate Topic String
        topic = f"Stock.{stock.get_name()}.{sector}"
        topic.strip()
        # Send serialized message or String
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=topic,
            body=stock.serialize(),
        )
        # Print Confirmation
        print(f" [x] Sent Order: {topic}")
        # Close channel and connection
        self.channel.close()
        self.connection.close()
