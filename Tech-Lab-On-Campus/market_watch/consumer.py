import pika
import os
from consumer_interface import mqConsumerInterface


class Consumer(mqConsumerInterface):
    def __init__(self, exchange_name: str) -> None:
        # Save parameters to class variables
        self.exchange_name = exchange_name
        # Call setupRMQConnection

        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service

        # Establish Channel

        # Create the exchange if not already present

        pass

    def bindQueueToExchange(self, queueName: str, topic: str) -> None:
        # Bind Binding Key to Queue on the exchange

        pass

    def createQueue(self, queueName: str) -> None:
        # Create Queue if not already present

        # Set-up Callback function for receiving messages

        pass

    def on_message_callback(self, channel, method_frame, header_frame, body):
        # De-Serialize JSON message object if Stock Object Sent

        # Acknowledge And Print Message

        pass

    def startConsuming(self) -> None:
        # Start consuming messages

        pass
