import pika
import json

def publish_bid(bid):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        
        # Declarar el exchange tipo 'fanout'
        channel.exchange_declare(exchange='bids', exchange_type='fanout')
        
        message = json.dumps(bid)
        channel.basic_publish(exchange='bids', routing_key='', body=message)
        
        print(f" [x] Sent {message}")
        print(' [*] Message published successfully.')
        connection.close()
    except Exception as e:
        print(f" [!] Error: {e}")

if __name__ == '__main__':
    bid = {"bidder": "User1", "amount": 100}
    publish_bid(bid)
