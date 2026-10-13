phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

phone_number = input("Enter phone number: ")

if len(phone_number) != 10 or not phone_number.isdigit():
    print("This is invalid number")
else:
    found = False

    for name, number in phone_book.items():
        if number == phone_number:
            print(name)
            found = True
            break

    if not found:
        print("Sorry, the number is not found")



