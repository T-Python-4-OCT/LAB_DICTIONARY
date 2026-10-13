
user_number = input("inter the phone number :")

phone_book = {


       ("0568323222") :"Amal",
   ("0522222232") : "Mohammed",
   ("0532335983") :"Khadijah",
    ("0545341144") :"Abdullah",
      ("0545534556") :"Rawan",
     ("0560664566") : "Faisal",
      ("0567917077") : "Layla"

}

if len(user_number) != 10   :
    print("inviled number")
elif not user_number.isdigit():
    print("must be all numbers")
else :
    print("the owner name :",phone_book.get(user_number,"Sorry, the number is not found"))

     




