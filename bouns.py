weather_data = {
    "Riyadh": {
        "2026-10-13": {"temperature": 35, "humidity": 20, "condition": "sunny"},
        "2026-10-14": {"temperature": 33, "humidity": 25, "condition": "cloudy"}
    },
    "Jeddah": {
        "2026-10-13": {"temperature": 38, "humidity": 60, "condition": "humid"}
    }
}
def add_weather(data, city, date, temperature, humidity, condition):
    """
    Add (or overwrite) one weather record for a city and date.
    Creates the city if it does not exist yet.

    Args:
        data: the nested dictionary (city -> date -> details).
        city: the city name.
        date: the date as YYYY-MM-DD.
        temperature: temperature in Celsius.
        humidity: humidity percentage (0-100).
        condition: weather condition, e.g. sunny, rainy.
    """
    if city not in data:
        data[city] = {}
    data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

def query_city(data, city):
    """
    Print all recorded weather data for a city.

    Args:
        data: the nested dictionary (city -> date -> details).
        city: the city name to look up.
    """
    if city not in data:
        print(f"No data found for {city}.")
        return
    print(f"Weather data for {city}:")
    for date, details in data[city].items():
        print(f"  {date}: {details['temperature']}°C, "
              f"humidity {details['humidity']}%, {details['condition']}")


def get_text(prompt):
    """
    Ask the user for text until it contains letters only.

    Args:
        prompt: the question shown to the user.

    Returns:
        str: the valid text in Title Case (e.g. "New York").
    """
    while True:
        text = input(prompt).strip()
        if text.replace(" ", "").isalpha():
            return text.title()
        print("invalid date. example: 2026-10-15")


def get_date():
    """
    Ask the user for a date until it matches the format YYYY-MM-DD.

    Returns:
        str: the valid date string.
    """
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()
        parts = date.split("-")
        if (len(parts) == 3 and all(p.isdigit() for p in parts)
                and len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2):
            return date
        print("Invalid date. Example: 2026-10-15")


def get_number(prompt, low, high):
    """
    Ask the user for a whole number within a range.

    Args:
        prompt: the question shown to the user.
        low: the smallest allowed value.
        high: the largest allowed value.

    Returns:
        int: the valid number.
    """
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print (f"Enter a number between {low} and {high}.")


def input_weather(data):
    """
    Collect a full weather record from the user and store it.

    Args:
        data: the nested dictionary (city -> date -> details).
    """
    city = get_text("City: ")
    date = get_date()
    temperature = get_number("Temperature (°C): ", -50, 60)
    humidity = get_number("Humidity (0-100): ", 0, 100)
    condition = get_text("Condition (sunny, rainy...): ").lower()
    add_weather(data, city, date, temperature, humidity, condition)
    print("Weather data saved.")



def delete_weather(data, city, date):
    """
    Delete one record. If the city has no dates left, delete the city too.

    Args:
        data: the nested dictionary (city -> date -> details).
        city: the city name.
        date: the date of the record to delete.
    """
    if city not in data or date not in data[city]:
        print("No record found for that city and date.")
        return
    del data[city][date]
    if not data[city]:
        del data[city]
    print("Record deleted.")


def update_weather(data, city, date):
    """
    Replace the values of an existing record.

    Args:
        data: the nested dictionary (city -> date -> details).
        city: the city name.
        date: the date of the record to update.
    """
    if city not in data or date not in data[city]:
        print("No record found for that city and date.")
        return
    temperature = get_number("New temperature (°C): ", -50, 60)
    humidity = get_number("New humidity (0-100): ", 0, 100)
    condition = get_text("New condition: ").lower()
    add_weather(data, city, date, temperature, humidity, condition)
    print("Record updated.")

def main():
    """Show the menu and run the program until the user exits."""
    while True:
        print("\n1. Add weather data")
        print("2. Query by city")
        print("3. Update a record")
        print("4. Delete a record")
        print("4. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            input_weather(weather_data)
        elif choice == "2":
            query_city(weather_data, get_text("City: "))
        elif choice == "3":
            update_weather(weather_data, get_text("City: "), get_date())
        elif choice == "4":
            delete_weather(weather_data, get_text("City: "), get_date())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 to 5.")


main()