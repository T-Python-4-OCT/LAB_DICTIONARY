weather_data = {}


def ask_city():
    while True:
        city = input("City name: ").strip().title()
        if city.replace(" ", "").isalpha():
            return city
        print("Invalid city name, use letters only")


def ask_date():
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()
        parts = date.split("-")
        if (len(parts) == 3 and len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2
                and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
            month = int(parts[1])
            day = int(parts[2])
            if 1 <= month <= 12 and 1 <= day <= 31:
                return date
        print("Invalid date, use the format YYYY-MM-DD")


def ask_number(message, low, high):
    while True:
        text = input(message).strip()
        if text[:1] == "-":
            digits = text[1:]
        else:
            digits = text
        if digits.isdigit() and low <= int(text) <= high:
            return int(text)
        print(f"Please enter a number between {low} and {high}")


def ask_condition():
    while True:
        condition = input("Condition (e.g. sunny, rainy): ").strip().lower()
        if condition.replace(" ", "").isalpha():
            return condition
        print("Invalid condition, use letters only")


def ask_details():
    temperature = ask_number("Temperature (C): ", -50, 60)
    humidity = ask_number("Humidity (%): ", 0, 100)
    condition = ask_condition()
    return {"temperature": temperature, "humidity": humidity, "condition": condition}


def add_weather():
    city = ask_city()
    date = ask_date()
    if city in weather_data and date in weather_data[city]:
        print("This date already exists, use update instead")
        return
    if city not in weather_data:
        weather_data[city] = {}
    weather_data[city][date] = ask_details()
    print(f"Saved weather for {city} on {date}")


def query_city():
    city = ask_city()
    if city not in weather_data:
        print("No data for this city")
        return
    print(f"Weather data for {city}:")
    for date, details in weather_data[city].items():
        print(f"  {date}: {details['temperature']}C, {details['humidity']}% humidity, {details['condition']}")


def update_weather():
    city = ask_city()
    date = ask_date()
    if city not in weather_data or date not in weather_data[city]:
        print("No data for this city and date")
        return
    weather_data[city][date] = ask_details()
    print(f"Updated weather for {city} on {date}")


def delete_weather():
    city = ask_city()
    date = ask_date()
    if city not in weather_data or date not in weather_data[city]:
        print("No data for this city and date")
        return
    del weather_data[city][date]
    if len(weather_data[city]) == 0:
        del weather_data[city]
    print(f"Deleted weather for {city} on {date}")


def main():
    while True:
        print()
        print("1. Add weather data")
        print("2. Query by city")
        print("3. Update weather data")
        print("4. Delete weather data")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_weather()
        elif choice == "2":
            query_city()
        elif choice == "3":
            update_weather()
        elif choice == "4":
            delete_weather()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()
