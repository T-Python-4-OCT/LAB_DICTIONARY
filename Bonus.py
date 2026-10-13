weather_data = {}

def input_weather():
    city = input("Enter city name: ").strip().title()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    temp = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    condition = input("Enter weather condition: ").strip().lower()

    if city == "" or date == "" or condition == "":
        print("Please fill in all fields.")
    elif len(date) != 10 or date[4] != "-" or date[7] != "-" or not date.replace("-", "").isdigit():
        print("Invalid date. Use YYYY-MM-DD.")
    elif not temp.lstrip("-").replace(".", "", 1).isdigit():
        print("Invalid temperature.")
    elif not humidity.isdigit():
        print("Invalid humidity.")
    elif int(humidity) < 0 or int(humidity) > 100:
        print("Humidity must be between 0 and 100.")
    else:
        if city not in weather_data:
            weather_data[city] = {}

        weather_data[city][date] = {
            "temperature": float(temp),
            "humidity": int(humidity),
            "condition": condition
        }

        print("Weather data is saved successfully.")


def show_query_city():
    city = input("Enter city to search: ").strip().title()

    if city in weather_data:
        for date, info in weather_data[city].items():
            print(date, info)
    else:
        print("City not found.")


def update_weather():
    city = input("Enter city to update: ").strip().title()
    date = input("Enter date: ").strip()

    if city in weather_data and date in weather_data[city]:
        print("Enter new weather data:")
        input_weather_for_update(city, date)
    else:
        print("Weather data not found.")


def input_weather_for_update(city, date):
    temp = input("Enter new temperature: ")
    humidity = input("Enter new humidity: ")
    condition = input("Enter new condition: ").strip().lower()

    if condition == "":
        print("Invalid condition.")
    elif not temp.lstrip("-").replace(".", "", 1).isdigit():
        print("Invalid temperature.")
    elif not humidity.isdigit():
        print("Invalid humidity.")
    elif int(humidity) < 0 or int(humidity) > 100:
        print("Humidity must be between 0 and 100.")
    else:
        weather_data[city][date] = {
            "temperature": float(temp),
            "humidity": int(humidity),
            "condition": condition
        }
        print("Weather data updated.")


def delete_weather():
    city = input("Enter city to delete: ").strip().title()
    date = input("Enter date: ").strip()

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]

        if len(weather_data[city]) == 0:
            del weather_data[city]

        print("Weather data deleted.")
    else:
        print("Weather data not found.")


while True:
    print("\n1. Add weather data")
    print("2. Show Query city")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        input_weather()
    elif choice == "2":
        show_query_city()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")