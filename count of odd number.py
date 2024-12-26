num=int(input("enter a integer"))
odd=0
for i in range(1,num+1):
    if(i%2!=0):
        odd=odd+1
print(odd,"is the count of odd num")