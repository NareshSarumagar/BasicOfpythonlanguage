class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Resturant:
    def __init__(self,name):
        self.name = name
        self.menu = []

    def add_dish(self,item):
        self.menu.append(item)

    def show_menu(self):
        for item in self.menu:
            print(f"{item.name}-${item.price}")

class Order:
    def __init__(self,custumer):
        self.custumer = custumer
        self.items = []
    def add_item(self,item):
        self.items.append(item)
        print(f"Added: {item.name}")
    def total(self):
        return sum(item.price for item in self.items)


pizza = MenuItem("Pizza",350)
coke = MenuItem("coke",200)

r1 = Resturant("Burger House")
r1.add_dish(pizza)
r1.add_dish(coke)

o1 = Order("naresh")
o1.add_item(r1.menu[0])
o1.add_item(r1.menu[1])


print(f"total: ${o1.total()} - custumer name: {o1.custumer}")
