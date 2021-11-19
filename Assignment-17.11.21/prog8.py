n=int(input("Enter 3 digit number "))
d=0
while(n>0):
    d=d*10 + n%10
    n=n//10

print("reversed Digit : ",d)