'''Create a program called ‘vowel’ that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a
message indicating that the entered letter is a vowel. If the user enters y
then your program should display a message indicating that sometimes y
is a vowel, and sometimes y is a consonant. Otherwise, your program
should display a message indicating that the letter is a consonant.'''


letter = input("Give me a letter")
letter = letter.lower()
if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
    print("This is a vowel")
elif (letter == 'y'):
    print("This is sometimes a vowel and sometimes a consonant")
else:
    print("This is a consonant")
