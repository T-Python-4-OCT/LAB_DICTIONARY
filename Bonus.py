CONDITIONS = {"sunny", "rainy", "cloudy", "windy", "snowy"}

def is_number(text):
    return text.replace("-", "", 1).replace(".", "", 1).isdigit()

def is_valid_date(date):
    parts = date.split("-")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return False
    year, month, day = parts
    return len(year) == 4 and len(month) == 2 and len(day) == 2 \
        and 1 <= int(month) <= 12 and 1 <= int(day) <= 31

def validate(city, date, temperature, humidity, condition):
    if city == "":
        return "City name cannot be empty."
    if not is_valid_date(date):
        return "Date must look like 2025-10-13."
    if not is_number(temperature):
        return "Temperature must be a number."
    if not (humidity.isdigit() and 0 <= int(humidity) <= 100):
        return "Humidity must be a whole number from 0 to 100."
    if condition not in CONDITIONS:
        return "Condition must be one of: " + ", ".join(sorted(CONDITIONS))
    return None

def add_weather(data, city, date, temperature, humidity, condition):
    error = validate(city, date, temperature, humidity, condition)
    if error:
        return error
    if city not in data:
        data[city] = {}                        
    data[city][date] = {
        "temperature": float(temperature),
        "humidity": int(humidity),
        "condition": condition,
    }
    return None

def query_city(data, city):

    return data.get(city)

def show_city(data, city):
    records = query_city(data, city)
    if records is None:
        print(f"No data for {city}.")
        return
    print(f"Weather data for {city}:")
    for date, info in sorted(records.items()):
        print(f"  {date}: {info['temperature']} C, {info['humidity']}% humidity, {info['condition']}")


def update_weather(data, city, date, temperature, humidity, condition):
    if city not in data or date not in data[city]:
        return "No such record to update."
    return add_weather(data, city, date, temperature, humidity, condition)

def delete_weather(data, city, date):
    if city not in data or date not in data[city]:
        return "No such record to delete."
    del data[city][date]
    if not data[city]:                         
        del data[city]
    return None

def main():
    data = {}
    print("=" * 40)
    print("    Welcome to the Weather System      ")
    print("=" * 40)
    
    while True:

        print("\n--- Main Menu ---")
        print("1. Add weather data")
        print("2. Search for a city")
        print("3. Update weather data")
        print("4. Delete weather data")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "5":
            print("Goodbye!")
            break
            
        if choice not in ("1", "2", "3", "4"):
            print("Error: Please choose a valid option (1-5).")
            continue
            
        city = input("City: ").strip().title()
        
        if choice == "2":
            show_city(data, city)
            continue
            
        date = input("Date (YYYY-MM-DD): ").strip()
        
        if choice == "4":
            error = delete_weather(data, city, date)
        elif choice in ("1", "3"):
            temperature = input("Temperature (C): ").strip()
            humidity = input("Humidity (%): ").strip()
            condition = input("Condition (sunny, rainy, cloudy, windy, snowy): ").strip().lower()
            
            if choice == "1":
                error = add_weather(data, city, date, temperature, humidity, condition)
            else:
                error = update_weather(data, city, date, temperature, humidity, condition)
                
        print(error if error else "Done.")

main()