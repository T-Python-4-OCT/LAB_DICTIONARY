weather_data = {}

def input_weather_data():
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    condition = input("Enter weather condition: ")

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data saved.")





def query_by_city():
    city = input("Enter city name to search: ")

    if city in weather_data:
        for date, details in weather_data[city].items():
            print("Date:", date)
            print("Temperature:", details["temperature"])
            print("Humidity:", details["humidity"])
            print("Condition:", details["condition"])
    else:
        print("City not found.")


def update_weather_data():
    city = input("Enter city name: ")
    date = input("Enter date: ")

    if city in weather_data and date in weather_data[city]:
        temperature = input("Enter new temperature: ")
        humidity = input("Enter new humidity: ")
        condition = input("Enter new condition: ")

        weather_data[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }

        print("Weather data updated.")
    else:
        print("Weather data not found.")


def delete_weather_data():
    city = input("Enter city name: ")
    date = input("Enter date: ")
   


    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]

        if not weather_data[city]:
            del weather_data[city]

        print("Weather data deleted.")
    else:
        print("Weather data not found.")


while True:
    print("\n1. Add weather data")
    print("2. Query by city")
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
        break
    else:
        print("Invalid choice.")
