# Create a file mymath.py with two functions: add(a, b) and is_prime(n) . In a
# second file main.py , import them and use both. (Prime logic is from #11.2.)
# Hint: from mymath import add, is_prime — keep both files in the same folder.

def add(a,b):
    sum = a+b
    print(sum)

add(4,5)

def is_prime(n):
    if n<=1:
        return False
    for i in (2,n):
        n%i==0
        return True

print(is_prime(7))