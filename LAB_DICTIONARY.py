phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla",
}

user_input = input("Please enter a phone number: ")

if not user_input.isdigit():
  print("This is invalid number")
elif len(user_input) != 10:
  print("This is invalid number")
else:
  owner = phone_book.get(user_input)
  if owner:
    print(owner)
  else:
    print("Sorry, the number is not found")