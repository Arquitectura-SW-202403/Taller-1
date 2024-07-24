import pika
import json

def callback(ch, method, properties, body):
    try:
        # Decodificar el mensaje JSON recibido
        bid = json.loads(body)
        print(f" [x] Analytics Service received bid from {bid['bidder']} with amount {bid['amount']}")
    except json.JSONDecodeError:
        print(f" [!] Error decoding JSON: {body}")

def consume_bid():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        
        # Declarar el exchange tipo 'fanout'
        channel.exchange_declare(exchange='bids', exchange_type='fanout')
        
        # Declarar una cola temporal
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        
        # Enlazar la cola al exchange
        channel.queue_bind(exchange='bids', queue=queue_name)
        
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        
        print(' [*] Waiting for bids. To exit press CTRL+C')
        print(' [*] Analytics Consumer setup complete and ready to receive messages.')
        channel.start_consuming()
    except Exception as e:
        print(f" [!] Error: {e}")

if __name__ == '__main__':
    consume_bid()
