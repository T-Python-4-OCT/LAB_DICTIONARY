phone_book = {"Amal":"0568323222",
"Mohammed":"0522222232",
"Khadijah":"0532335983",
"Abdullah":"0545341144",
"Rawan"	:"0545534556",
"Faisal":"0560664566",
"Layla":"0567917077"
}
def check (phone_book):
    phone = input("Enter the phone number: ")

    if len(phone) != 10 or not phone.isdigit():
        print("invalid number")
    else:
        for name, number in phone_book.items():
            if number == phone:
                print(name)
                break
        else:
            print("the number is not found")

check(phone_book)




