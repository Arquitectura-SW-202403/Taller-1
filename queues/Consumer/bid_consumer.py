import pika
import json
import os
import sys
import logging

logger = logging.getLogger(__name__)
def callback(ch, method, properties, body):
    try:
        # Decodificar el mensaje JSON recibido
        bid = json.loads(body)
        print(f" [x] Analytics Service received bid from {bid['bidder']} with amount {bid['amount']}")
    except json.JSONDecodeError:
        print(f" [!] Error decoding JSON: {body}")


def consume_bid():
    try:
        
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue=os.environ["RABBIT_QUEUE"])
        channel.basic_consume(queue=os.environ["RABBIT_QUEUE"], on_message_callback=callback,
         auto_ack=True
        )

        print(' [*] Waiting for bids. To exit press CTRL+C')
        print(' [*] Analytics Consumer setup complete and ready to receive messages.')
        channel.start_consuming()
    except Exception as e:
        print(f" [!] Error: {e}")


if __name__ == "__main__":
    try:
        consume_bid()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os.exit(0)
