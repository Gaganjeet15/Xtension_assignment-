import requests

api_key = 'c5609bbd94c3d694cb651d8bfc1f8bb6'  
city = input("Enter city name: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Extracting  information
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather_description = data['weather'][0]['description']

    
    # Display the formatted weather information
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature} °C")
    print(f"Feels Like: {feels_like} °C")
    print(f"Description: {weather_description}")

else:
    print("Error fetching data:", response.status_code)