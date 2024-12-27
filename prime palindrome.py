n=int(input("enter the number:"))
rem=0
reversed_num=0
num=n
while(n!=0):
    rem=n%10
    reversed_num=reversed_num*10+rem
    n//=10
if(reversed_num==num):
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not a palindrome")
            break
    else:
        print(num,"is a prime palindrome")
else:
    print(num,"is not a palindrome or prime")