class GameBoard:
    '''
    Class that represents the game boards
    Does this by storing symbols in a 2 dimensional array.
    Has a toString method for basic visual representation of the board
    '''
    def __init__(self, size):
        self.board = self.__newBoard(size)
    
    def getBoard(self):
        return self.board
    
    def getSquare(self, x, y):
        return self.board[y][x]

    def setSquare(self, symbol, x, y):
        self.board[y][x] = symbol

    def __newBoard(self, size):
        '''Creates a 2 dimensional array filled with a blank spaces to be used as a board'''
        board = []
        for i in range(size):
            row = []
            for i in range(size):
                row.append(' ')
            board.append(row)
        return board

    def sumUp(self, a, b):
        return a+b
    
    def __str__(self):
        yLabel = 9
        string = '   _______________________________________\n'
        for i in range(len(self.board)-1, -1, -1):
            string += str(yLabel)
            for j in self.board[i]:
                string += ' | ' + j
            string += ' |\n'
            yLabel -= 1
        string += '    0   1   2   3   4   5   6   7   8   9'
        return string


