from kafka import KafkaConsumer
from json import loads


topic = "result"
consumer = KafkaConsumer(
    # topic,
    bootstrap_servers="localhost:9092",
    auto_offset_reset ="latest",
    enable_auto_commit=True,
    # group_id="batch-processor",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
    consumer_timeout_ms=1000
)

consumer.subscribe(topics=[topic])


while True:

    for message in consumer:
        print(f'Topic : {message.topic}, Partition : {message.partition}, Offset : {message.offset}, Key : {message.key}, value : {message.value}')
 
print('[End] get consumer')
