# Greet with a Default
# Write a function greet(name, msg="welcome") that prints a greeting. Call it once
# with just a name, and once with both a name and a custom message.
# Uses: def + default arguments


def greet(name, msg = "welcome"):
    print(name, " ",msg)

greet("naresh")


# Rectangle Area
# Write a function area(length, width) that returns the area (not prints). Call it,
# store the result in a variable, and print it.
# Uses: return value  

def area (length, width): 
    return length * width

print("The area is: ",area(3,4))


# Write a function is_even(n) that returns True if n is even, else False . Test it
# with a few numbers.
# Hint: return n % 2 == 0

def is_even(n):
    return n%2==0
print(is_even(6))

# Simple Interest
# Write a function interest(principal, rate, years) that returns the simple
# interest ( P * R * T / 100 ). Give rate a default of 5. Call it once using the
# default and once overriding it.
# Hint: return the formula; use a default argument for rate.

def interest(principal, years, rate =5):
    i = principal*rate*years/100
    print("interest is: ",i)


interest(30000,2)

# Greatest of Three
# Write a function biggest(a, b, c) that returns the largest of three numbers —
# without using max() .

def biggest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else: 
       return c 

print(biggest(10,5,30))


# Write a function grade(marks) that returns "A", "B", "C", or "Fail" based on the
# marks (your own cutoffs). Test it with a few values.
# Hint: if/elif inside the function, then return the grade string.

def grade(marks):
    if marks >=90 and marks <=100:
        print("Grade A",marks)
    elif marks >=80 and marks <=90:
         print("Grade B",marks)
    elif marks >=70 and marks <=80:
         print("Grade C",marks)
    else: 
         print("Fail.",marks)

print(grade(85))

# Temperature Converter
# Write a function convert(temp, to="F") . If to is "F" it returns
# Celsius→Fahrenheit; if "C" it returns Fahrenheit→Celsius. Use a default argument
# and return the result. Test both directions.
# Hint: C→F is temp * 9/5 + 32 ; F→C is (temp - 32) * 5/9 . Use if/else on to .

def convert(temp, to="F"):
    if temp >=100:
        F = (temp-32)*5/9
        return F 
    else:
        C = temp*9/5+32
        return C
print(convert(90))