

try:
    age = int(input("Please enter your age: "))
    print("Next age:",age+1)
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")