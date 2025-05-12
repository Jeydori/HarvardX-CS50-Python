import requests
class CoinAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://rest.coinapi.io/v1/'

    def get_historical_prices(self, symbol, start_date, end_date):
        url = f"{self.base_url}ohlcv/{symbol}/USD/history?period_id=1DAY&time_start={start_date}&time_end={end_date}"
        headers = {'X-CoinAPI-Key': self.api_key}

        response = requests.get(url, headers=headers)
        data = response.json()

        return data
