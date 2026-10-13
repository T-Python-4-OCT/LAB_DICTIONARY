phone_book={"0568323222":"Amal",
            "0522222232":"mohamme",
             "0532335983":"Khadijah",
             "0545341144":"Abdullah",
             "0545534556":"Rawan",
             "0560664566":"Faisal",
             "0567917077":"Layla"
}

while True:
    enter_number=input("Enter a phone number : ")
    
    if enter_number in phone_book:
        print(phone_book[enter_number])
        break
    
    elif len(enter_number)!=10 or not enter_number.isdigit:
        print("the number must be digit and 10 numbers")

    else:
        print("the number is not found")
        break
        
    
