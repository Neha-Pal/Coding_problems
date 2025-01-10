year = int(input("Enter year - "))

if year % 4 == 0:
    if year % 100 == 0:
        if year & 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")    