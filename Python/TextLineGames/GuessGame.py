import random
def guessgame(num, num2):
    answer = random.randint(num, num2)
    guessesleft = 5
    while guessesleft >= 1:
        guessesleft -= 1
        guess = int(input('Give me a number between {} and {}'.format(num, num2)))
        if guess == answer:
            print('Congrats, you have guessed the right answer')
        elif guess < answer:
            print('The answer is greater than {}. You have {} guesses left.'.format(guess, guessesleft))
            if guessesleft == 0:
                print('Nice try. The answer was {}'.format(answer))
        else:
            print('The answer is less that {}. You have {} guesses left '.format(guess, guessesleft))
            if guessesleft == 0:
                print('Nice try. The answer was {}'.format(answer))




print(guessgame(1, 100))