n=input("enter the number")
print(n)
list1=list(n)
list2=list1[::-1]
res=""
for i in list2:
    res=res+i
print(res)