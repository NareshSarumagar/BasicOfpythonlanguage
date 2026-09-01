# Unpack a Student Record
# You have a tuple student = ("Amit", 21, "BCA", 8.5) = name, age, course, gpa.
# Unpack it into four variables in one line and print a sentence: "Amit (21) studies
# BCA with GPA 8.5" .
# Uses: tuple unpacking

student = ("Amit", 21, "BCA", 8.5)

name, age, course, score = student

print(name)
print(age,course,score)


# Given nums = [4, 1, 2, 2, 3, 4, 5, 1] , use a set to get only the unique
# numbers, then print how many unique numbers there are.
# Uses: set() + len()

nums = [4,1,2,2,3,4,5,1]

duplicate = list(set(nums))
print(duplicate)

#from sets 
nums = {4,1,2,2,3,4,5,1}
print(nums)
print(len(nums))


# Two people's friend lists: a = {"Ravi", "Sara", "Deep", "Amit"} and b =
# {"Sara", "Amit", "Neha"} . Print their common friends and all friends combined.
# Hint: intersection ( & ) for common, union ( | ) for combined.

a = {"Ravi", "Sara", "Deep", "Amit"}

b = {"Sara", "Amit", "Neha"}

print(a | b)
print(a & b)
print(a-b)
print(a^b)


# Swap Without a Temp Variable
# Take two numbers from the user and swap their values using tuple unpacking (no
# third variable). Print before and after.


to_num = (34,56)

a,b = to_num
print(b,a)


# Who Dropped Out?
# registered = {"A", "B", "C", "D", "E"} signed up, but attended = {"A", "C",
# "E"} showed up. Use set difference to find who did NOT attend.
# Hint: registered - attended


registered = {"A","B","C","D","E"}
attended = {"A","C","E"}

print(registered-attended)


# Unique Words Counter
# Take a sentence from the user. Split it into words and print how many unique
# words it contains (ignore repeats).

sentence = input("Enter your sentence: ")

sentence_split = sentence.split()

print(sentence_split)

print(list(set(sentence_split)))


# Create a list and a set both containing numbers 0 to 999999. Check if 999999 is
# present in each. Using the time module, measure and compare how long each
# lookup takes. Explain the result in a comment.
# Hint: import time , record time.time() before and after each lookup. You'll see the O(1) vs
# O(n) difference for real.

big_list = [1,2,3,...,10000]
big_set = {1,2,3,...,10000}

print(999 in big_list)