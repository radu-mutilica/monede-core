# monede-core #
Core backend components for monede.live

## What is it? ##
A simple flask backend for the [monede.live](https://github.com/radu-mutilica/monede.live "monede.live") crypto trends aggregator website. It fetches data from multiple crypto APIs (currently coingecko and binance) and Google Trends and merges them together into a digestable visual format.

## Running it
We rely on coingecko for providing a list of all the indexed coins. Ideally wanted to also use it to provide historical price and volume data, however the data resolution is too low, so we use binance for that.
It is recommended to use a virtual environment to install the requirements.txt dependencies first.
```bash
export BINANCE_API_KEY=<your_key>
export BINANCE_API_SECRET=<your_secret>
export FLASK_ENV=development

# run the flask app, it will start listening for commands
cd <root>
flask run

# check if it works by going to http://127.0.0.1:5000/ping
```
