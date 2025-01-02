class Student:
    def __init__(self,name,age):
        print("object is created")
        self.name=name
        self.age=age
std1=Student("chotu",20)
print("student name:",std1.name)
print("student age:",std1.age)
print("__________________")
std2=Student("choti",21)
print("student name:",std2.name)
print("student age:",std2.age)