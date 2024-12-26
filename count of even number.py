num=int(input("enter a integer"))
evensum=0
for i in range(1,num+1):
    if(i%2==0):
        evensum=evensum+1
print("even sum:",evensum)