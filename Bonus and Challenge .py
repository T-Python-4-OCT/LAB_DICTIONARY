weather_data = {}


def input_weather():
    """Add weather data for a city and date."""
    city = input("Enter city name: ")
    date = input("Enter date: ")

    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))
    condition = input("Enter weather condition: ")

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data saved!")


def query_city():
    """Display all weather data for a city."""
    city = input("Enter city name: ")

    if city in weather_data:
        for date in weather_data[city]:
            print("Date:", date)
            print("Temperature:", weather_data[city][date]["temperature"])
            print("Humidity:", weather_data[city][date]["humidity"])
            print("Condition:", weather_data[city][date]["condition"])
    else:
        print("City not found!")


def update_weather():
    """Update weather data for a city and date."""
    city = input("Enter city name: ")
    date = input("Enter date: ")

    if city in weather_data and date in weather_data[city]:
        temperature = float(input("Enter new temperature: "))
        humidity = float(input("Enter new humidity: "))
        condition = input("Enter new condition: ")

        weather_data[city][date]["temperature"] = temperature
        weather_data[city][date]["humidity"] = humidity
        weather_data[city][date]["condition"] = condition

        print("Weather data updated!")
    else:
        print("City or date not found!")


def delete_weather():
    """Delete weather data for a city and date."""
    city = input("Enter city name: ")
    date = input("Enter date: ")

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]

        if len(weather_data[city]) == 0:
            del weather_data[city]

        print("Weather data deleted!")
    else:
        print("City or date not found!")


while True:
    print("\n1. Add weather data")
    print("2. Query by city")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        input_weather()
    elif choice == "2":
        query_city()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
