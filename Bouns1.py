weather = {
    "Riyadh":{"2026-10-13": {"Temperature": 30.0,"Humidity": 40.0,"Condition": "Sunny"}},
            "Madine": {"2026-10-13": {"Temperature": 30.0,"Humidity": 40.0,"Condition": "Sunny"}}}


def sersh():
    user = input("Enter the city: ")

    if user in weather:
        print(weather[user])
    else:
        print("City is not found")


def insert1():
    city = input("Enter the city name: ")
    date = input("Enter the date (YYYY-MM-DD): ")

    if city == "" or date == "":
        print("City and date cannot be empty")
        return

    if city in weather and date in weather[city]:
        print("Date already exists for this city")
        return

    try:
        degree = float(input("Enter the temperature: "))
        humidity = float(input("Enter the humidity: "))

    except ValueError:
        print("Please enter valid numbers")
        return

    if not 0 <= humidity <= 100:
        print("Humidity must be between 0 and 100")
        return

    condition = input("Enter the condition (Sunny, Rainy, Cloudy): ")

    if condition not in ["Sunny", "Rainy", "Cloudy"]:
        print("Invalid weather condition")
        return

    if city not in weather:
        weather[city] = {}

    weather[city][date] = {
        "Temperature": degree,
        "Humidity": humidity,
        "Condition": condition
    }

    print("Weather added successfully!")
    print(weather)


def update():
    upname = input("Enter the city name: ")
    update1 = input("Enter the date (YYYY-MM-DD): ")

    if upname not in weather:
        print("City not found")
        return

    if update1 not in weather[upname]:
        print("Date not found")
        return

    try:
        upTemperature = float(input("Enter the new temperature: "))
        upHumidity = float(input("Enter the new humidity: "))

    except ValueError:
        print("Please enter valid numbers")
        return

    if not 0 <= upHumidity <= 100:
        print("Humidity must be between 0 and 100")
        return

    upCondition = input("Enter the new condition (Sunny, Rainy, Cloudy): ")

    if upCondition not in ["Sunny", "Rainy", "Cloudy"]:
        print("Invalid weather condition")
        return

    weather[upname][update1].update({
        "Temperature": upTemperature,
        "Humidity": upHumidity,
        "Condition": upCondition
    })

    print("Weather updated successfully!")
    print(weather)

def delete():
    deletN = input("Enter the city name: ")
    deletdete = input("Enter the date (YYYY-MM-DD): ")

    if deletN in weather and deletdete in weather[deletN]:
        weather[deletN].pop(deletdete)

        if not weather[deletN]:
            weather.pop(deletN)

        print("Weather deleted successfully!")
        print(weather)
    else:
        print("City or date not found")
while True:
    print("1. Add Weather")
    print("2. Update Weather")
    print("3. Delete Weather")
    print("4. Search Weather")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        insert1()
    elif choice == "2":
        update()
    elif choice == "3":
        delete()
    elif choice == "4":
        sersh()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
