from pprint import pprint
class ReversiGameLogic:
    def __init__(self):
        self.board = [[0] * 8] * 8
        self.board[3][3] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 1
        self.currentplayer = 1
        self.nextplayer = 2

    
    def whoseTurn(self):
        return self.currentplayer
    
    def numChips(self, player):
        counter = 0
        for i in self.board:
            for j in i:
                if j == player:
                    counter += 1
        
        return counter
    
    def numOpenSquares(self):
        counter = 0
        for i in self.board:
            for j in i:
                if j == 0:
                    counter += 1
        
        return counter
    
    def getWinner(self):
        pass

    def isLegalMove(self, row, col):
        if self.numOpenSquares() == 0:
            self.currentplayer = 0
            self.nextplayer = 0
            return 'NoMovesLeft'

        self.movesAvailable = []
        if self.board[row][col] == 0:
            #Up
            if self.board[row-1][col] == self.nextplayer and self.board[row-2][col] == self.currentplayer:
                self.movesAvailable.append('Up')
            #UpRight
            if self.board[row-1][col+1] == self.nextplayer and self.board[row-2][col+2] == self.currentplayer:
                self.movesAvailable.append('UpRight')
            #Right
            if self.board[row][col+1] == self.nextplayer and self.board[row][col+2] == self.currentplayer:
                self.movesAvailable.append('Right')
            #RightDown
            if self.board[row+1][col+1] == self.nextplayer and self.board[row+2][col+2] == self.currentplayer:
                self.movesAvailable.append('RightDown')
            #Down
            if self.board[row+1][col] == self.nextplayer and self.board[row+2][col] == self.currentplayer:
                self.movesAvailable.append('Down')
            #DownLeft
            if self.board[row+1][col-1] == self.nextplayer and self.board[row+2][col-2] == self.currentplayer:
                self.movesAvailable.append('DownLeft')
            #Left
            if self.board[row][col-1] == self.nextplayer and self.board[row][col-2] == self.currentplayer:
                self.movesAvailable.append('Left')
            #LeftUp
            if self.board[row-1][col-1] == self.nextplayer and self.board[row-2][col-2] == self.currentplayer:
                self.movesAvailable.append('LeftUp')
        
        if self.movesAvailable != []:
            return True
        else:
            return False

    def occupiedBy(self, row, col):
        return self.board[row][col]
    
    def makeMove(self, row, col):
        if self.isLegalMove(row, col) == True:
            for i in self.movesAvailable:
                if i == 'Up':
                    self.board[row-1][col] = self.currentplayer
                if i == 'UpRight':
                    self.board[row-1][col+1] = self.currentplayer
                if i == 'Right':
                    self.board[row][col+1] = self.currentplayer
                if i == 'RightDown':
                    self.board[row+1][col+1] = self.currentplayer
                if i == 'Down':
                    self.board[row+1][col] = self.currentplayer
                if i == 'DownLeft':
                    self.board[row+1][col-1] = self.currentplayer
                if i == 'Left':
                    self.board[row][col-1] = self.currentplayer
                if i == 'LeftUp':
                    self.board[row-1][col-1] = self.currentplayer
        
        self.board[row][col] = self.currentplayer

        if self.currentplayer == 1:
            self.currentplayer = 2
            self.nextplayer = 1
        elif self.currentplayer == 2:
            self.currentplayer = 1
            self.nextplayer = 2

    def returnboard(self):
        for i in self.board:
            print(i)
        return 'Current Board'

a = ReversiGameLogic()

a.returnboard()
a.numOpenSquares()


asdf = [[0] * 8] * 8

asdf[3][4] = 9
pprint(asdf)