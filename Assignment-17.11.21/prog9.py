days=[31,28,31,30,31,30,31,31,30,31,30,31]
noOfdays=0 
m=int(input("Enter month "))
d=int(input("Enter days "))

for i in range(0,m-1):
    noOfdays+=days[i]

print("Number of Days = ",noOfdays+d)