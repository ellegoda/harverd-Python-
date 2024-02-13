import sys
import requests


def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        if response.status_code == 200:
            data = response.json()
            bitcoin_price = float(data["bpi"]["USD"]["rate"].replace(",", ""))

            return bitcoin_price
        else:
            print(f"Error: Failed to retrieve Bitcoin price. Status Code: {response.status_code}")
            sys.exit(1)

    except Exception as e:
        print(f"Error: An exception occurred - {e}")
        sys.exit(1)


def main():
    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        else:
            bitcoins_to_buy = float(sys.argv[1])
            bitcoin_price = get_bitcoin_price()

            print(f"${bitcoins_to_buy * bitcoin_price:,.4f}")

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


if __name__ == "__main__":
    main()
