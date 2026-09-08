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

