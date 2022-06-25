class Maze():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = ['None' for _ in range(self.rows*self.cols)]
    
    def numRows(self):
        return self.rows
    
    def numCols(self):
        return self.cols
    
    def start(self, row, col):
        self.startrow = row
        self.startcol = col
        index = self.calcTo1D(row, col)
        self.board[index] = 'S'
    
    def finish(self, row, col):
        self.endrow = row
        self.endcol = col
        index = self.calcTo1D(row, col)
        self.board[index] = 'F'
    
    def returnboard(self):
        for i in range(0, len(self.board), self.rows):
            print(self.board[i:self.cols])
    
    def setwall(self, row, col):
        index = self.calcTo1D(row, col)
        self.board[index] = '*'
    
    def setpath(self, row, col):
        index = self.calcto1D(row, col)
        self.board[index] = '.'

    def setbacktracked(self, row, col):
        index = self.calcto1D(row, col)
        self.board[index] = 'o'
    
    def findpath(self):
        self.cr = self.startrow
        self.cc = self.startcol
        self.path = []
        done = False
        while done != True:

            if self.board[self.calcTo1D(self.cr, self.cc)] == 'F':
                done = True
            #Up
            if self.board[self.calcTo1D(self.cr-1, self.cc)] == '.' and (self.cr-1, self.cc) not in self.path:
                self.path.append((self.cr, self.cc))
                self.cr -= 1
            #Right
            elif self.board[self.calcTo1D(self.cr, self.cc+1)] == '.' and (self.cr, self.cc+1) not in self.path:
                self.path.append((self.cr, self.cc))
                self.cc += 1
            #Down
            elif self.board[self.calcTo1D(self.cr+1, self.cc)] == '.' and (self.cr+1, self.cc) not in self.path:
                self.path.append((self.cr, self.cc))
                self.cr += 1
            #Left
            elif self.board[self.calcTo1D(self.cr, self.cc-1)] == '.' and (self.cr, self.cc-1) not in self.path:
                self.path.append((self.cr, self.cc))
                self.cc -= 1
            #No Solution
            elif self.board[self.calcTo1D(self.cr, self.cc)] == 'S':
                return 'No Solution'
            #Dead End
            else:
                self.board[self.calcTo1D(self.cr, self.cc)] = 'o'
                self.cr, self.cc = self.board.pop()
        
        for self.cr, self.cc in self.path:
            self.board[self.calcTo1D(self.cr, self.cc)] == 'X'
        
        return self.board

            

    def calcTo1D(self, row, col):
        index = ((self.cols) * (row - 1)) + col
        index -= 1
        return index

a = Maze(5, 5)

a.setwall(3, 0)
a.setwall()
a.setwall()
a.setwall()
a.setwall()
a.setwall()
a.setwall()
a.setwall()
a.setwall()
a.setwall()