class duck:
    def walk(self):
        print("thpak thapaka")
class horse:
    def walk(self):
         print("thpak thapaka")
def myfunction(obj):
    obj.walk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)