num=int(input("enter a integer"))
evensum=0
oddsum=0
for i in range(1,num+1):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("even sum:",evensum)
print("odd sum:",oddsum)
