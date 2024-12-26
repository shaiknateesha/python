n=int(input("enter the integer:"))
sum_of=0
while(n!=0):
    rem=n%10
    sum_of+=rem
    n//=10
print("sum of digits is:",sum_of)    