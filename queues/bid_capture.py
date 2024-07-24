import pika
import json

def callback(ch, method, properties, body):
    bid = json.loads(body)
    print(f" [x] Captured bid: {bid}")

def main():
    try:
        # Conexión al servidor RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Declarar la cola
        channel.queue_declare(queue='bid_capture_queue')

        # Configurar el consumidor
        channel.basic_consume(queue='bid_capture_queue',
                              on_message_callback=callback,
                              auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        print(' [*] Capture Consumer setup complete and ready to receive messages.')
        channel.start_consuming()
    except Exception as e:
        print(f" [!] Error: {e}")

if __name__ == '__main__':
    main()
