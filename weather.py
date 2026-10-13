weather_database = {}

def add_weather():
    city = input("Enter city name: ")
    date = input("Enter date (e.g., 2026-10-13): ")
    temp = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    condition = input("Enter weather condition (e.g., Sunny): ")

    weather_database[city] = {
        "date": date,
        "temperature": temp,
        "humidity": humidity,
        "condition": condition
    }
    print("Weather data added successfully!\n")

def query_city():
    city = input("Enter city name to search: ")
    
    if city in weather_database:
        print(f"\n--- Weather Details for {city} ---")
        for key, value in weather_database[city].items():
            print(f"{key}: {value}")
        print("-" * 30)
    else:
        print("Sorry, the city is not found in the database.\n")

add_weather()

query_city()