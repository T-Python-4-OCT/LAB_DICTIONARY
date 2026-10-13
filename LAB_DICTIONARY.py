phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
number = input("Enter the phone number: ")

if len(number) != 10 or not number.isdigit():
    print("This is invalid number")
else:
    if number in phone_book:
        print("The owner is : " + phone_book[number])
    else:
        print("Sorry, the number is not found")