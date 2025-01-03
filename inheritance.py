class vehicle:
    def __init__(self):
        print("hey..! i'm the vehicle class constructor...!")
class bike(vehicle):
    def __init__(self):
        super().__init__()
        print("hey..! i'm the bike class constructor..!")
class superbike(bike):
    def __init__(self):
        super().__init__()
        print("hey..! i'm the super bike class constructor...!")
s1=superbike()