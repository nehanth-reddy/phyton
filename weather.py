import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data.get('cod') != 200:
        print("Error:", data.get('message'))
    else:
        city = data['name']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city}: {temp}°C, {description}")

def main():
    api_key = '86bf80126768dd8914d569b8381a3d84'  # Replace with your actual API key
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
