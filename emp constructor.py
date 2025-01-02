class Emp:
    def __init__(self,empname,empid,empdesi,empsal,emploc,empsplalow):
        print("object created")
        self.empname=empname
        self.empid=empid
        self.empdesi=empdesi
        self.empsal=empsal
        self.emploc=emploc
        self.empsplalow=empsplalow
emp1=Emp("chotu",1,"manager",3500,"gudivada","car")
print("employee name:",emp1.empname)
print("employee id:",emp1.empid)
print("employee designation:",emp1.empdesi)
print("employee salary:",emp1.empsal)
print("employee location:",emp1.emploc)
print("employee special allowances:",emp1.empsplalow)
print("-----------------------------------------")
emp2=Emp("choti",2,"office",5500,"eluru","car")
print("employee name:",emp2.empname)
print("employee id:",emp2.empid)
print("employee designation:",emp2.empdesi)
print("employee salary:",emp2.empsal)
print("employee location:",emp2.emploc)
print("employee special allowances:",emp2.empsplalow)
print("-----------------------------------")
emp3=Emp("hibbu",3,"hr",6000,"juction","bike")
print("employee name:",emp3.empname)
print("employee id:",emp3.empid)
print("employee designation:",emp3.empdesi)
print("employee salary:",emp3.empsal)
print("employee location:",emp3.emploc)
print("employee special allowances:",emp3.empsplalow)
