weather_data = {}


def valid_date(date):
    '''Check whether a date is valid in YYYY-MM-DD format.

    Args:
    date (str): Date to check, including year, month, and day.

    Returns:
    bool: True if the date is valid, including leap years; otherwise False.
    '''
    parts = date.split("-")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    if not all(part.isdigit() for part in parts):
        return False
    year, month, day = map(int, parts)
    if year < 1 or month < 1 or month > 12:
        return False
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days[1] = 29
    return 1 <= day <= days[month - 1]


def add_weather():
    '''Prompt for and store a city's weather report.

    Validate the city, date, temperature, humidity, and condition.
    Ask for confirmation before replacing a record for the same date.

    Returns:
    None: Updates the module-level weather_data dictionary in place.
    '''
    while True:
        city = input("Enter city: ").strip().title()
        if city:
            break
        print("City cannot be empty!")
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if valid_date(date):
            break
        print("Invalid date!")
    while True:
        try:
            temperature = float(input("Enter temperature: "))
            if temperature == temperature and abs(temperature) != float("inf"):
                break
            print("Invalid temperature!")
        except ValueError:
            print("Please enter a valid number!")
    while True:
        try:
            humidity = float(input("Enter humidity (0-100): "))
            if 0 <= humidity <= 100:
                break
            print("Humidity must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")
    while True:
        condition = input("Enter condition: ").strip().title()
        if condition:
            break
        print("Condition cannot be empty!")
    if city not in weather_data:
        weather_data[city] = {}
    if date in weather_data[city]:
        answer = input("Date exists. Replace? (yes/no): ").strip().lower()
        if answer not in ("yes", "y"):
            print("Data not changed.")
            return
    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
    print("Weather data added successfully!")


def query_by_city():
    '''Display all recorded weather information for a city.

    Ask for a city name, then print its entries ordered by date.
    Print an error message if the city does not exist.

    Returns:
    None: Displays weather information without returning a value.
    '''
    city = input("Enter city to search: ").strip().title()
    if city not in weather_data:
        print("City not found!")
        return
    print(f"\nWeather data for {city}:")
    for date, weather in sorted(weather_data[city].items()):
        print(f"\nDate: {date}")
        print(f"Temperature: {weather['temperature']} C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Condition: {weather['condition']}")


def main():
    '''Run the original weather-data command-line menu.

    Allow the user to add, search for, and view weather records
    until the Exit option is selected.

    Returns:
    None: Exits the menu when requested by the user.
    '''
    while True:
        print("\n===== WEATHER SYSTEM =====")
        print("1. Add weather data")
        print("2. Search by city")
        print("3. Show all data")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            add_weather()
        elif choice == "2":
            query_by_city()
        elif choice == "3":
            if weather_data:
                print(weather_data)
            else:
                print("No data available!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
