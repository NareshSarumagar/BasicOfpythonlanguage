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
Biryani = MenuItem("Biryani",400)
chatpat = MenuItem("chatpat",100)

r1 = Resturant("Burger House")
r1.add_dish(pizza)
r1.add_dish(coke)
r1.add_dish(chatpat)

o1 = Order("naresh")
o1.add_item(r1.menu[0])
o1.add_item(r1.menu[1])
o1.add_item(r1.menu[2])

o2 = Order("ramesh")
o2.add_item(r1.menu[2])

print(f"total: ${o1.total()} - custumer name: {o1.custumer}")
print(f"total: {o2.total()}->custumer name: {o2.custumer}")


'''B1. Model a Playlist that holds many Song objects (title, duration). Add add_song() and a total_duration()
method.'''

class song:
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)

    def total_duration(self):
        total = 0
        for song in self.songs:
            total +=song.duration
        return total

s1 = song("Believer", 4.50)
s2 = song("Passenger", 3.55)
s3 = song("A list of the guys", 4.00)
s4 = song("The dead", 3.44)

playlist = Playlist()

playlist.add_song(s1)
playlist.add_song(s3)
playlist.add_song(s3)
playlist.add_song(s4)

print(f"total playlist duration: {playlist.total_duration()} minutes")