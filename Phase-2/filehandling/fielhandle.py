
# f = open(r"C:\Users\A plus\OneDrive\ドキュメント\Naresh Saru Magar.txt")
# data = f.read()
# print(data)
# f.close()

with open("notes.txt", "w") as f:
    f.write("This is a sample note.\n")
    f.write("You can write multiple lines.\n")
    f.write("Make sure to close the file or use 'with' statement.\n")

with open("notes.txt", "a") as f:
    f.write("This line is appended to the file.\n")
    f.write("Appending allows you to add content without overwriting.\n")

'''Create a new file "practice.txt" using python.
add the following data in it.
Hi everyoue
we are learning File I/O
Using Java.
I like programming in Java.'''

with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning File I/O\n")
    f.write("Using Java.\n")
    f.write("I like programming in Java.\n")

'''WAF that replace all occurences of "java" with "python " in about file.'''
with open("practice.txt", "r") as f:
    content = f.read()

    updated_content = content.replace("Java", "python")
    print(updated_content)

'''search if the word "learning" exixts in the file or not.'''
with open("practice.txt", "r") as f:
    content = f.read()
    if("learning" in content):
        print("The word 'learning' exists in the file.")
    else:
        print("The word 'learning' does not exist in the file.")


'''WAF find in which line of the file does the word "learning'occur first.
print-1 if word not found '''


def check_content():
    content = "learning"
    with open("practice.txt", 'r') as f:
        learn = f.read()
        if(content in learn ):
            print("Found")
        else:
            print("not found.")

check_content()

'''from a file containing nubers separedted by comma, print the count of even numbers.'''

with open("even.txt", 'r')as f:
    r_num = f.read()

    num = r_num.split(",")
    count = 0

    for i in num:
        if int(i)%2 == 0:
            count +=1
        print(i)