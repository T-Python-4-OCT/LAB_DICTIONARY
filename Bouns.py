weather_data = {
    "Riyadh": {"2026-10-13": {"temp": 38, "humidity": 12, "condition": "dusty"}},
    "Jeddah": {"2026-10-13": {"temp": 35, "humidity": 58, "condition": "humid"}},
    "Abha": {"2026-10-13": {"temp": 22, "humidity": 55, "condition": "rainy"}},
}

#تقرا الحرارة والرطوبه
def read_details():
    """Read temperature, humidity and condition. Return a dictionary, or None if invalid."""
    temp = input("Temperature: ").strip()
    humidity = input("Humidity: ").strip()
    condition = input("Condition: ").strip().lower()

    if temp.isdigit() and humidity.isdigit() and int(humidity) <= 100 and condition.isalpha():
        return {"temp": int(temp), "humidity": int(humidity), "condition": condition}
    print("Invalid input")
    return None

#تضيف طقس وتسال عن مدينه وتاريخ وتحفظ
def add_weather():
    city = input("City: ").strip().title()
    date = input("Date (YYYY-MM-DD): ").strip()
    if not (city.replace(" ", "").isalpha() and len(date) == 10):
        print("Invalid city or date")
        return

    details = read_details()
    if details:
        if city not in weather_data:
            weather_data[city] = {}
        weather_data[city][date] = details
        print("Saved")

#تعرض كل سجلات الطقس المحفوظة لمدينة معينه
def query_city():
    city = input("City: ").strip().title()
    if not weather_data.get(city):
        print("No data found")
        return
    for date, info in weather_data[city].items():
        print(date, "|", info["temp"], "C |", info["humidity"], "% |", info["condition"])

#تعدل سجلات المينه و التاريخ
def update_weather():
    city = input("City: ").strip().title()
    date = input("Date (YYYY-MM-DD): ").strip()
    if city not in weather_data or date not in weather_data[city]:
        print("Not found")
        return

    details = read_details()
    if details:
        weather_data[city][date].update(details)
        print("Updated")

#تحذف سجلات 
def delete_weather():
    city = input("City: ").strip().title()
    date = input("Date (YYYY-MM-DD): ").strip()
    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        print("Deleted")
    else:
        print("Not found")

#هنا تشغيل وعرض خيارات الدالة المناسبة
while True:
    print("\n1) Add  2) Query  3) Update  4) Delete  5) Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_weather()
    elif choice == "2":
        query_city()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        break
    else:
        print("Invalid choice")


#MohammedAlnsafi        