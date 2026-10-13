phone_book = [
    {"name": "Amal","number": "0568323222"},
    {"name": "Moahmmed","number":"0522222232"},
    {"name": "Khadijah","number":"0532335983"},
    {"name": "Abdullah","number":"0545341144"},
    {"name": "Rawan","number":"0545534556"},
    {"name": "Faisal","number":"0560664566"},
    {"name": "Layla","number":"0567917077"}    
     ]
number = input("Enter a phone number: ")

for person in phone_book:
    if person["number"] == number:
        print("Owner:", person["name"])
        break
else:
    print("Number not found")