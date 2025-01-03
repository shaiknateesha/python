class Student:
    @staticmethod
    def collegename():
        print("ABC college name---!")
    @classmethod
    def writeexams(self):
        print("enjoy exams......!")
    def show_name(self):
        return self.studentname
    def set_name(self):
        self.studentname="choti"
    def __init__(self,studentname,id ,email):
        print("object created------")
        self.studentname=studentname
        self.id=id
        self.email=email
Student.collegename()
Student.writeexams()
stu=Student("choti",1,"choti@email.com")
print(stu.show_name())