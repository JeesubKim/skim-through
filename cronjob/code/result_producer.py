from kafka import KafkaProducer

from json import dumps
import time




producer = KafkaProducer(
    acks=1,
    compression_type="gzip",
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8")
)


start = time.time()

topic = "result"
data = {
    "oid":1234,
    "uuid":12441224,
    "user_id":"abc",
    "type":"qfc",
    "link":"https://www.qfc.com/search?query=kiwi&searchType=default_search",
}

producer.send(topic=topic, value=data)
producer.flush()

print(f"Sent to {topic}: ", data)