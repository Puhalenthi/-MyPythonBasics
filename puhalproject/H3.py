'''Write a program called ‘grader’ that takes in a user’s number grade and
outputs the user’s letter grade. Use the following scale:
a. A = At least 90%
b. B = At least 80% but less than 90%
c. C = At least 70% but less than 80%
d. D = At least 60% but less than 70%
e. F = Less than 60%'''

grader = input("Give me a grade. Don't include the percent sign")
grader = int(grader)

if grader >= 90:
    print("You get an A")
elif 80 <= grader < 90:
    print("You get a B")
elif grader >= 70 and grader < 80:
    print("You get a C")
elif ( grader >= 60 and grader < 70):
    print("You get a D")
elif (grader >= 0 and grader < 60):
    print("You get a F")
else:
    print("ERROR, Try Again")