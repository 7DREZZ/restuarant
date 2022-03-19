class Restaurant:

    def __init__(self):
        self.name = "Zdes edyat" 
        self.type = "russian"

    def describe_restuarant(self):
        print("Name:", self.name)
        print("Cuisine type:", self.type)
    
    def open_restuarant(self):
        print("Ресторан открыт") 
a = Restaurant()
print(a.name)
print(a.type)
a.describe_restuarant()
a.open_restuarant()   



