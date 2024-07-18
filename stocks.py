import requests

def get_stock_price(api_key, symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if "Time Series (1min)" in data:
            latest_time = max(data["Time Series (1min)"].keys())
            latest_data = data["Time Series (1min)"][latest_time]
            return {
                'symbol': symbol,
                'price': latest_data['4. close'],
                'time': latest_time
            }
        else:
            print("Error: No data found for symbol.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_stock_price(stock_data):
    if stock_data:
        print(f"Stock: {stock_data['symbol']}")
        print(f"Price: ${stock_data['price']}")
        print(f"Time: {stock_data['time']}")
    else:
        print("Error fetching data.")

def main():
    api_key = 'VM2TLE0YIWOHS0GJ'  # Replace with your actual API key
    symbol = input("Enter stock symbol: ").upper()  # Ensure symbol is uppercase

    stock_data = get_stock_price(api_key, symbol)
    display_stock_price(stock_data)

if __name__ == "__main__":
    main()