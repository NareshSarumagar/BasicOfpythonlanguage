# Problem 1 – FizzBuzz
# Difficulty: Easy
# Print numbers from 1 to 100. Print Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if
# divisible by both, otherwise print the number.
# Uses: Loop, if-elif-else, % operator.

# for i in range(1,101):
#     if i%3 == 0:
#         print("Fizz")

#     if i%5 == 0:
#         print("Buzz")

#     if i%3 and i%5 == 0:
#         print("FizzBuzz")
#     print(i)

#     Find the sum and average of a list without using sum() or statistics.mean().
# Uses: Lists, Loop, Variables.

num = [4,5,6,2,3,7]
sum = 0

for i in num[::]:
    sum += i
print(sum)
avg = sum/2
print(avg)

# Difficulty: Medium
# Find the largest element in a list without using max().
# Uses: Lists, Loop, if.

nums = [30,20,35,10,50,60,45,55,32]
large = nums[0]

for i in nums:
    if i>large:
        large = i
print(large)


# Difficulty: Medium
# Check whether a given number is Prime or Not Prime.
# Uses: Loop, if, % operator.

nume = int(input("Enter a number: "))

if nume <=1:
    print("not prime")
else:
    is_prime = True

    for i in range(2,nume):
        if nume%i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime")
    else:
        print("Not prime")

