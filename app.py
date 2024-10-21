from flask import Flask, jsonify, render_template
import requests
from datetime import datetime

app = Flask(__name__)

# Example API URL for CoinGecko
COIN_GECKO_API_URL = 'https://api.coingecko.com/api/v3/coins/'

# Helper function to get price data from CoinGecko
def fetch_coin_prices(coin_id):
    try:
        response = requests.get(f'{COIN_GECKO_API_URL}{coin_id}/market_chart', params={
            'vs_currency': 'usd',
            'days': '7'
        })
        data = response.json()
        prices = [
            {'date': datetime.utcfromtimestamp(price[0] / 1000), 'price': price[1]}
            for price in data['prices']
        ]
        return prices
    except Exception as e:
        print(f'Error fetching {coin_id} prices: {e}')
        return []

# Routes to serve the charts
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bitcoin-prices')
def bitcoin_prices():
    prices = fetch_coin_prices('bitcoin')
    return jsonify(prices)

@app.route('/api/ethereum-prices')
def ethereum_prices():
    prices = fetch_coin_prices('ethereum')
    return jsonify(prices)

@app.route('/api/solana-prices')
def solana_prices():
    prices = fetch_coin_prices('solana')
    return jsonify(prices)

@app.route('/api/bnb-prices')
def bnb_prices():
    prices = fetch_coin_prices('binancecoin')
    return jsonify(prices)

@app.route('/api/avax-prices')
def avax_prices():
    prices = fetch_coin_prices('avalanche-2')
    return jsonify(prices)

@app.route('/api/optimism-prices')
def optimism_prices():
    prices = fetch_coin_prices('optimism')
    return jsonify(prices)

@app.route('/api/arbitrum-prices')
def arbitrum_prices():
    prices = fetch_coin_prices('arbitrum')
    return jsonify(prices)

@app.route('/api/fantom-prices')
def fantom_prices():
    prices = fetch_coin_prices('fantom')
    return jsonify(prices)

@app.route('/api/conflux-prices')
def conflux_prices():
    prices = fetch_coin_prices('conflux-token')
    return jsonify(prices)

@app.route('/api/kava-prices')
def kava_prices():
    prices = fetch_coin_prices('kava')
    return jsonify(prices)

@app.route('/api/moonbeam-prices')
def moonbeam_prices():
    prices = fetch_coin_prices('moonbeam')
    return jsonify(prices)

if __name__ == '__main__':
    app.run(debug=True)
