# Python Basics

# Output
# use print() to write to the screen
print('Hello!') # words go in quotation marks "" or single quotes ' '
# print multiple words, numbers, etc., separate them with commas
print("I am",39,"years old")
# Choose how to separate items, use sep=
print("Hello","Everyone","!",sep="...")
# Choose what happens at the end. use end=
print("Hi","There",sep=" ",end="!!\n")


# Variables
# variables are essentially boxes that hold info. Give it a name, give it a value
name = "Zebarth"
print("Hello", name)

# Each variable name can only be used once.
# We can do math on variables of all types
print(name*3)
name = "Mr. "+name
print(name)

# It is good practice to have all of your variables at the start of your code
# This way you can ensure that every variable is there and ready for you when you need them

# Input
# The user will type information and then hit the enter key. We need to be able to retrieve
# and save this information
# use the input() command
print("Give me your name: ")
name = input()
print("Hello", name)

# We can also use the input command to ask the question
hockeyTeam = input("What's your favourite hockey team?")

# NOTE: Using input only returns information of type "str", or strings.
# Sometimes we will want to have integers or floats (decimal numbers)
# You can convert them as follows
num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
answer = num1/num2
print(answer)

# One other type of data is bool. This is either True or False
checkFlag = False

