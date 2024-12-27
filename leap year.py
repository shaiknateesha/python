y=int(input("enter the year:"))
if((y%4==0)and((y%100!=0)or(y%400==0))):
     print(y,"leap year")
else:
     print(y,"not a leap year")
