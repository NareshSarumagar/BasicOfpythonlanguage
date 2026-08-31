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
print(marks[5:])
print(marks[::2])
print(marks[::-1])