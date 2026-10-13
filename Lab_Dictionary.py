name = {
      "Amal":"0568323222",
      "Mohammed":"0522222232",
      "Khadijah":"0532335983",
      "Abdullah":"0545341144",
      "Rawan":"0545534556",
      "Faisal":"0560664566",
      "Layla":"0567917077"
}
phone=input("Enter the phone number: ")
if not phone.isdigit() or len(phone) != 10:
    print("This is invalid number")

elif phone in name.values():
    for owner, number in name.items():
         if number == phone: 
            print("The owner of this number is", owner)

else:
        print("Sorry, the number is not found")