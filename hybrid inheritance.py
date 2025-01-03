class a:
    def __init__(self):
        print("class a")
class b(a):
    def __init__(self):
        super().__init__()
        print("class b")
class c(a):
    def __init__(self):
        super().__init__()
        print("class c")
class d(b,c):
    def __init__(self):
        super().__init__()
        print("class d")
c1=c()