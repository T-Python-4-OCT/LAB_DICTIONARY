weather_data = {}


CITY_NAME_ALIASES = {
    "riyadh": "riyadh",
   
}


def normalize_city_name(city):
    normalized_city = city.strip().casefold()
    return CITY_NAME_ALIASES.get(normalized_city, normalized_city)


def find_city_key(city):
    normalized_city = normalize_city_name(city)
    return next(
        (stored_city for stored_city in weather_data
         if normalize_city_name(stored_city) == normalized_city),
        None
    )


def add_weather():
    city = input("Enter city name: ").strip()
    date = input("Enter date: ")
    temperature = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    condition = input("Enter weather condition: ")

    if city == "" or date == "" or condition == "":
        print("Invalid input")
        return

    if not temperature.replace("-", "", 1).isdigit():
        print("Invalid temperature")
        return

    if not humidity.isdigit():
        print("Invalid humidity")
        return

    humidity = int(humidity)

    if humidity < 0 or humidity > 100:
        print("Invalid humidity")
        return

    temperature = int(temperature)

    if city not in weather_data:
        existing_city = find_city_key(city)
        if existing_city is not None:
            city = existing_city
        else:
            weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data added successfully")


def query_city():
    city = input("Enter city name: ").strip()
    city_key = find_city_key(city)

    if city_key is not None:
        print(f"Weather data for {city_key}:")

        for date, details in weather_data[city_key].items():
            print(f"Date: {date}")
            print(f"Temperature: {details['temperature']}")
            print(f"Humidity: {details['humidity']}%")
            print(f"Condition: {details['condition']}")
            print()

    else:
        print("City not found")


def update_weather():
    city = input("Enter city name: ").strip()
    date = input("Enter date: ")
    city_key = find_city_key(city)

    if city_key is None:
        print("City not found")
        return

    if date not in weather_data[city_key]:
        print("Date not found")
        return

    temperature = input("Enter new temperature: ")
    humidity = input("Enter new humidity: ")
    condition = input("Enter new weather condition: ")

    if not temperature.replace("-", "", 1).isdigit():
        print("Invalid temperature")
        return

    if not humidity.isdigit():
        print("Invalid humidity")
        return

    humidity = int(humidity)

    if humidity < 0 or humidity > 100:
        print("Invalid humidity")
        return

    weather_data[city_key][date]["temperature"] = int(temperature)
    weather_data[city_key][date]["humidity"] = humidity
    weather_data[city_key][date]["condition"] = condition

    print("Weather data updated successfully")


def delete_weather():
    city = input("Enter city name: ").strip()
    date = input("Enter date: ")
    city_key = find_city_key(city)

    if city_key is None:
        print("City not found")
        return

    if date not in weather_data[city_key]:
        print("Date not found")
        return

    del weather_data[city_key][date]

    print("Weather data deleted successfully")


while True:
    print()
    print("1. Add weather data")
    print("2. Search by city")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_weather()

    elif choice == "2":
        query_city()

    elif choice == "3":
        update_weather()

    elif choice == "4":
        delete_weather()

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")

