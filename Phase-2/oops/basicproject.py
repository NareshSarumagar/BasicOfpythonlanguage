# B2. Model a Classroom that holds many Student objects (name, marks). Add a method that prints the class topper

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

class Classroom:
    def __init__(self):
        self.students = []
    def add_student(self,student):
         self.students.append(student)
    def print_topper(self):
        if not self.students:
            print("Not Available students.")
            return
        topper = max(self.students, key= lambda student: student.marks)

        print("student Name: ",topper.name)
        print("student marks: ",topper.marks)


s1=Student("naresh", 500)
s2= Student("ramesh",300)
s3=Student("ram",400)
s4=Student("sita",300)
s6=Student("hari",600)

classroom = Classroom()

classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)
classroom.add_student(s4)
classroom.add_student(s6)

classroom.print_topper()


# B3. For the food app, add a show_bill() method to Order that prints each item with its price, then the total at the
# bottom.

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def show_bill(self):
        print("----- FOOD BILL -----")

        total = 0

        for name, price in self.items:
            print(f"{name}: Rs. {price}")
            total += price

        print("---------------------")
        print(f"Total: Rs. {total}")


# Create an order
order = Order()

order.add_item("Burger", 250)
order.add_item("Pizza", 500)
order.add_item("Momo", 180)
order.add_item("coke",200)

order.show_bill()

# M1. Library. Build three classes: Book (title, available), Member (name, borrowed list), and Library (holds books &
# members) with a borrow(member, book) method that checks availability and updates both objects.
# Hint: borrow() reads book.available, sets it False, and appends the book to member.borrowed.
# M2.

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def borrow(self, member, book):
        if book.available:
            book.available = False
            member.borrowed.append(book)

            print(member.name, "borrowed", book.title)
        else:
            print(book.title, "is not available.")

book1 = Book("Python Programming")
book2 = Book("Java Programming")

member1 = Member("Aarati")

library = Library()

library.books.append(book1)
library.books.append(book2)
library.members.append(member1)

library.borrow(member1, book1)


library.borrow(member1, book1)


print("\nBorrowed books by", member1.name)

for book in member1.borrowed:
    print("-", book.title)
