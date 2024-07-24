import pika
import json
import time

def send_message(channel, queue, message):
    """Envía un mensaje a una cola específica"""
    try:
        channel.basic_publish(exchange='',
                              routing_key=queue,
                              body=message)
        print(f" [x] Sent {message} to {queue}")
    except Exception as e:
        print(f" [!] Error sending message to {queue}: {e}")

def main():
    try:
        # Conexión al servidor RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Declarar las colas
        channel.queue_declare(queue='bid_capture_queue')
        channel.queue_declare(queue='bid_tracking_queue')
        channel.queue_declare(queue='bid_analytics_queue')

        # Lista de pujas
        bids = [
            {'bidder': 'User1', 'amount': 100},
            {'bidder': 'User2', 'amount': 200},
            {'bidder': 'User3', 'amount': 300}
        ]

        # Enviar cada mensaje a todas las colas
        for bid in bids:
            message = json.dumps(bid)
            send_message(channel, 'bid_capture_queue', message)
            send_message(channel, 'bid_tracking_queue', message)
            send_message(channel, 'bid_analytics_queue', message)
            time.sleep(1)  # Esperar un segundo entre mensajes para evitar sobrecarga

        print(' [*] All messages sent successfully.')

        connection.close()
    except Exception as e:
        print(f" [!] Error: {e}")

if __name__ == '__main__':
    main()
