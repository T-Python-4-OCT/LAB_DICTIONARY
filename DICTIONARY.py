phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}


user_number = input("Enter your number: ")


if not user_number.isdigit() or len(user_number) != 10:
    print("This is invalid number")


elif user_number in phone_book:
    print(phone_book[user_number])


else:
    print("Sorry, the number is not found")