# Conditionals
# We want to be able to make decisions based on our variables
# We use the "if" statment with a condition to check for a result
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is the same as", num2)

# You can have as many "elif" statements as you want. Each one must have a different condition
# The "else" statement always goes last. This is run if none of the other conditions are met.

# We can also use this with words and letters
password = input("Enter the password: ")
realPassword = "Pa$$w0rd"
if password == realPassword:
    print("You got it!")
else:
    print("Wrong password")

# Possible comparisons
# == equal
# != not equal
# > greater than
# < less than
# >= greater than equal
# <= less than equal
# and   combine two conditions
# or    one or the other condition
