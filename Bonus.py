weather_data = {}

def add_weather():
    city = input("Enter city name: ").strip().capitalize()
    date = input("Enter date (e.g., YYYY-MM-DD): ").strip()
    temp = input("Enter temperature: ").strip()
    humidity = input("Enter humidity (e.g., 40%): ").strip()
    condition = input("Enter weather condition (e.g., sunny, rainy): ").strip()

   
    weather_data[city] = {
        "date": date,
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }
    print(f"\n[+] Weather data for {city} added successfully!\n")



def query_weather():
    city = input("Enter city name to search: ").strip().capitalize()
    
    if city in weather_data:
        print(f"\n--- Weather Report for {city} ---")
        details = weather_data[city]
        print(f"Date      : {details['date']}")
        print(f"Temp      : {details['temp']}°C")
        print(f"Humidity  : {details['humidity']}")
        print(f"Condition : {details['condition']}")
        print("-" * 30 + "\n")
    else:
        print(f"\n[-] Sorry, no weather data found for '{city}'.\n")



def update_or_delete():
    city = input("Enter city name to update or delete: ").strip().capitalize()
    
    if city not in weather_data:
        print(f"\n[-] City '{city}' not found in records.\n")
        return

    action = input("Do you want to (update) or (delete) this data? ").strip().lower()
    
    if action == "delete":
        del weather_data[city]
        print(f"\n[+] Weather data for {city} has been deleted.\n")
        
    elif action == "update":
        print(f"Updating data for {city}:")
        date = input("Enter new date: ").strip()
        temp = input("Enter new temperature: ").strip()
        humidity = input("Enter new humidity: ").strip()
        condition = input("Enter new weather condition: ").strip()
        
        weather_data[city] = {
            "date": date,
            "temp": temp,
            "humidity": humidity,
            "condition": condition
        }
        print(f"\n[+] Weather data for {city} updated successfully!\n")
    else:
        print("\n[-] Invalid choice.\n")



def main():
    while True:
        print("=== Weather Data System ===")
        print("1. Add Weather Data")
        print("2. Query Weather by City")
        print("3. Update or Delete Weather Data (Challenge)")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_weather()
        elif choice == "2":
            query_weather()
        elif choice == "3":
            update_or_delete()
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[-] Invalid choice, please choose between 1 and 4.\n")


if __name__ == "__main__":
    main()