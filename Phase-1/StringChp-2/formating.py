#f-strings (formatted string literals) are a way to embed expressions inside string literals, 
# using curly braces {}. They were introduced in Python 3.6 and provide a concise and readable way to format strings.
name = "Rajeev"
score = 95.5
# Basic usage
print(f"Name: {name}") # Name: Rajeev
print(f"Score: {score}") # Score: 95.5
# Expressions inside {}
print(f"2 + 3 = {2 + 3}") # 2 + 3 = 5
print(f"{name.upper()} rocks!") # RAJEEV rocks!
# Number formatting
print(f"{score:.2f}") # 95.50 (2 decimal places)
print(f"{1000000:,}") # 1,000,000 (comma separator)
print(f"{score:.0f}%") # 96% (round to int)
# Multi-line f-string
card = f"""
Student : {name}
Score : {score:.1f}
Grade : {"A" if score >= 90 else "B"}
"""
print(card)

#format() method is a versatile way to format strings in Python. It allows you to insert values into a string using placeholders defined by curly braces {}. The format() method can take positional arguments, keyword arguments, and even perform advanced formatting.
# Basic usage
print("Hello, {}!".format(name)) # Hello, Rajeev!
print("Hello, {0}!".format(name)) # Hello, Rajeev!
print("Hello, {name}!".format(name=name)) # Hello, Rajeev!
# Positional arguments
print("Name: {}, Score: {}".format(name, score)) # Name: Rajeev, Score: 95.5
print("Score: {1}, Name: {0}".format(name, score)) # Score: 95.5, Name: Rajeev
# Keyword arguments
print("Name: {n}, Score: {s}".format(n=name, s=score)) # Name: Rajeev, Score: 95.5
# Advanced formatting
print("Score: {:.2f}".format(score)) # Score: 95.50 (2 decimal places)
print("Score: {:,}".format(1000000)) # Score: 1,000,000 (comma separator)
print("Score: {:>10}".format(score)) # Score:       95.5
print("Score: {:<10}".format(score)) # Score: 95.5


# % operator
print("Name: %s, Score: %.1f" % (name, score)) # Name: Rajeev, Score: 95.5
print("Score: %d" % 1000000) # Score: 1000000
print("Score: %10.2f" % score) # Score:      95.50 (right-aligned, width 10)
print("Score: %-10.2f" % score) # Score: 95.50     (left-aligned, width 10)
print("Score: %010.2f" % score) # Score: 000095.50 (zero-padded, width 10)

#Raw strings are a way to create string literals in Python that treat backslashes (\) as literal characters, rather than as escape characters. This is useful when dealing with file paths, regular expressions, or any other situation where backslashes are common.
# To create a raw string, you prefix the string literal with an 'r' or 'R'. For example:
raw_string = r"C:\Users\Rajeev\Documents\file.txt"


# Normal string — \n becomes a newline, \f becomes form-feed
print("C:\new\folder") # Oops! \n and \f are processed
# Raw string — backslash is just a backslash
print(r"C:\new\folder") # C:\new\folder n
# File paths (Windows)
path = r"C:\Users\Rajeev\Desktop\project"
# Regular expressions (we will cover regex later)
import re
pattern = r"\d+\.\d+" # matches decimals like 3.14
m = re.search(pattern, "Value is 3.14")
print(m.group()) # 3.14



# n Beginner
# Q1. Convert 'pymaster india' to uppercase, then to title case. Print both.
# Q2. Remove spaces from ' clean this ' using strip(). Verify with len().
# Q3. Check if the string '12345' is all digits. Check if 'hello123' is all alpha.
# Q4. Replace 'bad' with 'good' in 'This is bad code with bad habits'.
# Q5. Split 'one:two:three' on ':' and print the resulting list.
# Q6. Join ['Python', 'is', 'fun'] with a space separator.
# Q7. Check if 'Python' starts with 'Py' and ends with 'on'.
# Q8. Print your name right-aligned in a field of width 30 using rjust().
# Q9. Zero-pad the number string '7' to width 4.
# Q10. Use an f-string to display: 'My name is X and my score is Y.2f'


#Q1. Convert 'pymaster india' to uppercase, then to title case. Print both.
str1 = 'pymaster india';
print(str1.upper()) # PYMASTER INDIA
print(str1.title()) # Pymaster India

#Q2. Remove spaces from ' clean this ' using strip(). Verify with len().
str2 = ' clean this '
str2_stripped = str2.strip()
print(str2_stripped) # clean this
print(len(str2_stripped)) # 10

#Q3. Check if the string '12345' is all digits. Check if 'hello123' is all alpha.
str3 = '12345'
str4 = 'hello123'
print(str3.isdigit())
print(str4.isalnum())

#Q4. Replace 'bad' with 'good' in 'This is bad code with bad habits'.
str5 = 'This is bad code with bad habits'
str5_replaced = str5.replace('bad', 'good')
print(str5_replaced) # This is good code with good habits



#Q5. Split 'one:two:three' on ':' and print the resulting list.
str6 = 'one:two:three'
str6_split = str6.split(':')
print(str6_split) # ['one', 'two', 'three']

#Q6. Join ['Python', 'is', 'fun'] with a space separator.
words = ['Python', 'is', 'fun']
join_result = ' '.join(words)
print(join_result) # Python is fun

#Q7. Check if 'Python' starts with 'Py' and ends with 'on'.
str7 = 'Python'
print(str7.startswith('Py')) # True
print(str7.endswith('on')) # True


#Q8. Print your name right-aligned in a field of width 30 using rjust().
name = 'Rajeev'
print(name.rjust(30)) # Right-aligned in a field of width 30
print(name.rjust(30, '.')) # Right-aligned with '.' padding

#Q9. Zero-pad the number string '7' to width 4.
number_str = '7'
print(number_str.zfill(4)) # 0007
print(number_str.zfill(4)) # 0007


#Q10. Use an f-string to display: 'My name is X and my score is Y.2f'
name = 'Rajeev'
score = 95.5
print(f'My name is {name} and my score is {score:.2f}') # My name is Rajeev and my score is 95.50
print(f'My name is {name} and my score is {score:.2f}') # My name is Rajeev and my score is 95.50



# n Intermediate
# Q11. Find the index of 'India' in 'PyMaster India'. Use both find() and index().
# Q12. Count how many times 'an' appears in 'banana'. Count 'a' too.
# Q13. Split the CSV string 'Rajeev,25,Varanasi,Python' into a list and print each value on a new line.
# Q14. Use .format() to display a formatted invoice: Item, Quantity, Price in columns.
# Q15. Strip all '*' characters from '***hello world***' using strip().
# Q16. Check if user input (simulate with a variable) is a valid integer using isdigit().
# Q17. Use swapcase() on 'PyMaster India' and explain what happened.
# Q18. Using only find() (no 'in'), write a function that returns True if substring exists.
# Q19. Split 'a::b::c' on '::' and rejoin with ' | '.
# Q20. Format the number 1234567.89 with commas and 2 decimal places using f-string.

#Q11. Find the index of 'India' in 'PyMaster India'. Use both find() and index().
str8 = 'PyMaster India'
print(str8.find('India')) # 9
print(str8.index('India')) # 9

#Q12. Count how many times 'an' appears in 'banana'. Count 'a' too.
str9 = 'banana'
print(str9.count('an')) # 2
print(str9.count('a')) # 3


#Q13. Split the CSV string 'Rajeev,25,Varanasi,Python' into a list and print each value on a new line.
csv_str = 'Rajeev,25,Varanasi,Python'
csv_list = csv_str.split(',')
for value in csv_list:
    print(value)

#Q14. Use .format() to display a formatted invoice: Item, Quantity, Price in columns.
str10 = "Item: {item}, Quantity: {quantity}, Price: ${price:.2f}"
print(str10.format(item="Apple", quantity=5, price=0.99))
print(str10.format(item="Banana", quantity=10, price=0.59))
print(str10.format(item="Cherry", quantity=20, price=2.49))
print(str10.format(item="Mango", quantity=3, price=1.49))


#Q15. Strip all '*' characters from '***hello world***' using strip().
str11 = '***hello world***'
strip_result = str11.strip('*')
print(strip_result) # hello world

#Q16. Check if user input (simulate with a variable) is a valid integer using isdigit().
user_input = '12345' # Simulating user input
if user_input.isdigit():
    print(f"{user_input} is a valid integer.")


    #Q17. Use swapcase() on 'PyMaster India' and explain what happened.
str12 = 'PyMaster India'
str13 = str12.swapcase()
print(str13) # pYmASTER iNDIA
# The swapcase() method converts all uppercase letters to lowercase and all lowercase letters to uppercase in the string.


#Q18. Using only find() (no 'in'), write a function that returns True if substring exists.
def substring_exists(s, substring):
    return s.find(substring) != -1
print(substring_exists("Hello World", "World")) # True
print(substring_exists("Hello World", "Python")) # False


#Q19. Split 'a::b::c' on '::' and rejoin with ' | '.
str14 = 'a::b::c'
split_list = str14.split('::')
rejoined_str = ' | '.join(split_list)
print(rejoined_str) # a | b | c

#Q20. Format the number 1234567.89 with commas and 2 decimal places using f-string.
number = 1234567.89
formatted_number = f"{number:,.2f}"
print(formatted_number) # 1,234,567.89


# n Think & Apply
# Q21. Write a function that counts the number of vowels in a string using count() for each vowel.
# Q22. Validate that a string is a proper title (each word starts with uppercase) using istitle().
# Q23. Given a path string 'C:\\Users\\Rajeev', how would you store this using a raw string?
# Q24. Write a function that removes all extra spaces from a string (split then join).
# Q25. Given a CSV line of student data, split it and format a readable summary using f-strings.
# Q26. Create a simple Caesar cipher: shift each letter in a word by 1 using ord() and chr().
# Q27. Write a function title_case_words(s) that title-cases only words longer than 3 characters.
# Q28. Given a list of names with inconsistent spacing and casing, normalize each name.
# Q29. Use find() to find ALL occurrences of 'is' in a string (hint: use a loop with start param).
# Q30. Build a simple receipt printer: given items and prices, print a formatted table using ljust/rjust.

#Q21. Write a function that counts the number of vowels in a string using count() for each vowel.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for vowel in vowels:
        count += s.count(vowel)
    return count


    #Q22. Validate that a string is a proper title (each word starts with uppercase) using istitle().
def is_proper_title(s):
    return s.istitle()
print(is_proper_title("This Is A Title")) # True
print(is_proper_title("this is not a title")) # False

#Q23. Given a path string 'C:\\Users\\Rajeev', how would you store this using a raw string?
path = r'C:\Users\Rajeev'
print(path) # C:\Users\Rajeev

#Q24. Write a function that removes all extra spaces from a string (split then join).
def remove_extra_spaces(s):
    return ' '.join(s.split())
print(remove_extra_spaces("  This   is  a   test  ")) # This is a test


#Q25. Given a CSV line of student data, split it and format a readable summary using f-strings.
def format_student_data(csv_line):
    data = csv_line.split(',')
    name, age, city, course = data
    return f"Student Name: {name}\nAge: {age}\nCity: {city}\nCourse: {course}"
print(format_student_data("Rajeev,25,Varanasi,Python"))

#Q26. Create a simple Caesar cipher: shift each letter in a word by 1 using ord() and chr().
def caesar_cipher(word):
    shifted_word = ''
    for char in word:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + 1) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + 1) % 26 + 97)
            shifted_word += shifted_char
            print(f"Original: {char}, Shifted: {shifted_char}")  # Debugging statement
        else:
            shifted_word += char
            print(f"Non-alpha character: {char}, remains unchanged.")  # Debugging statement
    return shifted_word
print(caesar_cipher("Hello, World!")) # Ifmmp, Xpsme!


#Q27. Write a function title_case_words(s) that title-cases only words longer than 3 characters.
def title_case_words(s):
    words = s.split()
    title_cased = [word.title() if len(word) > 3 else word for word in words]
    print(f"Original string: {s}")  # Debugging statement
    print(f"Words after processing: {title_cased}")  # Debugging statement
    return ' '.join(title_cased)
print(title_case_words("this is a test of the title case function")) # this is a Test of the Title Case Function


#Q28. Given a list of names with inconsistent spacing and casing, normalize each name.
def normalize_names(names):
    normalized = []
    for name in names:
        normalized_name = ' '.join(name.split()).title()
        normalized.append(normalized_name)
        print(f"Original: '{name}', Normalized: '{normalized_name}'")  # Debugging statement
    return normalized

print(normalize_names(["  rajeev  ", "RAJEEV", "raJeev"])) # ['Rajeev', 'Rajeev', 'Rajeev']

#Q29. Use find() to find ALL occurrences of 'is' in a string (hint: use a loop with start param).
def find_all_occurrences(s, substring):
    occurrences = []
    start = 0
    while True:
        index = s.find(substring, start)
        if index == -1:
            break
        occurrences.append(index)
        start = index + 1
    return occurrences 

print(find_all_occurrences("This is a test. This is only a test.", "is")) # [2, 5, 22, 25]

#Q30. Build a simple receipt printer: given items and prices, print a formatted table using ljust/rjust.
def print_receipt(items):
    print("Item".ljust(20) + "Price".rjust(10))
    print("-" * 30)
    for item, price in items:
        print(item.ljust(20) + f"${price:.2f}".rjust(10))
    total = sum(price for _, price in items)
    print("-" * 30)
    print("Total".ljust(20) + f"${total:.2f}".rjust(10))

    print_receipt([("Apple", 0.99), ("Banana", 0.59), ("Cherry", 2.49), ("Mango", 1.49)])