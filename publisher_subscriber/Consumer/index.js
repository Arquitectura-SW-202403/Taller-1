const { Kafka } = require('@confluentinc/kafka-javascript').KafkaJS;

(async function (){
    const consumer = new Kafka().consumer({
        'bootstrap.servers': 'kafka_broker:9092',
        'group.id': process.env.KAFKA_ID,
        'auto.offset.reset': 'earliest',
    });
    
    await consumer.connect();    
    await consumer.subscribe({ topics: ["testjs"] });

    consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
          console.log({
            topic,
            partition,
            received_by: process.env.KAFKA_ID,
            value: message.value.toString(),
          });
        }
      });
})();