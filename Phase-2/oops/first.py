'''So far you have written code as a sequence of instructions and functions that pass data around. Object-Oriented Programming
(OOP) is a different way of organizing code: you bundle data and the functions that work on that data together into a single unit
called an object .
Think of a real-world thing — a car. A car has data (color, speed, fuel) and can do things (start, accelerate, brake). OOP lets you model
that same idea in code.
Class — the blueprint (e.g. the design of a car).
Object — a real thing built from the blueprint (e.g. your actual red car).
Why care? OOP makes big programs easier to organize, reuse, and maintain. Almost every real library you will use — Django,
pandas, tkinter — is built with classes.'''


#Creating a Class & Making Objects

class Dog:
    pass         # an empty class for now

# Creating (instantiating) objects
d1 = Dog()
d2 = Dog()

print(type(d1))    #<class '__main.py__'
print(d1==d2)      #false - two separate objects

#3. __init__ Constructor 
'''An empty dog is useless. We want each dog to have its own name and breed. That is what __init__ does — it runs automatically
the moment an object is created, and sets up its starting data.'''

class Dog:
  def __init__(self, name, breed):
       self.name = name # instance attribute
       self.breed = breed


d1 = Dog("Bruno", "Labrador")
d2 = Dog("Rocky", "Beagle")
print(d1.name)
print(d1.breed) # Bruno
print(d2.breed) # Beagle

#Instance Attributes vs Class Attributes

'''Instance attributes are unique to each object (set with self. inside __init__). Class attributes are shared by all objects of the
class (defined directly in the class body).'''

class Dog:
    species = "canis species" #class attributes

    def __init__(self,name):
        self.name = name  #instance attributes

dog = Dog("Brounoo")

print(dog.name)
print(dog.species)

#Methods — Instance, Class & Static

'''A method is just a function that lives inside a class. There are three kinds.'''

class Circle:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
        # 1) instance method — uses self / object data
    def area(self):
        return Circle.pi * self.radius ** 2
        # 2) class method — uses cls, works on the class
    @classmethod
    def unit_circle(cls):
        return cls(1)
        # 3) static method — no self, no cls; just a helper
    @staticmethod
    def describe():
        return "A circle is a round shape."
c = Circle(5)
print(c.area()) # 78.53975
print(Circle.unit_circle().radius) # 1
print(Circle.describe())

#Real-World Example: Bank Account Class

'''Let us tie everything together — instance attributes, class attributes, and methods — in a realistic BankAccount class.'''

class BankAccount:
    bank_name = "naresh_saru"

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <=0:
           return print("Ammount must be negative.")
        self.balance +=amount
        print(f"Deposited {amount}. Balance: {self.balance}")


    def withdraww(self, amount):
        if amount > self.balance:
            return print("Insuficeint balance.")
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

acc = BankAccount("naresh",2000)
acc.deposit(2000)
print(acc.deposit(1000))
print(acc.withdraww(500))
print(acc.bank_name)

#Practice Basic

'''B1. Make a Car class with attributes brand and speed. Add a method show() that prints them nicely.'''

class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        return f"Brand is {self.brand} and speed is{self.speed}"

c1 = Car("toyataaa", 3000)
print(c1.show())

'''M2. Create a Temperature class storing celsius. Add a @staticmethod called c_to_f(c) that converts Celsius to
Fahrenheit, and an instance method fahrenheit() that uses it.'''


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

    def fahrenheit(self):
        return Temperature.c_to_f(self.celsius)

temp = Temperature(30)
print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit())

'''M3. Build a Playlist class holding a list of songs. Add add_song(), remove_song(), and total() methods.'''

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def total(self):
        return self.songs


# playlist
playlist = Playlist()

# Add songs
playlist.add_song("Perfect")
playlist.add_song("Shape of You")
playlist.add_song("Believer")
playlist.add_song("Move on")
playlist.add_song("The amazing spider man.")
# Remove
playlist.remove_song("Believer")

# Display
print("Total songs:", playlist.total())