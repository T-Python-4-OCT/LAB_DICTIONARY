weather_data = {}

def check_number(text):
    '''Checks if the input is a number'''
    text = text.strip()
    if text.startswith("-"):
        text = text[1:]
    if text.count(".") > 1:
        return False
    return text.replace(".", "").isdecimal()


def check_date(text):
    '''Checks if the date is valid'''
    parts = text.split("-")
    if len(parts) != 3:
        return False

    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if not (year.isdecimal() and month.isdecimal() and day.isdecimal()):
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29  # leap year

    return 1 <= day <= days_in_month[month - 1]


def read_weather():
    '''Gets weather details'''
    while True:
        temperature = input("Enter the temperature 🌡️. (or back) : ").strip()
        if temperature ==("back"):
            return
        if check_number(temperature):
            temperature = float(temperature)
            break
        print("the temperature must be a number")

    
    while True:
        humidity = input("Enter humidity (0-100)💧. (or back) : ").strip()
        if humidity == ("back"):
            return
        if not check_number(humidity):
            print("the humidity must be a number")
        elif not 0 <= float(humidity) <= 100:
            print("the humidity must be between 0 and 100")
        else:
            humidity = float(humidity)
            break

    
    while True:
        condition = input("Enter the wather condation (sunny, rainy, cloudy, windy)🌤️  (or back):").strip().lower()
        if condition == ("back"):
            return
        if condition.isalpha():
            break
        print("the condition must be letters only")

    return {"temperature": temperature, "humidity": humidity, "condition": condition}


def add_weather():
    '''Adds weather data'''
    while True:
        city = input("Type the city name🏙️  (or back):  ").strip().lower()
        if city == "back":
            return
        if city .replace(" ", "").isalpha():
            break
        print("City name should contain letters")

    
    while True:
        date = input("Enter date (YYYY-MM-DD)📅 (or back): ").strip()
        if date =="back":
            return
        
        if check_date(date):
            break
        print("Please enter the date as YYYY-MM-DD")

   
    details = read_weather()

   
    if city  not in weather_data:
        weather_data[city] = {}

    weather_data[city ][date] = details
    print(" Weather record added successfully!✅")


def search_city():
    '''Shows weather data for a city'''
    city_name = input("Type a city : ").strip().lower()
    if city_name not in weather_data:
        print("No records found")
        return

    print("\nRecords for:", city_name)
    for date in weather_data[city_name]:
        info = weather_data[city_name][date]
        print(f"{date} - Temp: {info['temperature']}°C - Moisture: {info['humidity']}% - Weather: {info['condition']}")


def update_weather():
    '''Updates weather data'''
    city_name = input("enter the city name : ").strip().lower()
    date = input("Enter date (YYYY-MM-DD)   : ").strip()

    if city_name in weather_data and date in weather_data[city_name]:
        print("enter the new data")
        weather_data[city_name][date] = read_weather()
        print("data updated")
    else:
        print("this city or date is not found")


def remove_weather():
    '''Deletes weather data'''
    city_name = input("enter the city name : ").strip().lower()
    date = input("Enter date (YYYY-MM-DD) : ").strip()

    if city_name in weather_data and date in weather_data[city_name]:
        del weather_data[city_name][date]
        if len(weather_data[city_name]) == 0:  
            del weather_data[city_name]
        print("data deleted")
    else:
        print("this city or date is not found")


while True:
    print("\n🌤️  Weather Manager")
    print("1️⃣  Add new record")
    print("2️⃣  View city records")
    print("3️⃣  Edit a record")
    print("4️⃣  Remove a record")
    print("5️⃣  Close program")

    choice = input("Select an option : ")

    if choice == "1":
        add_weather()
    elif choice == "2":
        search_city()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        remove_weather()
    elif choice == "5":
        print("Goodbye👋✨ ")
        break
    else:
        print("invalid choice, choose from 1 to 5")





