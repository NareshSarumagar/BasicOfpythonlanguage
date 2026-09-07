

try:
    age = int(input("Please enter your age: "))
    print("Next age:",age+1)
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")


    #zerodividionError

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.",e)

    #catching multiple exceptions

try:
    nums = [10,20]
    i = int(input("Enter an index: "))
    print(100/nums[i])
except ValueError: 
    print("an value error occured")
except IndexError as e:
    print("Error: Index is out of bounds.",e)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#catching several exception in a single 
def risky():
    nums = [10, 20]
    i = int(input("Enter an index: "))
    print(100 / nums[i])
try:
    risky()
except (ValueError, TypeError, IndexError, ZeroDivisionError) as e:
    print("An error occurred:", e)


#else block with try except
try:
    num = [10,20,30]
    i = int(input("enter an index:"))
    print(30/num[i])
except ValueError as e:
    print("Error: Index is out of bounds.", e)
except IndexError as e:
        print("Error: Index is out of bounds.",e)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.",e)
else:
    print("You entered a valid index:",i)
finally:
    print("checking is completed...")

#raise — Triggering Your Own Errors

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Age is valid.")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)

except ValueError as e:
    print("Error:", e)


#custion exception 

class InsufficientBalance(Exception):
 pass
def withdraw(balance, amount):
 if amount > balance:
  raise InsufficientBalance("Not enough money!")
 return balance - amount
try:
 withdraw(100, 500)
except InsufficientBalance as e:
 print("Error:", e) #