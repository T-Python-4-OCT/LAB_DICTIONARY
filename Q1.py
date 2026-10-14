phone_book = {
"Amal": "0568323222",
 "Mohammed": "0522222232",
  "Khadijah": "0532335983",
  "Abdullah": "0545341144",
   "Rawan": "0545534556",
    "Faisal": "0560664566",
     "Layla": "0567917077"}

while True:
    number = input("Enter a number to search for a name (or type 'exit' to quit): ")
    if number.lower() == 'exit':
        break
    elif not number.isdigit() or len(number) != 10:
        print("Please enter a valid 10-digit number.")
        continue
    else:
        for name, phone in phone_book.items():
            if phone == number:
                print(f"The name associated with the number {number} is: {name}")
                break
        else:
            print(f"No name found for the number {number}.")