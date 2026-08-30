# Homework (post answers in comments):
# • Print the sum of numbers from 1 to 100 using a loop.
# • Print only even numbers from 1 to 20 using continue.
# • Take a number and check if it is prime, using a loop with break.


# Print the sum of numbers from 1 to 100 using a loop.

sum = 0
for i in range(1,101):
    sum += i

print(sum)

# print only even numbers from 1 to 20 using continue.
for i in range(1,20):
    if i%2 ==0: 
        print(i)

print("\n")

# Take a number and check if it is prime, using a loop with break.

for num in range(2,21):
    is_prime = True

    for i in range(2,num):
        if num%i ==0:
            is_prime = False
            break;
    if is_prime: 
        print(num)