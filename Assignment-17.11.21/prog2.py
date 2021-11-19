temp=[] 
print("enter 7 temperatures : ")
for i in range (0,7):
    temp.append(int(input()))
print("Average temperature is : ",sum(temp)/len(temp))