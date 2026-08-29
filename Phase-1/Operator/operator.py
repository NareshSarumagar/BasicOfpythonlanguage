#integer have no limit store the data 
import math

a = 10 
b = 20.4578

print(a + b)
print(type(a + b))

 #arthemetic operator 

print(20+30+50) #addition
print(50-20) #subtraction
print(2*5) #multiple
print(40/10) #division 

print(2*5+10**2) #expotential 

#user input 
# The input() function lets your program take data from the user. It always returns a string, even if the
# user types a number.
#user input have already in the form of string that should be change in integer... 

a = int(input("enter the value of a: "))
b = float(input("enter the value of b: "))

c = a+b;
print(c)


#Let's build your first interactive program! This calculator takes two numbers from the user and shows
#all arithmetic operations.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#arthematic operations
print("Addition a+b: ", a + b)
print("Subtraction a-b: ", a - b)
print("Multiplication a*b: ", a * b)
print("Division a/b: ", a / b)
print("Modulus a%b: ", a % b)
print("Exponentiation a**b: ", a ** b)

print(math.isclose(0.1+0.2, 0.3))