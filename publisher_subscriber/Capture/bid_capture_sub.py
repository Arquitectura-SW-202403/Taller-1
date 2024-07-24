from kafka import KafkaConsumer

consumer = KafkaConsumer('bid_topic',
                         bootstrap_servers=['kafka_broker:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         group_id='my_group_id',
                         value_deserializer=lambda x: x.decode('utf-8')
                         )

for message in consumer:
    data = message.value
    print(f"Bid taken from Bid Analytics {data}")
