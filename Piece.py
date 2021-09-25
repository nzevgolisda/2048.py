
class Piece:
    def __init__(self, value, square):
        self.value = value
        self.square = square
        self.turn = 1
    def shiftRight(self, other):
        if self.value != 0:
            if other.value == 0:
                other.value = self.value
                self.value = 0
            elif other.value != 0:
                if self.value == other.value:
                    if other.turn == 1 and self.turn == 1:
                        other.value += self.value
                        self.value = 0
                        other.turn = 0
    def __str__(self):
        if self.value == 0:
            return str('     ')+'| '
        else:
            if self.value < 10:
                return '  '+str(self.value)+'  | '
            elif self.value  < 100:
                return ' '+str(self.value)+'  | '
            elif self.value < 1000:
                return ' '+str(self.value)+' | '
            elif self.value >=1000:
                return str(self.value)+' | '
             
    ##def __str__(self):
    ##    if self.value == 0:
    ##        return ' '+str(self.square)+' | '
    ##    else:
    ##        return '  '+str(self.value)+' | '