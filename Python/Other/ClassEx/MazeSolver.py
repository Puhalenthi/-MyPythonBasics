import emoji

class Maze():
    def __init__(self, rows = 3, cols = 3):
        self.rows = rows + 2
        self.cols = cols + 2
        self.board = []

    def blankMaze(self):
        self.board = []
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.cols):
                self.board[i].append('X')

    def passMaze(self):
        self.blankMaze()

        check = int(input('Do you want to enter the whole maze (0) or row by row (1):       '))

        if check:
            for i in range(1, self.rows):
                passed = input('Enter a row of the maze:    ')
                j = 1
                for char in passed:
                    self.board[i][j] = char
                    if char == 'S':
                        self.startrow = i
                        self.startcol = j
                    j += 1
        else:
            passed = (input('Enter the maze:     '))
            if len(passed) == (self.rows - 2) * (self.cols - 2):
                for i in range(self.rows - 2):
                    boardrow = passed[i:((self.rows - 2) * (i + 1))]
                    if 'S' in boardrow:
                        counter = 0
                    for j in range(len(boardrow)):
                        self.board[i + 1][j + 1] = boardrow[j]
                        if boardrow[j] == 'S':
                            self.startrow = i
                            self.startcol = counter
                        counter += 1



    def numRows(self):
        return self.rows
    
    def numCols(self):
        return self.cols
    
    def start(self, row, col):
        self.startrow = row
        self.startcol = col
        self.board[row][col] = 'S'
    
    def finish(self, row, col):
        self.endrow = row
        self.endcol = col
        self.board[row][col] = 'F'
    
    def returnboard(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'X':
                    print(emoji.emojize(':black_large_square:'), end = '')
                elif self.board[i][j] == '*':
                    print(emoji.emojize(':white_large_square:'), end = '')
                elif self.board[i][j] == 'o':
                    print(emoji.emojize(':blue_square:'), end = '')
                elif self.board[i][j] == 'S':
                    print(emoji.emojize(':green_square:'), end = '')
                else:
                    print(emoji.emojize(':red_square:'), end = '')
            print()

    
    def setwall(self, row, col):
        self.board[row][col] = 'X'
    
    def setpath(self, row, col):
        self.board[row][col] = '.'

    def setbacktracked(self, row, col):
        self.board[row][col] = 'o'
    
    def findpath(self):
        self.cr = self.startrow
        self.cc = self.startcol
        self.path = []
        done = False
        while done != True:
            print(self.path)
            if self.board[self.cr][self.cc] == 'F':
                done = True
            #Up
            elif (self.board[self.cr - 1][self.cc] == '.' and (self.cr - 1, self.cc) not in self.path) or (self.board[self.cr - 1][self.cc] == 'F' and self.cr != 0):
                self.path.append((self.cr, self.cc))
                self.cr -= 1
            #Right
            elif (self.board[self.cr][self.cc + 1] == '.' and (self.cr, self.cc + 1) not in self.path) or (self.board[self.cr][self.cc + 1] == 'F' and self.cc != (self.cols - 1)):
                self.path.append((self.cr, self.cc))
                self.cc += 1
            #Down
            elif (self.board[self.cr + 1][self.cc] == '.' and (self.cr + 1, self.cc) not in self.path) or (self.board[self.cr + 1][self.cc] == 'F' and self.cr != (self.rows - 1)):
                self.path.append((self.cr, self.cc))
                self.cr += 1
            #Left
            elif (self.board[self.cr][self.cc - 1] == '.' and (self.cr, self.cc - 1) not in self.path) or (self.board[self.cr][self.cc - 1] == 'F' and self.cc != 0):
                self.path.append((self.cr, self.cc))
                self.cc -= 1
            #No Solution
            elif self.board[self.cr][self.cc] == 'S':
                done = True
                return 'No Solution'
            #Dead End
            else:
                self.board[self.cr][self.cc] = 'o'
                self.cr, self.cc = self.path.pop()
        
        for self.cr, self.cc in self.path:
            if self.board[self.cr][self.cc] != 'S':
                self.board[self.cr][self.cc] = '*'
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == '.':
                    self.board[i][j] = 'o'
        
        return self.returnboard()


b = Maze(21, 21)
b.passMaze()
b.findpath()

'''
XXX  XX   X 
   X    X X 
 X X XXXX X 
 XSX XXX  X 
 XX  X   XX 
    XX X    
XXX XF XXXX 
'''

'''
X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X   X                       X                           X           X           X
X   X   X   X X X X X X X X X   X X X X X   X X X X X   X   X X X X X   X X X   X
X   X   X   X           X       X           X       X       X       X   X       X
X   X   X   X   X X X   X   X X X   X   X X X   X   X X X   X   X   X   X   X X X
X       X   X   X       X   X       X   X       X       X   X   X       X       X
X   X X X   X   X   X X X   X   X X X   X   X X X X X   X   X   X X X X X X X   X
X   X       X   X           X       X   X   X       X   X   X           X   X   X
X   X   X X X   X X X X X X X X X   X X X   X   X   X   X X X X X X X   X   X   X
X S X                           X               X   X                       X F X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X #


'''

'''

XSXXXXXXXXXXXXXXXXXXX
X.............X.X...X
X.XXXXX.XXXXX.X.X.X.X
X.X...X.X.....X...X.X
X.X.XXX.X.XXXXXXXXX.X
X...X...X.......X...X
XXXXX.X.XXXXXXX.X.X.X
X.....X.X.....X.X.X.X
X.XXXXX.X.XXX.X.X.X.X
X.....X.X.X...X.X.X.X
XXXXX.XXX.X.XXX.X.X.X
X.....X...X...X...X.X
X.XXXXX.XXXXX.XXXXX.X
X.......X...X.X.....X
XXXXXXXXX.X.XXX.XXXXX
X.X...X...X...X...X.X
X.X.X.X.X.XXXXXXX.X.X
X...X.X.X.......X...X
X.XXX.X.XXXXXXX.XXX.X
X...X.........X.....X
XXXXXXXXXXXXXXXXXXXFX

'''



'''

 X         X X 
 X X XXXXXXX X 
 X X X     X X 
 X X X XXX X X 
   X X X   X X 
 XXX X X XXX X 
 X   X X    X  
 X XXX XXXXXXX 
SX         XF  

'''

'''
 X           X             X     X     
 X X XXXXXXXXX XXXXX XXXXX X XXXXX XXX 
 X X X     X   X     X   X   X   X X   
 X X X XXX X XXX X XXX X XXX X X X X XX
   X X X   X X   X X   X   X X X   X   
 XXX X X XXX X XXX X XXXXX X X XXXXXXX
 X   X X     X   X X X   X X X     X X 
 X XXX XXXXXXXXX XXX X X X XXXXXXX X X 
SX             X       X X            XF


'''