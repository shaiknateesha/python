num=int(input("enter thr integer value:"))
digitcount=0
while(num!=0):
    num=num//10
    digitcount=digitcount+1
print(digitcount,"digits")