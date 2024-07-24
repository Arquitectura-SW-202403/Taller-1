from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(
    bootstrap_servers=["kafka_broker:9092"]
)

while True:
    sleep(5)
    print("Bacano")
    producer.send("bid_topic", value="Bid sended".encode("utf-8"))

