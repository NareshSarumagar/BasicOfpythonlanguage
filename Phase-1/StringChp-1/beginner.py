#Begineer Section
#Q1. Crete a string with your name. Print its length and data type.
name = "naresh saru magar";

print("Length of my name is: ",len(name))
print("Data type of my name is: ",type(name));

#Q2. print the first and last character of the string 'DataScience'
str1 = "DataScience"
str2 = str1[0];
str3 = str1[-1];
print("First character of the string is: ",str2)
print("Last character of the string is: ",str3)


#Q3 using negative indexing. Print the 3rd character from the end of 'PyMaster'
pystr = "PyMaster"

pychar = pystr[-3]
print("3rd character from the end of the string is: ",pychar);

#Q4. slice 'PROGRAMMING' to extract only 'GRAM'
progstr = "PROGRAMMING"
progslice = progstr[3:7]
print("Sliced string is: ",progslice)

#Q5. Rerse the string 'India' using slicing and print it.
indstr = "India"
indrev = indstr[::-1]
print("Reversed string is: ",indrev)