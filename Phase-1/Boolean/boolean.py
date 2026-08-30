# Create two numbers and print the result of all six comparison operators ( ==, !=, >, <, >=, <= ) between them.
# B2. Set is_raining = True and has_umbrella = False . Print whether the person will stay dry (they stay dry if it's
# not raining OR they have an umbrella).
# B3. Print whether each of these is truthy or falsy by putting them in an if : 0 , "hi" , [] , None , 42 .


#create two numbers and print the reslut of all six comparison operators(==,!=,>,<,>=<<=) between them.
a=9
b=10 

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# set is_raining=tru and has_umbrella = False. Print whether the person will stay dry (they stay dry if its not raining OR they have an umbralla.)

is_raining = False
has_umbrella = True

is_wheather = is_raining or has_umbrella

if(is_wheather): 
    print("They have an umbrella ")

else:
    print("they stay dry..")

    #Print whether each of these is truthy of falsy by putting them in an if :0 , "hi",[],None,42.

#     values = [0, "hi", [], None, 42]

# for value in values:
#     if value:
#         print(value, "is truthy")
#     else:
#         print(value, "is falsy")



#         M1. A student passes if marks >= 40 and attendance >= 75. Take both as input and print "Pass" or "Fail".
# M2. Write a login check: the user is allowed if the username matches and the password matches. Use and , and print a
# clear message either way.
# M3. Given a variable that could be a name or an empty string, use short-circuit or to print the name, or "Guest" if it's
# empty: print(name or "Guest") . Explain in a comment why this works.
# Hint: or returns the first truthy value.
# I NTERVIEW


student_mark = int(input("Enter Your Mark: "))
attendance = int(input("Enter attendance: "))

if(student_mark >=40 and attendance):
    print("Pass")
else: 
    print("Fail")


#write a login check: the user is allowed if the username matches and the password matches. Use and, and print a clear message either way.

user_name="nareshsarumagar"
pass_word= "naresh@001"

user_name1 = input("Enter your username: ")
pass_word1 = input("Enter your password: ")

is_login = user_name==user_name1 or pass_word==pass_word1
if(is_login): 
    print("Login successfully...")
else: print("Invalid Details..")


# M3. Given a variable that could be a name or an empty string, use short-circuit or to print the name, or "Guest" if it's
# empty: print(name or "Guest") . Explain in a comment why this works.
# Hint: or returns the first truthy value.
# I NTERVIEW

