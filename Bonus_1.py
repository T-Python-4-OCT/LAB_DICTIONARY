
def input_weather(data):
    city = input("Enter city name: ").strip().capitalize()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    
    temp_input = input("Enter temperature (°C): ").strip()
    if not temp_input.lstrip('-').isdigit():
        print("Invalid temperature! Please enter a valid number.")
        return
    temperature = float(temp_input)
    
    hum_input = input("Enter humidity (%): ").strip()
    if not hum_input.isdigit():
        print("Invalid humidity! Please enter a valid number.")
        return
    humidity = int(hum_input)
    
    condition = input("Enter weather condition (e.g., sunny, rainy): ").strip().lower()
    
    if city not in data:
        data[city] = {}
        
    data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
    print(f"Weather data for {city} on {date} added successfully!\n")

def query_by_city(data):
    city = input("Enter the city name to query: ").strip().capitalize()
    
    if city in data:
        print(f"\n--- Weather Data for {city} ---")
        for date, details in data[city].items():
            print(f"Date: {date}")
            print(f"  - Temperature: {details['temperature']}°C")
            print(f"  - Humidity: {details['humidity']}%")
            print(f"  - Condition: {details['condition']}")
        print("-" * 30)
    else:
        print(f"Sorry, no weather data found for '{city}'.\n")

def update_or_delete_weather(data):
    city = input("Enter city name for update/delete: ").strip().capitalize()
    
    if city not in data:
        print(f"City '{city}' not found in the database.\n")
        return
        
    date = input("Enter date (YYYY-MM-DD): ").strip()
    
    if date not in data[city]:
        print(f"No records found for {city} on {date}.\n")
        return
        
    action = input("Do you want to (U)pdate or (D)elete this record? ").strip().upper()
    
    if action == 'U':
        print("Enter new details:")
        temp_input = input("Enter new temperature: ").strip()
        hum_input = input("Enter new humidity: ").strip()
        condition = input("Enter new condition: ").strip().lower()
        
        if temp_input.lstrip('-').isdigit() and hum_input.isdigit():
            data[city][date]["temperature"] = float(temp_input)
            data[city][date]["humidity"] = int(hum_input)
            if condition:
                data[city][date]["condition"] = condition
            print("Record updated successfully!\n")
        else:
            print("Invalid numeric values entered. Update failed.\n")
            
    elif action == 'D':
        del data[city][date]
        print(f"Record for {city} on {date} has been deleted.\n")
        if not data[city]:
            del data[city]
    else:
        print("Invalid choice.\n")

def main():
    weather_database = {}
    
    while True:
        print("\n=== Weather Data Aggregation System ===")
        print("1. Add Weather Data")
        print("2. Query Weather by City")
        print("3. Update or Delete Weather Record ")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            input_weather(weather_database)
        elif choice == '2':
            query_by_city(weather_database)
        elif choice == '3':
            update_or_delete_weather(weather_database)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
