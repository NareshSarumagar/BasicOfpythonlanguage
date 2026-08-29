#Q1. Try s[0]='X' on any string. Observe and explain the error you get.

s = "Hello"
s[0] = 'X'  # This will raise a TypeError because strings in Python are immutable, 
# meaning that their contents cannot be changed after they are created.

#TypeError: 'str' object does not support item assignment


#Q2. write a print statement that outputs. He said "Hello" (include the Quotes in the output)

str1 = '"Hello"';
print(str1);

#Q3. Print a Windows file path: C:\Users\Name\Documents\file.txt using escape characters.
print("C:\\Users\\Name\\Documents\\file.txt")

#Q4.what does s[1:-1] do? Test it on at least three different strings.
str1 = "Python"
print(str1[1:-1])  # Output: ytho
str2 = 'DataScience'
print(str2[1:-1])  # Output: ataScience
str3 = '''Hello World'''
print(str3[1:-1])  # Output: ello World


#Q5 con you find a slice expression that returns an empty string from 'PYTHON'? Find two different ways.

str1 = "PYTHON"
slice1 = str1[0:0]  # This will return an empty string
str2 = str1[6:6]  # This will also return an empty string
print("Slice expression 1 returns: '", slice1, "'")

str3 = ""
slice2 = str1[0:0]  # This will also return an empty string
print("Slice expression 2 returns: '", slice2, "'");
