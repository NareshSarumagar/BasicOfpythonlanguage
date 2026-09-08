# Given items = [10, 20, 30] , ask the user for an index and print that item. Catch
# IndexError and print "No item there" if the index is out of range.
# Hint: except IndexError .

try:
    items = [10,20,30]
    index = int(input("Enter an index:"))
    print(items[index])
except IndexError:
    print("No item there")


# Given a phone book dict, ask for a name and print the number. Catch KeyError
# and print "Name not found" . (Compare with using .get() from #14.)
# Hint: except KeyError .

try:
    dict = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-555-5555"}
    name = input("Enter a name: ")
    print("Phone number:", dict[name])
except KeyError:
    print("Name not found")

# Using a while loop with try/except, keep asking the user for a number until they
# enter a valid one, then print it. Invalid input should re-prompt, not crash.
# Hint: loop, try the conversion, break on success, except to re-prompt.

while True:
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Validate with raise
# Write a function set_age(age) that raise s a ValueError if the age is negative
# or over 150, otherwise returns it. Call it inside a try/except and print the caught
# message.
# Hint: raise ValueError("...") inside the function.

def set_age(age):
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                raise ValueError("Age must be between 0 and 150.")
            return age
        except ValueError as e:
            print("Error:", e)
            print("Please enter a valid age.")


try:
    user_age = set_age(0)  # The argument is not used; input is taken inside the function
    print("Your age is:", user_age)
except ValueError as e:
        print("Caught an error:",e)


# Loop over pairs [(10, 2), (5, 0), (9, 3)] . For each, try to divide and print the
# result in an else block, catch ZeroDivisionError in except , and print "---" in
# finally after each pair.
# Hint: use all of try/except/else/finally together.

pairs = [(10, 2), (5, 0), (9, 3)]

i = 0
while i < len(pairs):
    try:
        num1, num2 = pairs[i]
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result of {num1} / {num2} is: {result}")
    finally:
        print("---")
    i += 1

#interview question: What will the following code print?

    def f():
        try:
            return "runs"
        finally:
            print("cleanup")


print(f())

# Custom Exception Bank
# Create a custom exception InsufficientBalance . Write a withdraw(balance,
# amount) function that raises it when the amount exceeds the balance. Test both a
# successful and a failing withdrawal with try/except.
# Tests: defining and raising a custom exception (Section 6).

class InsufficientBalance(Exception):
    pass

balance = 0  # Initialize balance to 0

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalance("Insufficient balance for this withdrawal.")
    return balance - amount

while balance == 0:
    try:
        balance = float(input("Enter your current balance: "))
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
    except ValueError as e:
        print("Error:", e)
        balance = 0  # Reset balance to 0 to re-prompt

try:
    amount = float(input("Enter the amount to withdraw: "))
    new_balance = withdraw(balance, amount)
    print(f"Withdrawal successful. New balance: {new_balance}")
except InsufficientBalance as e:
    print("Error:", e)