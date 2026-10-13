weather_data = {}


def ask_details():
    """Ask for temperature, humidity, condition. Return a dictionary, or None if invalid."""
    try:
        temperature = float(input("Temperature: "))
        humidity = float(input("Humidity (0-100): "))
    except ValueError:
        print("Temperature and humidity must be numbers")
        return 
    if humidity < 0 or humidity > 100:
        print("Humidity must be between 0 and 100")
        return 
    condition = input("Condition (sunny, rainy, ...): ").strip().lower()
    if not condition.isalpha():
        print("Invalid condition")
        return 
    return {"temperature": temperature, "humidity": humidity, "condition": condition}


def input_weather_data():
    city = input("City: ").strip().title()
    date = input("Date (YYYY-MM-DD): ").strip()
    if not city.replace(" ", "").isalpha() or len(date) != 10:
        print("Invalid city or date")
        return
    details = ask_details()
    if details is not None:
        weather_data.setdefault(city, {})[date] = details
        print("Saved")


def query_by_city():
    city = input("City: ").strip().title()
    if city not in weather_data:
        print("No data for this city")
        return
    for date, d in weather_data[city].items():
        print(date, d["temperature"], d["humidity"], d["condition"])


def update_weather_data():
    city = input("City: ").strip().title()
    date = input("Date (YYYY-MM-DD): ").strip()
    if city in weather_data and date in weather_data[city]:
        details = ask_details()
        if details is not None:
            weather_data[city][date] = details
            print("Updated")
    else:
        print("Record not found")


def delete_weather_data():
    city = input("City: ").strip().title()
    date = input("Date (YYYY-MM-DD): ").strip()
    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        if len(weather_data[city]) == 0:
            del weather_data[city]
        print("Deleted")
    else:
        print("Record not found")


while True:
    choice = input("\n1-Add  2-Query  3-Update  4-Delete  5-Exit: ")
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
        print("Invalid option")