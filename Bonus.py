weather_data = {}


def add_weather_data():
    city = input("Enter city name: ").capitalize()
    if not city.isalpha() or city == "":
        print("Please enter a valid city name.")
        return
    date = input("Enter date (YYYY-MM-DD): ")
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        print("Please enter a valid date in the format YYYY-MM-DD.")
        return
    temp = input("Enter temperature (°C): ")
    if not temp.replace('.', '', 1).replace('-', '', 1).isdigit():
        print("Please enter a valid temperature.")
        return 
    humidity = input("Enter humidity (%): ")
    if not humidity.isdigit():
        print("Humidity must be a number.")
        return

    if int(humidity) < 0 or int(humidity) > 100:
        print("Humidity must be between 0 and 100.")
        return
    condition = input("Enter weather condition (e.g., Sunny, Rainy): ").capitalize()
    if condition == "":
        print("Weather condition cannot be empty.")
        return

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }

    print(f"Data for {city} on {date} has been added.")


def query_by_city():
    city = input("Enter city name to view weather: ").capitalize()
    
    if city == "":
        print("City name cannot be empty.")
        return

    if city in weather_data:
        print(f"\nWeather data for {city}:")
        for date, info in weather_data[city].items():
            print(f"Date: {date}")
            print(f"    Temperature: {info['temp']}°C")
            print(f"    Humidity: {info['humidity']}%")
            print(f"    Condition: {info['condition']}\n")
            print("-----------------------------\n")
    else:
        print("City not found.")


def update_or_delete():
    city = input("Enter city name: ").capitalize()
    date = input("Enter date to update or delete (YYYY-MM-DD): ")
    
    if city == "":
        print("City name cannot be empty.")
        return
    if date == "":
        print("Date cannot be empty.")
        return

    if city in weather_data and date in weather_data[city]:
        action = input("Type 'update' or 'delete': ").lower()

        if action == "update":
            print("1. Update temperature")
            print("2. Update humidity")
            print("3. Update weather condition")
            print("4. Update all fields")
            print("5. Go back to main menu")

            choice = input("Choose what to update (1-5): ")

            if choice == "1":
                temp = input("New temperature (°C): ")
                if not temp.replace('.', '', 1).replace('-', '', 1).isdigit():
                    print("Please enter a valid temperature.")
                    return
                weather_data[city][date]["temp"] = temp
                print(f"Weather data updated successfully for {city} on {date}.")
            elif choice == "2":
                humidity = input("New humidity (%): ")
                if not humidity.isdigit():
                    print("Humidity must be a number.")
                    return
                if int(humidity) < 0 or int(humidity) > 100:
                    print("Humidity must be between 0 and 100.")
                    return
                weather_data[city][date]["humidity"] = humidity
                print(f"Weather data updated successfully for {city} on {date}.")
            elif choice == "3":
                condition = input("New weather condition: ").capitalize()
                if condition == "":
                    print("Weather condition cannot be empty.")
                    return
                weather_data[city][date]["condition"] = condition
                print(f"Weather data updated successfully for {city} on {date}.")
            elif choice == "4":
                temp = input("New temperature (°C): ")
                if not temp.replace('.', '', 1).replace('-', '', 1).isdigit():
                    print("Please enter a valid temperature.")
                    return
                humidity = input("New humidity (%): ")
                if not humidity.isdigit():
                    print("Humidity must be a number.")
                    return
                if int(humidity) < 0 or int(humidity) > 100:
                    print("Humidity must be between 0 and 100.")
                    return
                condition = input("New weather condition: ").capitalize()
                if condition == "":
                    print("Weather condition cannot be empty.")
                    return
                weather_data[city][date] = {
                    "temp": temp,
                    "humidity": humidity,
                    "condition": condition
                }
                print(f"Weather data updated successfully for {city} on {date}.")
            elif choice == "5":
                return
            else:
                print("Invalid choice.")


        elif action == "delete":
            del weather_data[city][date]
            print(f"Weather data deleted successfully for {city} on {date}.")
        else:
            print("Invalid action.")
    else:
        print("City or date not found.")

def main():
    while True:
        print("\n--- Weather Data Program ---")
        print("1. Add weather data")
        print("2. Query by city")
        print("3. Update/Delete data")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_weather_data()
        elif choice == "2":
            query_by_city()
        elif choice == "3":
            update_or_delete()
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice, try again.")

main()