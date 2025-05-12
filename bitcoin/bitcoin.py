import sys
import requests
import json

def main():
    amount_btc = amount()
    btc_per_coin= float(parse())

    total = amount_btc * btc_per_coin
    total = round(total, 4)
    print(f"${total:,}")

def parse():
    try:
        bitcoin_api = requests.get("http://rest.coincap.io/v3/assets/bitcoin?apiKey=8d8652139310e7f7c15a28a51282a2be9f694ce78cf06b7a197bbb23de4588a7")
        response = bitcoin_api.json()
        return response['data']['priceUsd']

    except requests.RequestException:
        pass

def amount():
    if len(sys.argv) == 2:
        try:
            amount = float(sys.argv[1])
            return amount
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()
