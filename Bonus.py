from datetime import datetime
import math

weather_data = {}

def input_weather_data():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date")
        return

    try:
        temperature = float(input("Enter temperature: "))
        humidity = float(input("Enter humidity (0-100): "))

        if not math.isfinite(temperature) or not math.isfinite(humidity):
            print("Please enter valid numeric values")
            return

        if not 0 <= humidity <= 100:
            print("Invalid humidity")
            return

    except ValueError:
        print("Please enter valid numeric values")
        return

    condition = input("Enter weather condition: ").strip().lower()

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

    print("Weather data added successfully")


def query_by_city():
    city = input("Enter city name: ").strip()

    if city in weather_data:
        print("\nWeather data for", city)

        for date, details in weather_data[city].items():
            print("Date:", date)
            print("Temperature:", details["temperature"])
            print("Humidity:", details["humidity"])
            print("Condition:", details["condition"])
            print("------------------------")

    else:
        print("City not found")


def update_weather_data():
    city = input("Enter city name: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date")
        return

    if city not in weather_data or date not in weather_data[city]:
        print("Weather data not found")
        return

    try:
        temperature = float(input("Enter new temperature: "))
        humidity = float(input("Enter new humidity (0-100): "))

        if not math.isfinite(temperature) or not math.isfinite(humidity):
            print("Please enter valid numeric values")
            return

        if not 0 <= humidity <= 100:
            print("Invalid humidity")
            return

    except ValueError:
        print("Please enter valid numeric values")
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
    city = input("Enter city name: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date")
        return

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]

        if not weather_data[city]:
            del weather_data[city]

        print("Weather data deleted successfully")

    else:
        print("Weather data not found")


while True:
    print("\n--- Weather Data Aggregation ---")
    print("1. Add Weather Data")
    print("2. Query Weather Data by City")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")

    choice = input("Choose an option(any number from list): ").strip()

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
        print("Invalid choice. Please try again.")