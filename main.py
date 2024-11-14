# homework17

print("Is the 4-digit number even and not end with a 0? ")

x=int(input("Give me an integer number:"))

if x<10000 and x>=1000:

    if not x%10==0:
    
        if x%2==0:
            print("It is good because it's even.")
        
        else:
            print("It is bad because it's not even.")
    
    else:
        print("It is bad because it ends with 0.")

else:
    print("It is bad because it's not 4 digits.")


quit()
