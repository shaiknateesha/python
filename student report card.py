studentname=input("enter the student name:")
sub1=int(input("enter the sub1 marks:"))
sub2=int(input("enter the sub2 marks:"))
sub3=int(input("enter the sub3 marks:"))
total=0
average=0
print("student report:")
print("------------------")
print("student name:",studentname)
print("subject1:",sub1)
print("subject2:",sub2)
print("subject3:",sub3)
if(sub1>=35 and sub2>=35 and sub3>=35):
    total=sub1+sub2+sub3
    print("total:",total)
    average=total/3
    print("average:",average)
    if(average>=90):
        print("congrats you have qualifed 1 st class...!")
    elif(average>=75):
        print("congrats you have qualifed 2 nd class...!")
    else:
        print("congrats you have qualifed 3 rd class...!")
else:
    print("better luck next time")