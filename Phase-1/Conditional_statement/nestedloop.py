# Solve in Video
# S1. Print a 5×5 square using *.
# S2. Print:
# 1
# 12
# 123
# 1234
# 12345
# Basic
# B1. Print numbers 1–5 using nested loops.
# B2. Print a 4×6 rectangle of stars.
# B3. Print multiplication tables from 1–5.
# Moderate
# M1. Diamond-like half pattern.
# M2. Floyd's Triangle.
# M3. Print A, AB, ABC, ABCD, ABCDE.
# Break & Continue
# BC1. Stop at 13 while printing 1–20.
# BC2. Skip multiples of 3 from 1–20.
# BC3. Print a 5×5 grid skipping the centre.
# Challenge
# C1. 1 / 22 / 333 / 4444 / 55555
# C2. Right aligned star triangle.
# C3. Multiplication tables 1–10.
# C4. Print all prime numbers from 1–100 using nested loops.


#  print a 5*5 square using *.

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

#      S2. Print:
# # 1
# # 12
# # 123
# # 1234
# # 12345

for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()


#B1. Print numbers 1–5 using nested loops.

for i in range(1,6): 
    for j in range(1,6):
        print(j, end=" ")
    print()

# for i in range(1,6): 
#     for j in range(i,6):                      
#         print(j, end=" ")
#     print()

# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5 

# Print the reactangle 4*6 of stars 

for i in range(1,7):
    for j in range(4):
        print("*", end=" ")
    print()