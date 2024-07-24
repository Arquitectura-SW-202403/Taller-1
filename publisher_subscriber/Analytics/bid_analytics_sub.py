from kafka import KafkaConsumer

consumer = KafkaConsumer('bid_topic',
                         bootstrap_servers=['kafka_broker:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         group_id='my_group_id',
                         value_deserializer=lambda x: x.decode('utf-8')
                         )
consumer.subscribe(topics=['bid_topic'])

while True:
    msg = consumer.poll(timeout_ms=1000)
    if msg:
        for topic, partition, offset, key, value in msg.items():
            print("Topic: {} | Partition: {} | Offset: {} | Key: {} | Value: {}".format(
                topic, partition, offset, key, value
            ))
    else:
        print("No new messages")
