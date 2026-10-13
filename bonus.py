#
weather_data = {}


def input_weather_data():
    city = input("Enter city name: ").title()
    date = input("Enter date (YYYY-MM-DD): ")

    if not city:
        print("Invalid city name!")
        return

    if (len(date) != 10 or date[4] != "-"
            or date[7] != "-"):
        print("Invalid date format!")
        return

    try:
        temperature = float(input("Enter temperature: "))
        humidity = float(input("Enter humidity: "))
    except ValueError:
        print("Temperature and humidity must be numbers!")
        return

    if humidity < 0 or humidity > 100:
        print("Humidity must be between 0 and 100!")
        return

    condition = input(
        "Enter condition (sunny/rainy/cloudy): "
    ).lower()

    if condition not in ["sunny", "rainy", "cloudy"]:
        print("Invalid weather condition!")
        return

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data added successfully!")


def query_by_city():
    city = input("Enter city name: ").title()

    if city not in weather_data:
        print("City not found!")
        return

    for date, details in weather_data[city].items():
        print("Date:", date)
        print("Temperature:", details["temperature"])
        print("Humidity:", details["humidity"])
        print("Condition:", details["condition"])
        print("--------------------")


def update_weather_data():
    city = input("Enter city name: ").title()
    date = input("Enter date (YYYY-MM-DD): ")

    if city not in weather_data or date not in weather_data[city]:
        print("Record not found!")
        return

    try:
        temperature = float(input("Enter new temperature: "))
        humidity = float(input("Enter new humidity: "))
    except ValueError:
        print("Please enter numbers!")
        return

    if humidity < 0 or humidity > 100:
        print("Invalid humidity!")
        return

    condition = input("Enter new condition: ").lower()

    if condition not in ["sunny", "rainy", "cloudy"]:
        print("Invalid condition!")
        return

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data updated successfully!")


def delete_weather_data():
    city = input("Enter city name: ").title()
    date = input("Enter date (YYYY-MM-DD): ")

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]

        if not weather_data[city]:
            del weather_data[city]

        print("Weather data deleted successfully!")
    else:
        print("Record not found!")


while True:
    print("\n===== Weather Data Aggregation =====")
    print("1. Add weather data")
    print("2. Query weather by city")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Exit")

    choice = input("Choose an option: ")

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
        print("Invalid choice! Please try again.")