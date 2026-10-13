import bonus


def read_optional_number(message, minimum=None, maximum=None):
    '''Read an optional number and validate its value.

    A blank response keeps the existing value. Invalid numbers are
    rejected, and the user is asked to try again.

    Args:
        message (str): Prompt shown to the user.
        minimum (float | None): Minimum permitted value, if any.
        maximum (float | None): Maximum permitted value, if any.

    Returns:
        float | None: The entered number, or None for a blank response.
    '''
    while True:
        value = input(message).strip()

        if value == "":
            return None

        try:
            number = float(value)
        except ValueError:
            print("Please enter a valid number!")
            continue

        if number != number or abs(number) == float("inf"):
            print("Invalid number!")
            continue

        if minimum is not None and number < minimum:
            print(f"Number must be at least {minimum}!")
            continue

        if maximum is not None and number > maximum:
            print(f"Number must not exceed {maximum}!")
            continue

        return number


def update_weather():
    '''Update every field of a weather record identified by city and date.

    First find the existing record using its current city and date.
    The user can change the city, date, temperature, humidity, and
    weather condition. Leaving a field blank preserves its old value.
    If the new city and date already belong to another record, ask
    permission before replacing that record. A moved record is deleted
    from its original location only after all inputs are validated.

    Returns:
        None: Prints the outcome and updates bonus.weather_data in place.
    '''
    city = input("Enter current city: ").strip().title()
    date = input("Enter current date (YYYY-MM-DD): ").strip()

    if city not in bonus.weather_data:
        print("City not found!")
        return

    if date not in bonus.weather_data[city]:
        print("Date not found for this city!")
        return

    old_record = bonus.weather_data[city][date]

    print("\nCurrent weather data:")
    print(f"City: {city}")
    print(f"Date: {date}")
    print(f"Temperature: {old_record['temperature']} C")
    print(f"Humidity: {old_record['humidity']}%")
    print(f"Condition: {old_record['condition']}")
    print("\nPress Enter to keep the old value.")

    new_city = input("New city: ").strip().title() or city

    while True:
        new_date = input("New date (YYYY-MM-DD): ").strip()
        if not new_date:
            new_date = date
            break
        if bonus.valid_date(new_date):
            break
        print("Invalid date! Use YYYY-MM-DD.")

    new_temperature = read_optional_number("New temperature: ")
    if new_temperature is None:
        new_temperature = old_record["temperature"]

    new_humidity = read_optional_number("New humidity (0-100): ", 0, 100)
    if new_humidity is None:
        new_humidity = old_record["humidity"]

    new_condition = input("New condition: ").strip().title()
    if not new_condition:
        new_condition = old_record["condition"]

    # A different city/date might already hold another weather report.
    moved = (new_city, new_date) != (city, date)
    if moved and new_date in bonus.weather_data.get(new_city, {}):
        answer = input(
            "A record already exists for the new city and date. "
            "Replace it? (yes/no): "
        ).strip().lower()
        if answer not in ("yes", "y"):
            print("Update cancelled. Original data was not changed.")
            return

    new_record = {
        "temperature": new_temperature,
        "humidity": new_humidity,
        "condition": new_condition,
    }

    if moved:
        bonus.weather_data[city].pop(date)
        if not bonus.weather_data[city]:
            bonus.weather_data.pop(city)
        if new_city not in bonus.weather_data:
            bonus.weather_data[new_city] = {}

    bonus.weather_data[new_city][new_date] = new_record

    print("\nWeather data updated successfully!")
    print(f"City: {new_city}")
    print(f"Date: {new_date}")
    print(f"Temperature: {new_record['temperature']} C")
    print(f"Humidity: {new_record['humidity']}%")
    print(f"Condition: {new_record['condition']}")


def delete_weather():
    '''Delete a weather record for a specific city and date.

    Ask the user to identify an existing report and confirm deletion.
    Remove the city key if that city has no remaining reports.

    Returns:
        None: Prints the outcome and updates bonus.weather_data in place.
    '''
    city = input("Enter city to delete from: ").strip().title()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    if city not in bonus.weather_data:
        print("City not found!")
        return

    if date not in bonus.weather_data[city]:
        print("Date not found for this city!")
        return

    print("\nRecord to delete:")
    print(f"City: {city}")
    print(f"Date: {date}")
    print(bonus.weather_data[city][date])

    confirm = input("Confirm delete? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        print("Delete cancelled.")
        return

    bonus.weather_data[city].pop(date)
    if not bonus.weather_data[city]:
        bonus.weather_data.pop(city)

    print("Weather data deleted successfully!")


def main():
    '''Run the extended weather-data management menu.

    Use the original add and search functions from bonus.py, along
    with the update and delete functions in this file.

    Returns:
        None: Stops when the user selects Exit.
    '''
    while True:
        print("\n===== WEATHER CHALLENGE =====")
        print("1. Add weather data")
        print("2. Search by city")
        print("3. Update weather data")
        print("4. Delete weather data")
        print("5. Show all data")
        print("6. Exit")

        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            bonus.add_weather()
        elif choice == "2":
            bonus.query_by_city()
        elif choice == "3":
            update_weather()
        elif choice == "4":
            delete_weather()
        elif choice == "5":
            if bonus.weather_data:
                print(bonus.weather_data)
            else:
                print("No data available!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
