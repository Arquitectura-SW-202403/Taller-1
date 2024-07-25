const { Kafka } = require('@confluentinc/kafka-javascript').KafkaJS;

(async function (){
    const kafka = new Kafka({
        kafkaJS: {
            brokers: ['kafka_broker:9092']
        },
    });
    try {
        const producer = kafka.producer();
        await producer.connect();
        console.log("CONNECTED")
        
        const inter = setInterval(async () => {
            await producer.send({
                topic: 'testjs',
                messages: [
                    { value: 'Bid send' }
                ]
            })
            console.log("SEND!!!")
        }, 1000);

    } catch (e) {
        console.log(e)
    }
})();