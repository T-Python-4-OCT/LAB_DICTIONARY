
# lab dictionary

phone_number = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

number = input("Enter the phone number: ")

if not number.isdigit():
    print("This is invalid number")
elif len(number) != 10:
    print("This is invalid number")
elif number in phone_number:
    print(phone_number[number])
else:
    print("Sorry, the number is not found")


    #output

# Enter a phone number: 0568323222
#  Amal

# Enter a phone number: 0552160081
# Sorry, the number is not found 

# Enter a phone number: 056832322 
# This is invalid number

# Enter a phone number: faris
# This is invalid number

# Enter a phone number: faris511
# This is invalid number

