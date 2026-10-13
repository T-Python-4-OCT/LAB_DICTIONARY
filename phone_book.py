phone_book = {
    "0536791777":"Morad",
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla",
}

number = input("Enter the phone number: ").strip()
if not number.isdigit() or len(number) != 10:
    print("This is invalid number")
elif number in phone_book:
    print(phone_book[number])
else:
    print("Sorry, the number is not found")
