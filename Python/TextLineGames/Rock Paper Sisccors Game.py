import random
choices = ['rock', 'paper', 'scissors']

def rockpaperscissorsgame():
    play = True
    userpoints = 0
    comppoints = 0
    while play == True:
        n = random.randint(0, 2)
        compinput = choices[n]
        userinput = input('Choose: rock, paper, or scissors. MUST BE IN LOWERCASE!!!')
        if (userinput == 'rock' and compinput == 'scissors') or (userinput == 'scissors' and compinput == 'paper') or (userinput == 'paper' and compinput == 'rock'):
            userpoints += 1
            print('Good Job you earned a point. You have {} points and the computer has {} points.'.format(userpoints, comppoints))
        elif (compinput == 'rock' and userinput == 'scissors') or (compinput == 'scissors' and userinput == 'paper') or (compinput == 'paper' and userinput == 'rock'):
            comppoints += 1
            print('OOPS. The computer earned a point. You have {} points and the computer has {} points.'.format(userpoints, comppoints))
        elif userinput == compinput:
            print('TIE. You have {} points and the Computer has {} points.'.format(userpoints, comppoints))
        else:
            print('Invalid thing entered')
            break
        question = input('Do you want to play again')
        if question == 'Yes' or question == 'yes':
            play = True
        elif question == 'No' or question == 'no':
            play = False
            if userpoints > comppoints:
                print('You won! You have {} points and the computer has {} points'.format(userpoints, comppoints))
            elif comppoints > userpoints:
                print('The computer won. You have {} points and the computer has {} points'.format(userpoints, comppoints))
            elif comppoints == userpoints:
                print('Tie. You have {} point(s) and the computer has {} points'.format(userpoints, comppoints))
            else:
                print('Invalid thing entered.')



rockpaperscissorsgame()