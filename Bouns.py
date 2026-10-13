weather_data = {}


def input_weather():
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

    print("Weather data added successfully")


def query_city():
    city = input("Enter city name: ")

    if city in weather_data:
        print(weather_data[city])
    else:
        print("City not found")


def update_weather():
    city = input("Enter city name: ")
    date = input("Enter date: ")

    if city in weather_data and date in weather_data[city]:
        temperature = float(input("Enter new temperature: "))
        humidity = float(input("Enter new humidity: "))
        condition = input("Enter new weather condition: ")

        weather_data[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }

        print("Weather data updated successfully")
    else:
        print("Weather data not found")


def delete_weather():
    city = input("Enter city name: ")
    date = input("Enter date: ")

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        print("Weather data deleted successfully")
    else:
        print("Weather data not found")


while True:
    print("1. Add weather data")
    print("2. Search by city")
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
        print("Invalid choice")