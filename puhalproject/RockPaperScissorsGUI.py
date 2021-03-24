import tkinter as t
import random
choices = ['Rock', 'Paper', 'Scissors']
userscore = 0
compscore = 0
whowins = ''
screen = t.Tk()

screen.geometry('500x500')

def comp_calc_rock():
    global choices, userscore, compscore, whowins
    compnum = random.randint(0, 2)
    compitem = choices[compnum]
    if compitem == 'Paper':
        compscore += 1
        whowins = 'Computer'
    elif compitem == 'Scissors':
        userscore += 1
        whowins = 'You'
    else:
        whowins = 'No One'
    output['text'] = f'{whowins} Won\nYour Choice:  Rock\nComputer\'s Choice:   {compitem}\n    Your Score : {userscore}\n   Computer\'s Score:  {compscore}'
    output.pack()
def comp_calc_paper():
    global choices, userscore, compscore, whowins
    compnum = random.randint(0, 2)
    compitem = choices[compnum]
    if compitem == 'Scissors':
        compscore += 1
        whowins = 'Computer'
    elif compitem == 'Rock':
        userscore += 1
        whowins = 'You'
    else:
        whowins = 'No One'
    output['text'] = f'{whowins} Won\nYour Choice:  Paper\nComputer\'s Choice:   {compitem}\n    Your Score : {userscore}\n   Computer\'s Score:  {compscore}'
    output.pack()

def comp_calc_scissors():
    global choices, userscore, compscore, whowins
    compnum = random.randint(0, 2)
    compitem = choices[compnum]
    if compitem == 'Rock':
        compscore += 1
        whowins = 'Computer'
    elif compitem == 'Paper':
        userscore += 1
        whowins = 'You'
    else:
        whowins = 'No One'
    output['text'] = f'{whowins} Won\nYour Choice:  Scissors\nComputer\'s Choice:   {compitem}\n    Your Score : {userscore}\n   Computer\'s Score:  {compscore}'
    output.pack()

def restart():
    global choices, userscore, compscore, whowins
    userscore = 0
    compscore = 0
    whowins = ''
    output['text'] = f'You Have Restarted The Game. The Two Scores Are Now Set To 0.'
    output.pack()


frame = t.Frame(master=screen)
frame.pack()
rockbutton = t.Button(master=frame, text='Rock', width='7', height='2', command=comp_calc_rock, bg='blue')
rockbutton.pack(side='left')
paperbutton = t.Button(master=frame, text='Paper', width='7', height='2', command=comp_calc_paper, bg='green')
paperbutton.pack(side='left')
scissorsbutton = t.Button(master=frame, text='Scissors', width='7', height='2', command=comp_calc_scissors, bg='red')
scissorsbutton.pack(side='left')
output = t.Label(master=screen, text='Click On A Button To Start!')
output.pack()
restartbutton = t.Button(master=screen, text='Click Here To Restart The Game', width='23', height='2', command=restart)
restartbutton.pack()

screen.mainloop()