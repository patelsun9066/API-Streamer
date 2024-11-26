import json
import time

import requests
from quixstreams import Application

app = Application(broker_address="localhost:29092", loglevel="DEBUG")

while True:

    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-price"
    querystring = {"region": "US", "symbol": "AAPL"}
    headers = {
        "x-rapidapi-key": "127e2bf455msh6cd398823023b2ep121aa1jsn8dfb270a9c75",
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }

    res = requests.get(url, headers=headers, params=querystring)
    print(res)
    stock_price_data = res.json()

    with app.get_producer() as producer:
        producer.produce(topic='stock_price_data', key="ticker_price", value=json.dumps(stock_price_data))

    time.sleep(5)

