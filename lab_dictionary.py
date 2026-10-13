contacts = [
    {"Name": "Amal", "Number": "0568323222"},
    {"Name": "Mohammed", "Number": "0522222232"},
    {"Name": "Khadijah", "Number": "0532335983"},
    {"Name": "Abdullah", "Number": "0545341144"},
    {"Name": "Rawan", "Number": "0545534556"},
    {"Name": "Faisal", "Number": "0560664566"},
    {"Name": "Layla", "Number": "0567917077"}
]

numbar = input("Enter the number: ")

if not numbar.isdigit():
    print("This is an incorrect number")

elif len(numbar) != 10:
    print("This is an invalid number")

else:
    found = False

    for name in contacts:
        if name["Number"] == numbar:
            print(name["Name"])
            found = True
            break

    if not found:
        print("Sorry, number not found")