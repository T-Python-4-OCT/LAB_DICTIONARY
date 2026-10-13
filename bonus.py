from datetime import datetime

weather = {}
conditions = ["sunny", "rainy", "cloudy", "windy", "snowy", "stormy", "foggy"]


def ask_city():
    while True:
        city = input("City name: ").strip()
        if city.replace(" ", "").isalpha():
            return city.title()
        print("Invalid city name.")


def ask_date():
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date.")


def ask_number(label, low, high):
    while True:
        try:
            value = float(input(label))
            if low <= value <= high:
                return value
        except ValueError:
            pass
        print(f"Enter a number between {low} and {high}.")


def ask_details():
    temperature = ask_number("Temperature (C): ", -90, 60)
    humidity = ask_number("Humidity (0-100): ", 0, 100)
    while True:
        condition = input("Condition (" + "/".join(conditions) + "): ").strip().lower()
        if condition in conditions:
            break
        print("Invalid condition.")
    return {"temperature": temperature, "humidity": humidity, "condition": condition}


def add_weather():
    city = ask_city()
    date = ask_date()
    if date in weather.get(city, {}):
        print("Data already exists. Use update.")
        return
    weather.setdefault(city, {})[date] = ask_details()
    print("Saved.")


def query_city():
    city = ask_city()
    if city not in weather:
        print("No data found.")
        return
    for date in sorted(weather[city]):
        data = weather[city][date]
        print(date, data["temperature"], "C", data["humidity"], "%", data["condition"])


def update_weather():
    city = ask_city()
    date = ask_date()
    if date not in weather.get(city, {}):
        print("No data found.")
        return
    weather[city][date] = ask_details()
    print("Updated.")


def delete_weather():
    city = ask_city()
    date = ask_date()
    if date not in weather.get(city, {}):
        print("No data found.")
        return
    del weather[city][date]
    if not weather[city]:
        del weather[city]
    print("Deleted.")


while True:
    print("\n1. Add  2. Query  3. Update  4. Delete  5. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_weather()
    elif choice == "2":
        query_city()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")