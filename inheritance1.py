class engineer:
    def __init__(self):
        print(" i'm the engineer class constructor...!")
e1=engineer()
print("-------------------------")
class softwareengineer(engineer):
    def __init__(self):
        super().__init__()
        print("hey..! i'm the software engineer class constructor..!")
s1=softwareengineer()
print("-------------------------------")
class civilengineer(engineer):
    def __init__(self):
        super().__init__()
        print("hey..! i'm the software engineer class constructor...")
c1=civilengineer()
print("-----------------------------------------")
class mechanicalengineer(engineer):
    def __init__(self):
        super().__init__()
        print("i'm mechanical engineer class constructor.....!")
m1=mechanicalengineer()
