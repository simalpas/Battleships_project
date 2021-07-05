class GameBoard:
    '''
    Class that represents the game boards
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
    
    def __str__(self):
        yLabel = 9
        string = '\033[1;30;40m   _______________________________________\n'
        for i in range(len(self.board)-1, -1, -1):
            string += '\033[1;30;40m'+str(yLabel)+'\033[1;37    ;40m'
            for j in self.board[i]:
                string += '\033[1;30;40m | \033[1;37;40m' + j
            string += '\033[1;30;40m |\n\033[1;37;40m'
            yLabel -= 1
        string += '\033[1;30;40m    0   1   2   3   4   5   6   7   8   9\033[1;37;40m'
        return string


