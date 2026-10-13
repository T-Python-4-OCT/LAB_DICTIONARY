weather_database = {}

def add_weather_data():
    print("\n--- Add Weather Data ---")
    city = input("Enter city name: ").strip().lower()
    date = input("Enter date (e.g., YYYY-MM-DD): ").strip()
    
    try:
        temp = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
    except ValueError:
        print("Error: Temperature and humidity must be numbers.")
        return

    condition = input("Enter weather condition (e.g., Sunny, Rainy): ").strip().capitalize()

    if city not in weather_database:
        weather_database[city] = {}

    weather_database[city][date] = {
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }
    print(f"Successfully added weather data for {city.capitalize()} on {date}.")

def query_weather_by_city():
    print("\n--- Query Weather by City ---")
    city = input("Enter city name to search: ").strip().lower()
    
    if city in weather_database and weather_database[city]:
        print(f"\nWeather records for {city.capitalize()}:")
        for date, details in weather_database[city].items():
            print(f"  Date: {date}")
            print(f"    - Temperature: {details['temp']}°C")
            print(f"    - Humidity: {details['humidity']}%")
            print(f"    - Condition: {details['condition']}")
    else:
        print(f"Sorry, no weather data found.")

def update_weather_data():
    print("\n--- Update Weather Data ---")
    city = input("Enter city name: ").strip().lower()
    
    if city not in weather_database or not weather_database[city]:
        print(f"No records found for this city.")
        return

    # عرض التواريخ المسجلة لهذه المدينة لتوضيحها للمستخدم
    print(f"\nAvailable dates for {city.capitalize()}:")
    for existing_date in weather_database[city].keys():
        print(f" - {existing_date}")

    date = input("\nEnter the exact date of the record you want to update (e.g., YYYY-MM-DD): ").strip()
    
    if date not in weather_database[city]:
        print(f"Error: The date '{date}' does not exist for this city.")
        return

    try:
        temp = float(input("Enter new temperature (°C): "))
        humidity = float(input("Enter new humidity (%): "))
    except ValueError:
        print("Error: Temperature and humidity must be numbers.")
        return

    condition = input("Enter new weather condition: ").strip().capitalize()

    # تحديث البيانات في القاموس المتداخل
    weather_database[city][date] = {
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }
    print(f"Successfully updated weather data for {city.capitalize()} on {date}!")
def update_weather_data():
    print("\n--- Update Weather Data ---")
    city = input("Enter city name: ").strip().lower()
    
    if city not in weather_database or not weather_database[city]:
        print(f"No records found.")
        return

    date = input("Enter the date of the record you want to update (YYYY-MM-DD): ").strip()
    if date not in weather_database[city]:
        print(f"No record found for this date.")
        return

    try:
        temp = float(input("Enter new temperature (°C): "))
        humidity = float(input("Enter new humidity (%): "))
    except ValueError:
        print("Error: Temperature and humidity must be numbers.")
        return

    condition = input("Enter new weather condition: ").strip().capitalize()

    weather_database[city][date] = {
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }
    print(f"Successfully updated weather data for {city.capitalize()} on {date}.")

def delete_weather_data():
    print("\n--- Delete Weather Data ---")
    city = input("Enter city name: ").strip().lower()
    
    if city not in weather_database or not weather_database[city]:
        print(f"No records found.")
        return

    date = input("Enter the date of the record you want to delete (YYYY-MM-DD): ").strip()
    if date not in weather_database[city]:
        print(f"No record found for this date.")
        return

    del weather_database[city][date]
    print(f"Successfully deleted weather record for {city.capitalize()} on {date}.")

    if not weather_database[city]:
        del weather_database[city]

def main():
    while True:
        print("\n==============================")
        print("   WEATHER AGGREGATION SYSTEM ")
        print("==============================")
        print("1. Add Weather Data")
        print("2. Query Weather by City")
        print("3. Update Weather Data (Challenge)")
        print("4. Delete Weather Data (Challenge)")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            add_weather_data()
        elif choice == '2':
            query_weather_by_city()
        elif choice == '3':
            update_weather_data()
        elif choice == '4':
            delete_weather_data()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()