import random
from Piece import Piece
class Board:
    def __init__(self):
        self.r = ['1', '2', '3', '4']
        self.m = int(len(self.r))
        self.c = ['a', 'b', 'c', 'd']
        self.n = int(len(self.c))
        self.board = self.getBoard()
    def getBoard(self):
        self.board = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                s = str(self.c[j]+self.r[i])
                p = Piece(0, s)
                row.append(p)
            self.board.append(row)
        return self.board
    def isEqual(self, other):
        k = 0
        for i in range(self.m):
            for j in range(self.n):
                p = self.board[i][j]
                p1 = other.board[i][j]
                if p.value == p1.value:
                    continue
                else:
                    k += 1
        if k == 0:
            return True
        else:
            return False
    def addPiece(self):
        flag = False
        k = 0
        power = random.randint(1, 2)
        while flag == False and k <= self.countNonZero()+1:
            i = random.randint(0, self.m-1)
            j = random.randint(0, self.n-1)
            p = self.board[i][j]
            if p.value == 0:
                p.value = 2**power
                p.square = self.c[i]+self.r[j]
                flag = True
                k += 1
        return self
    def initSquareValue(self):
        for i in range(self.m):
            for j in range(self.n):
                p = self.board[i][j]
                p.turn = 1
                p.square = self.c[j]+self.r[i]
        return self
    def changeRight(self):
        for i in range(self.m):
            row = self.board[i]
            for j in range(self.n-1):
                p1 = row[self.n-j-2]
                p = row[self.n-j-1]
                p1.shiftRight(p)
        return self
    def right(self):
        if self.countNonZero() <= self.m*self.n+1:
            for k in range(self.m-1):
                self.changeRight()
            self.initSquareValue()
        return self

    def clone(self):
        other = Board()
        other.board = self.board
        return other

    def rotate(self, k): ## counter-clockwise rotation of board if k = 1
        L = []
        if k == 1:
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(self.board[j][self.n-1-i])
                L.append(row)
            self.board = L
        elif k == -1:
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(self.board[self.m-j-1][i])
                L.append(row)
            self.board = L
        self.initSquareValue()
        return self
    def rightMove(self):
        other = self.clone()
        if self.isEqual(other.right()) == True:
            self.addPiece()
        print(self)
        return self
        
    def upMove(self):
        self.rotate(-1)
        other = self.clone()
        if self.isEqual(other.right()) == True:
            self.addPiece()
        self.rotate(1)
        print(self)
        return self
    def leftMove(self):
        self.rotate(-1)
        self.rotate(-1)
        other = self.clone()
        if self.isEqual(other.right()) == True:
            self.addPiece()
        self.rotate(1)
        self.rotate(1)
        print(self)
        return self
    def downMove(self):
        self.rotate(1)
        other = self.clone()
        if self.isEqual(other.right()) == True:
            self.addPiece()
        self.rotate(-1)
        print(self)
        return self

    def countNonZero(self):
        k = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j].value != 0:
                    k += 1
        return k
        
    def __str__(self):
        bord = ''
        for i in range(self.m):
            row = '|'
            for j in range(self.n):
                row += str(self.board[i][j])
            bord += row + '\n'
        bord += '*********'*self.n + '\n'
        return bord
