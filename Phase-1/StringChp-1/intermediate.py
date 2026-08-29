#Q1.Check whether 'Python' is present in the string 'I love Python programming'.
str0 = "Python";
str1 = "I love Python programming"
str2 = str0 not in str1
print("Is 'Python' present in the str1? ",str2)

#Q2.Concatenate 'Hello' and 'World' with a space in between and print it.
str3 = "Hello"
str4 = "World"
str5 = str3 + " " + str4
print("Concatenated string is: ",str5)

#Q3. Repeat '*' 20 times to print a separator line.
str6 = "*"
str7 = str6 * 20
print("Separator line is: ",str7)

#Q4. Extract every alternate character from 'ABCDEFGHIJ' and print it.
str8 = "ABCDEFGHIJ"
str9 = str8[::2]    
print("Alternate characters from the string are: ",str9)

#Q5.From 'Pymater India', extract 'India' using slicing and print it.
str10 = "Pymater India"
str11 = str10[8:13:1]
print("Extracted substring is: ",str11)