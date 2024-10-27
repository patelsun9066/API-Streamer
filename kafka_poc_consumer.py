from quixstreams import Application
import json

app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
    consumer_group="weather_data_consumer"
)

with app.get_consumer() as consumer:
    consumer.subscribe(["weather_data"])
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            print("no message")
            continue
        else:
            key = msg.key().decode('utf-8')
            value = json.loads(msg.value())
            print(value)
