from random import randint

def tictactoe():
    symbols = ['X', 'O']
    index = randint(0, 1)
    usersymbol = symbols[index]
    complete = False
    Row1 = [' ', ' ', ' ']
    Row2 = [' ', ' ', ' ']
    Row3 = [' ', ' ', ' ']
    try:
        compsymbol = symbols[index + 1]
    except:
        compsymbol = symbols[index - 1]
    print('Your symbol is:       {}'.format(usersymbol))
    while complete == False:
        UserRowInput = int(input('Which row do you want to enter your value in'))
        UserColumnInput = int(input('Which column would you like to put it in'))
        if UserRowInput == 1:
            if UserColumnInput == 1 and Row1[0] == ' ':
                Row1[0] = usersymbol
            elif UserColumnInput == 2 and Row1[1] == ' ':
                Row1[1] = usersymbol
            elif UserColumnInput == 3 and Row1[2] == ' ':
                Row1[2] = usersymbol
            else:
                print('Column has to be 1, 2, or 3')
                complete = True
        elif UserRowInput == 2:
            if UserColumnInput == 1 and Row2[0] == ' ':
                Row2[0] = usersymbol
            elif UserColumnInput == 2 and Row2[1] == ' ':
                Row2[1] = usersymbol
            elif UserColumnInput == 3 and Row2[2] == ' ':
                Row2[2] = usersymbol
            else:
                print('Column has to be 1, 2, or 3')
                complete = True
        elif UserRowInput == 3:
            if UserColumnInput == 1 and Row3[0] == ' ':
                Row3[0] = usersymbol
            elif UserColumnInput == 2 and Row3[1] == ' ':
                Row3[1] = usersymbol
            elif UserColumnInput == 3 and Row3[2] == ' ':
                Row3[2] = usersymbol
            else:
                print('Column has to be 1, 2, or 3')
                complete = True
        else:
            print('Row has to be 1, 2, or 3')
            complete = True
        if complete == True:
            break
        print('Your Move')
        print(Row1)
        print(Row2)
        print(Row3, '\n')
        if Row1[0] == Row1[1] == Row1[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row1[1] == Row1[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row2[0] == Row2[1] == Row2[2] == usersymbol:
            print('YOU WON')
            complete == True
        elif Row2[0] == Row2[1] == Row2[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row3[0] == Row3[1] == Row3[2] == usersymbol:
            print('YOU WON')
            complete == True
        elif Row3[0] == Row3[1] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[0] == Row2[0] == Row3[0] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row2[0] == Row3[0] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[1] == Row2[1] == Row3[1] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[1] == Row2[1] == Row3[1] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[2] == Row2[2] == Row3[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[2] == Row2[2] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True      
        compcomplete = False
        while compcomplete == False and complete == False:
            CompRow = randint(1, 3)
            CompColumn = randint(1, 3)
            if CompRow == 1:
                if CompColumn == 1 and Row1[0] == ' ':
                    Row1[0] = compsymbol
                    compcomplete = True
                elif CompColumn == 2 and Row1[1] == ' ':
                    Row1[1] = compsymbol
                    compcomplete = True
                elif CompColumn == 3 and Row1[2] == ' ':
                    Row1[2] = compsymbol
                    compcomplete = True
            elif CompRow == 2:
                if CompColumn == 1 and Row2[0] == ' ':
                    Row2[0] = compsymbol
                    compcomplete = True
                elif CompColumn == 2 and Row2[1] == ' ':
                    Row2[1] = compsymbol
                    compcomplete = True
                elif CompColumn == 3 and Row2[2] == ' ':
                    Row2[2] = compsymbol
                    compcomplete = True
            elif CompRow == 3:
                if CompColumn == 1 and Row3[0] == ' ':
                    Row3[0] = compsymbol
                    compcomplete = True
                elif CompColumn == 2 and Row3[1] == ' ':
                    Row3[1] = compsymbol
                    compcomplete = True
                elif CompColumn == 3 and Row3[2] == ' ':
                    Row3[2] = compsymbol
                    compcomplete = True
        print("Computer's Move")
        print(Row1)
        print(Row2)
        print(Row3, '\n')
        if Row1[0] == Row1[1] == Row1[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row1[1] == Row1[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row2[0] == Row2[1] == Row2[2] == usersymbol:
            print('YOU WON')
            complete == True
        elif Row2[0] == Row2[1] == Row2[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row3[0] == Row3[1] == Row3[2] == usersymbol:
            print('YOU WON')
            complete == True
        elif Row3[0] == Row3[1] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[0] == Row2[0] == Row3[0] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row2[0] == Row3[0] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[1] == Row2[1] == Row3[1] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[1] == Row2[1] == Row3[1] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[2] == Row2[2] == Row3[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[2] == Row2[2] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == usersymbol:
            print('YOU WON ')
            complete = True
        elif Row1[0] == Row2[1] == Row3[2] == compsymbol:
            print('The computer Won :(')
            complete = True


tictactoe()