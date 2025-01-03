class duck:
    def walk(self):
        print("thpak thapaka")
class horse:
    def walk(self):
         print("thpak thapaka")
class cat:
    def walk(self):
        print("meow meow")
def myfunction(obj):
    if hasattr(obj,'walk'):
         obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)
c=cat()
myfunction(c)