
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
user_number = input("Please enter the phone number: ")

if not user_number.isdigit():
    print("This is invalid number")
elif len(user_number) != 10:
    print("This is invalid number")
else:
    owner = phone_book.get(user_number)
    
    if owner:
        print(f"The owner's name is: {owner}")
    else:
        print("Sorry, the number is not found")