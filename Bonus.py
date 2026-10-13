def input_weather_data(weather_data):
    city = input("Enter city name: ").strip()
    date = input("Enter date (e.g., YYYY-MM-DD): ").strip()
    temp = input("Enter temperature: ").strip()
    humidity = input("Enter humidity: ").strip()
    condition = input("Enter weather condition (e.g., sunny, rainy): ").strip()
    
    if not city or not date or not temp or not humidity or not condition:
        print("Invalid input. Data cannot be empty.")
        return
        
    if city not in weather_data:
        weather_data[city] = {}
        
    weather_data[city][date] = {
        "temperature": temp,
        "humidity": humidity,
        "condition": condition
    }
    print("Weather data added successfully.")

def query_weather_data(weather_data):
    city = input("Enter city name to query: ").strip()
    if city in weather_data:
        print(f"\nWeather data for {city}:")
        for date, details in weather_data[city].items():
            print(f"Date: {date} | Temp: {details['temperature']} | Humidity: {details['humidity']} | Condition: {details['condition']}")
    else:
        print("Sorry, no weather data found for this city.")

weather_data = {}

while True:
    print("\n1. Add Weather Data")
    print("2. Query Weather Data")
    print("3. Exit")
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        input_weather_data(weather_data)
    elif choice == "2":
        query_weather_data(weather_data)
    elif choice == "3":
        break
    else:
        print("Invalid choice, please try again.")