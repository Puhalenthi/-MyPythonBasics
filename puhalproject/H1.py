'''Write a program called ‘coolfunction’ that takes in a number, and if it’s
even, adds 3 to it, if it’s odd multiply by 4 to it, and then print the resulting
number.
'''


coolfunction = input("Give me a number")
coolfunction = int(coolfunction)

if (coolfunction % 2 == 0):
    coolfunction += 3
    print(coolfunction)
else:
    coolfunction *= 4
    print(coolfunction)