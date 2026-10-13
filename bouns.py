weather_data = {}

def is_number(text):
   
    text = text.strip()
    if text.startswith("-"):
        text = text[1:]
    if text.count(".") > 1:
        return False
    return text.replace(".", "").isdecimal()


def is_valid_date(text):
 
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


def get_weather_values():
    
    while True:
        temperature = input("Enter the temperature : ").strip()
        if is_number(temperature):
            temperature = float(temperature)
            break
        print("the temperature must be a number")

    
    while True:
        humidity = input("Enter humidity (0-100) : ").strip()
        if not is_number(humidity):
            print("the humidity must be a number")
        elif not 0 <= float(humidity) <= 100:
            print("the humidity must be between 0 and 100")
        else:
            humidity = float(humidity)
            break

    
    while True:
        wather_condtion = input("Enter the wather condation (sunny, rainy, cloudy, windy) : ").strip().lower()
        if wather_condtion.isalpha():
            break
        print("the condition must be letters only")

    return {"temperature": temperature, "humidity": humidity, "condition": wather_condtion}


def information_wather():
   
    while True:
        city_name = input("enter the city name : ").strip().lower()
        if city_name.replace(" ", "").isalpha():
            break
        print("the city name must contain letters only")

    
    while True:
        dtae = input("Enter date (YYYY-MM-DD) : ").strip()
        if is_valid_date(dtae):
            break
        print("the date must be like this 2026-10-13")

   
    details = get_weather_values()

   
    if city_name not in weather_data:
        weather_data[city_name] = {}

    weather_data[city_name][dtae] = details
    print("data saved")


def query_by_city():
    city_name = input("enter the city name : ").strip().lower()

    if city_name not in weather_data:
        print("no data for this city")
        return

    print("\nweather data for", city_name)
    for date in weather_data[city_name]:
        info = weather_data[city_name][date]
        print(date, "| temperature:", info["temperature"], "| humidity:", info["humidity"], "| condition:", info["condition"])


def update_weather():
    city_name = input("enter the city name : ").strip().lower()
    date = input("Enter date (YYYY-MM-DD) : ").strip()

    if city_name in weather_data and date in weather_data[city_name]:
        print("enter the new data")
        weather_data[city_name][date] = get_weather_values()
        print("data updated")
    else:
        print("this city or date is not found")


def delete_weather():
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
    print("\n1. Add weather data")
    print("2. Query by city")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Exit")

    choice = input("Choose a number : ")

    if choice == "1":
        information_wather()
    elif choice == "2":
        query_by_city()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("invalid choice, choose from 1 to 5")