year=int(input("enter a year:"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is a leap year")
        else:
            print("not leap year")
    else:
         print("it is a leap year") 
else:
    print("this is not a leap year")               