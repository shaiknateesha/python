class Student:
    def __init__(self):
        print("object is created")
        self.name="choti"
        self.age=20
std1=Student()
print("student name:",std1.name)
print("student age:",std1.age)
print("__________________")
std2=Student()
print("student name:",std2.name)
print("student age:",std2.age)