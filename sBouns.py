from datetime import datetime
weather_data = {}


def input_weather_data():
    city = input("Enter city name:").strip().title()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("This is an invalid date")
        return

    try:  # to solve the error from user 
        temperature = float(input("Enter temperature:"))
        humidity = float(input("Enter humidity (0-100):"))
    except ValueError:
        print("Temperature and humidity must be numbers")
        return

    if not city or not 0 <= humidity <= 100:
        print("Invalid city or humidity")
        return

    condition=input("Enter weather condition:").strip().lower()

    if not condition:
        print("Weather condition cannot be empty")
        return

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data saved successfully")


def query_by_city():
    city = input("Enter city to search: ").strip().title()

    if city not in weather_data:
        print("City not found")
        return

    print(f"\nWeather data for {city}:")

    for date, details in weather_data[city].items():
        print(f"Date: {date}")
        print(f"Temperature: {details['temperature']} C")
        print(f"Humidity: {details['humidity']}%")
        print(f"Condition: {details['condition']}")
        print("--------------------")


def update_weather_data():
    city = input("Enter city to update: ").strip().title()
    date = input("Enter date to update (YYYY-MM-DD): ").strip()

    if city not in weather_data or date not in weather_data[city]:
        print("Weather record not found")
        return

    try:
        temperature = float(input("Enter new temperature: "))
        humidity = float(input("Enter new humidity (0-100): "))
    except ValueError:
        print("Temperature and humidity must be numbers")
        return

    if not 0 <= humidity <= 100:
        print("Humidity must be between 0 and 100")
        return

    condition = input("Enter new weather condition: ").strip().lower()

    if not condition:
        print("Weather condition cannot be empty")
        return

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data updated successfully")


def delete_weather_data():
    city = input("Enter city to delete from: ").strip().title()
    date = input("Enter date to delete (YYYY-MM-DD): ").strip()

    if city not in weather_data or date not in weather_data[city]:
        print("Weather record not found")
        return

    del weather_data[city][date]

    if not weather_data[city]:
        del weather_data[city]

    print("Weather data deleted successfully")


while True:
    print("\n Weather Data")
    print("1. Add weather data")
    print("2. Query weather by city")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Close")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        input_weather_data()
    elif choice == "2":
        query_by_city()
    elif choice == "3":
        update_weather_data()
    elif choice == "4":
        delete_weather_data()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1-5.")
