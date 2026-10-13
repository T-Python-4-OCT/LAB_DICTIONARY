'''' Phone Book Search and validate phone numbers'''



phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0542630900": "Layla"
    }

print("Phone Book 📞")
number = input ("Enter phone number:" ) 
if not number.isdigit() or len(number)!=10:
    print("This is invalid nuber ❌")
else:
 if number in phone_book:
   print("Owner✅:",phone_book[number])
 else:
    print("Sorry, the number is not found ❌")
    