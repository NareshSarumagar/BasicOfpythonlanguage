#case methods #upper(), #lower(), #title(), #capitalize(), #swapcase()
#what is the difference between funtion() and mthod() in python
#function is a block of code that is defined using the def keyword and can be called independently, it is also called independent entity.
# while a method is a function that is associated with an object and is called on that object.

str1 = "hello world"
print("Original string: ", str1)
print("Uppercase: ", str1.upper())
print("Lowercase: ", str1.lower())

str2 = "python programming"
print("Original string: ", str2)
print("Title Case: ", str2.title())

str3 = "i love python programming language"
print("Original string: ", str3)
print("Capitalized: ", str3.capitalize())
print("Swapcase: ", str3.swapcase())

#strip methods #strip(), #lstrip(), #rstrip()
str4 = "   hello world   "
print("Original string with spaces: '", str4, "'")
print("Stripped string: '", str4.strip(), "'")  

str5 = "Hello world  "
print("Original string with trailing spaces: '", str5, "'")
print("Left stripped string: '", str5.lstrip(), "'")
print("Right stripped string: '", str5.rstrip(), "'")

str6 ="***Hello World***"
print("Original string with prefix and suffix: '", str6, "'")
print("Stripped string: '", str6.strip('*'), "'")

str7 = "###Hello World###"
print("Original string with prefix and suffix: '", str7, "'")
print("Left stripped string: '", str7.lstrip('#'), "'")


s = "Python is fun and Python is powerful"
# find() — index of first match, returns -1 if not found
print(s.find("Python")) # 0
print(s.find("Python", 5)) # 18 ¬ search from index 5 onward
print(s.find("Java")) # -1 ¬ not found, NO error
# index() — same as find() but raises ValueError if not found
print(s.index("is")) # 7
# s.index("Java") # n ValueError: substring not found
# count() — how many times does substring appear?
print(s.count("Python")) # 2
print(s.count("is")) # 2
print("banana".count("an")) # 2


#Replace, slipt, join methods
str8 = "I love Python programming"
str9 = str8.replace("Python", "Java")
print("Original string: ", str8)
print("Replaced string: ", str9)
str_2 = str8.replace("love", "enjoy",2)
print("Original string: ", str8)
print("Replaced string with count: ", str_2)
str10 = "apple,banana,cherry"
str11 = str10.split(",")
print("Original string: ", str10)
print("Split string: ", str11)

#slipt() method with maxsplit parameter
# Default split — splits on ANY whitespace
s = " one two three "
print(s.split()) # ['one', 'two', 'three'] — also strips spaces!
# Split on specific separator
s2 = "one,two,three,four"
print(s2.split(',')) # ['one', 'two', 'three', 'four']
# Limit splits with maxsplit
print(s2.split(',', 2)) # ['one', 'two', 'three,four']
# Split a sentence into words
sentence = "Python is awesome"
words = sentence.split() # ['Python', 'is', 'awesome']


# join is the INVERSE of split
words = ['Python', 'is', 'awesome']
print(' '.join(words)) # Python is awesome
print('-'.join(words)) # Python-is-awesome
print(''.join(words)) # Pythonisawesome
# Common pattern: split ® process ® join
s = 'one two three'
words = s.split()
upper_words = [w.upper() for w in words] # (we will cover this later!)
result = ' '.join(upper_words)
print(result) # ONE TWO THREE

#check methods #isalnum(), #isalpha(), #isdigit(), #isspace(), #istitle(), #isupper(), #islower(), #startswith(), #endswith()
print("hello123".isalnum()) # True — all alphanumeric?
print("hello".isalpha()) # True — all letters?
print("12345".isdigit()) # True — all digits?
print(" ".isspace()) # True — all whitespace?
print("Hello World".istitle())# True — title case?
print("HELLO".isupper()) # True — all uppercase?
print("hello".islower()) # True — all lowercase?
# startswith / endswith
print("Python".startswith("Py")) # True
print("Python".endswith("on")) # True
print("Python".startswith(("Py","Go"))) # True ¬ accepts a tuple!


s = "Python"
print(s.center(20)) # " Python "
print(s.center(20, "-")) # "-------Python-------"
print(s.ljust(20, ".")) # "Python.............."
print(s.rjust(20, ".")) # "..............Python"
# zfill — zero-pad number strings
print("42".zfill(5)) # "00042"
print("7".zfill(4)) # "0007"
# Real use — printing formatted table
for item, price in [("Apple",12),("Mango",25),("Banana",8)]:
    print(item.ljust(10), str(price).rjust(5))
# Apple 12
# Mango 25
# Banana