import time

import pika
import json

queues_to_send = ['analytics', 'capture', 'tracking']


def connect():
    global channel
    global connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    # Declarar el exchange tipo 'fanout'
    #channel.exchange_declare(exchange='bids', exchange_type='direct')
    for destination in queues_to_send:
        channel.queue_declare(queue=destination)
        #channel.queue_bind(exchange='bids', queue=destination, routing_key=destination)


def publish_bid(bid: dict, destination: str):
    try:
        message = json.dumps(bid)
        print(f"Sending to {destination}")
        channel.basic_publish(exchange='', routing_key=destination, body=message)

        print(f" [x] Sent {message}")
        print(f' [*] Message published successfully to {destination}.')
    except Exception as e:
        print(f" [!] Error: {e}")
        connection.close()
        return "FAILED"



if __name__ == "__main__":
    connect()
    while True:
        for dest in queues_to_send:
            bid = {"bidder": "User1", "amount": 100, "to": dest}
            code = publish_bid(bid, dest)
            time.sleep(5)
            if code == "FAILED":
                exit(1)