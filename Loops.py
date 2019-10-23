# Loops
# Repeat code using a condition (while loop)
password = ""
while password != "Irish":
    password = input("Enter your password: ")
# any of the conditions in the "conditionals.py" file will work here


# Repeat code over a range (for loop)
# We can repeat starting at 0, stopping before a value                  range(5)
# We can repeat starting at a value, stopping before a separate value   range(3,8)
# We can repeat starting at a value, stopping before a separate value, increasing by a set amount   range(2,20,3)
total = 0
for counter in range(3, 8):
    total = total + counter
    print(total)

# Repeat over the parts of a collection, example, the letters in a string
counter = 1
for letter in password:
    print("letter #", counter, letter)
    counter += 1
