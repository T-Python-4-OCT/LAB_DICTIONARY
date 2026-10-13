
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
input_number = input("Please enter a phone number: ")
if input_number in phone_book:
    print(f"The number {input_number} belongs to {phone_book[input_number]}.")
elif len(input_number) != 10:
    print("The number is invalid.")
elif input_number.isdigit() == False:
    print("The number is invalid.")
elif input_number not in phone_book:
    print("Sorry, the number is not found. ")

