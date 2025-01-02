class mobile:
    def __init__(self):
        self.model = ' realme'
    def show_model(self):
        print(self.model)
realme=mobile()
realme.show_model()
r=realme.show_model
print("outside class:",r)