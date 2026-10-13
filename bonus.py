weather_data = {}

while True:
    print("\n--- Weather Data System ---")
    print("1. Add Weather Data")
    print("2. Query Weather by City")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        city = input("Enter city name: ").strip()
        date = input("Enter date (e.g., YYYY-MM-DD): ").strip()
        temp = input("Enter temperature: ").strip()
        humidity = input("Enter humidity: ").strip()
        condition = input("Enter weather condition: ").strip()

        if city not in weather_data:
            weather_data[city] = {}

        weather_data[city][date] = {
            "temperature": temp,
            "humidity": humidity,
            "condition": condition
        }
        print("Data added successfully!")

    elif choice == "2":
        city = input("Enter city name to query: ").strip()
        
        if city in weather_data:
            print(f"\nWeather Records for {city}:")
            for date, details in weather_data[city].items():
                print(f"- Date: {date}")
                print(f"  Temperature: {details['temperature']}")
                print(f"  Humidity: {details['humidity']}")
                print(f"  Condition: {details['condition']}")
                print("-" * 20)
        else:
            print("City not found.")

    elif choice == "3":
        city = input("Enter city name: ").strip()
        date = input("Enter date to update: ").strip()

        if city in weather_data and date in weather_data[city]:
            temp = input("Enter new temperature: ").strip()
            humidity = input("Enter new humidity: ").strip()
            condition = input("Enter new condition: ").strip()

            weather_data[city][date] = {
                "temperature": temp,
                "humidity": humidity,
                "condition": condition
            }
            print("Data updated successfully!")
        else:
            print("Record not found.")

    elif choice == "4":
        city = input("Enter city name: ").strip()
        date = input("Enter date to delete: ").strip()

        if city in weather_data and date in weather_data[city]:
            del weather_data[city][date]
            print("Data deleted successfully!")
        else:
            print("Record not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter a number between 1 and 5.")