y=int(input("enter the year"))

if(y%400==0):
    print("Leap Year")
else:
    if(y%100==0):
        print("NOT leap year")
    else:
        if(y%4==0):
            print("Leap year")
        else:
            print("NOT leap year")
