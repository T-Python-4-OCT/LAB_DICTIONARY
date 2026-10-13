# Lab

numbers = {
"Amal": "0568323222",
"Mohammed": "0522222232",
"Khadijah": "0532335983",
"Abdullah": "0545341144",
"Rawan": "0545534556",
"Faisal": "0560664566",
"Layla": "0567917077"
}

input_number = input("Enter number phone: ")


if not input_number.isdigit():
     print("This is invalid number")
    
elif len(input_number) != 10:
     print("This is invalid number")
    
else:
    found = False

    for name, number in numbers.items():
     if number == input_number:
        print("The owner:", name)
        found=True
        break
    if not found:
        print("Sorry, the number is not found")



