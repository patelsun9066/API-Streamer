import json
import time

import requests
from quixstreams import Application

app = Application(broker_address="localhost:9092", loglevel="DEBUG")

while True:

    res = requests.get("https://api.open-meteo.com/v1/forecast", params={
        "latitude": 40.41,
        "longitude": -74.35,
        "current": "temperature_2m",
    })
    weather = res.json()

    with app.get_producer() as producer:
        producer.produce(topic='weather_data', key="London", value=json.dumps(weather))

    time.sleep(5)

