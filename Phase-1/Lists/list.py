# PROBLEM 1
# Create & Access
# Create a list of your 5 favourite programming languages. Print the first and the
# last one using both positive and negative indexing.


name_pro = ["java","python","c#","c++","javascript"]

print(name_pro[0])
print(name_pro[-1])

# PROBLEM 2
# Slice the Marks
# Given marks = [45, 67, 89, 23, 90, 56, 78] :
# Print the first 3 marks
# Print the last 2 marks
# Print every alternate mark
# Print the list in reverse


marks = [45,67,89,23,90,56,78]
print(marks[:3])
for mark in marks[:3]:
    print(mark)
print(marks[5:])
for mark in marks[5:]:
    print(mark)
print(marks[::2])
for mark in marks[::2]:
    print(mark)
print(marks[::-1])
for mark in marks[::-1]:
    print(mark)


#     PROBLEM 3
# Todo List Manager
# Start with todos = ["wake up", "study"] . Then:
# Add "exercise" at the end
# Add "meditate" at the very beginning
# Remove "study"
# Replace the last item with "sleep"
# Print the final list

todos = ["wake up", "study"]
todos.append("exercise")
print(todos)
for i in todos[::]:
    print(i)

todos.insert(0,"meditate")
print(todos)

todos.remove("study")
print(todos)

todos[2] = "sleep"
print(todos)

# PROBLEM 4
# Student Record (Nested)
# Create a nested list where each inner list is [name, marks] for 3 students. Print
# the name of the 2nd student and the marks of the 3rd student.

sdt_record = [
    ["ram",45],
    ["Hari",50],
    ["Sita",90]
]

print(sdt_record[1])
print(sdt_record[2])

# Unpack the Coordinates
# You have data = [101, "Varanasi", 25.3, 82.9] = id, city, lat, lon. Unpack it
# into four named variables in a single line and print a sentence using them.

data = [101,"varanasi", 25.3, 82.9]

a,b,c,d = data
print(a,b,c,d)
print(a)


# The Copy Trap
# Create original = [1, 2, 3] . Make a copy called backup . Append 99 to
# backup . Print both lists and explain (in a comment) why original did NOT
# change. Then deliberately create the bug using = and observe the difference.

original = [1,2,3]
backup = original.copy()

backup.append(99)

print("original",original)
print("backup",backup)

# Mini Leaderboard
# Given scores = [40, 80, 65, 95, 70] , without using sort() yet — find the
# highest and lowest using slicing tricks after you learn them, OR rearrange
# manually using index assignment. Print "Winner is at position X". (We'll improve
# this in a later video.)

scores = [40,80,65,95,70]

print(scores[::3])