# Student Profile CRUD
# Create a dict student with name and age . Then: add a course key, update the
# age, safely read a missing email key with .get() , and delete the course. Print
# the dict after each step.
# Uses: add, update, get, delete

dic1 = {
    "name":"ram",
    "age":"23"
}

print(dic1.get("name"))

dic1["emial"] = "xxxttaction@gmail.com"

dic1["age"] = 24

dic1["name"] = "hari"
print(dic1.get("age"))

del dic1["age"]
# age = dic1.pop("email")
# print(age)
print(dic1)


# Build a phone book dict with 3 name → number entries. Ask the user for a name
# and print the number using .get() so a missing name prints "Not found"
# instead of crashing.
# Hint: book.get(name, "Not found")


phone_book = {
    "peace": "4567",
    "booked": "4568",
    "hashed": "4569"
}

book = input("enter your book name: ")

print(phone_book.get(book, "Not found"))

# Given prices = {"pen": 10, "book": 50, "bag": 200} , loop over it with
# .items() and print each line as "pen costs 10" .
# Uses: .items() looping
    
prices = {"pen":10,"book":50, "bag":200}

for key, value in prices.items():
    print(key, "costs",value)


# Total & Highest
# Given marks = {"math": 90, "sci": 85, "eng": 78} , use looping to print the
# total marks and the subject with the highest marks.
# Hint: loop .values() for the total; loop .items() tracking the best (pattern from #11.2).

marks = {"math":90, "sci":85,"eng":78}
total = 0
for value in marks.values():
    total += value
print(total)

highest = 0
highest_subject = ""

for subject, mark in marks.items():
    if mark > highest: 
        highest = mark
        highest_subject = highest
print(highest_subject)


# Create a nested dict of 3 students, each with name and gpa . Loop over it and
# print each student's name and gpa. Then print the name of the student with the
# highest gpa.
# Hint: nested dict + .items() + best-so-far trackin

std = {
    "s1":{"name": "Ram", "gpa": 7.8},
    "s2":{"name": "Hari", "gpa": 8.0},
    "s3":{"name": "onedrive", "gpa": 8.8}
}

highest = 0
high = ""
for sid,info in std.items():
    print(sid,"->",info["name"],"->",info["gpa"])
    if info["gpa"] > highest : 
        highest = info["gpa"]
        high = highest
print(high)


# Count Letters with defaultdict
# Take a word from the user. Use defaultdict(int) to count how many times each
# letter appears, and print the result.
# Hint: counts = defaultdict(int) , then counts[ch] += 1 .
from collections import defaultdict
count = defaultdict(int)
user_word = input("enter user word: ")
for ch in user_word:
    count[ch] +=1
print(dict(count))

# Word Frequency with Counter
# Take a sentence from the user. Split it into words and use Counter to find the 3
# most common words. Print them with their counts.
# Hint: Counter(sentence.split()).most_common(3)
from collections import Counter
sent = input("enter a sentence from user: ")

count = Counter(sent)
print(count)

most_comm = Counter(sent).most_common(3)
print(most_comm)
print(sent.split())
print(set(sent))