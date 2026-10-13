phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0504509545": "Saleh"
       
}
number = input("Enter phone number:")

if len(number) != 10:
    print("This is Invalid number")

elif not number.isdigit():
    print("This is invalid number")

elif number in phone_book:
    print(phone_book[number])

else:
    print("Sorry, the number is not found")
