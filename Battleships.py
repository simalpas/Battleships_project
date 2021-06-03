# import only system from os
from os import system, name
import time
import random

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Singleton class
    #TODO in the process of converting to MVC
    '''
    #class vars
    # The ships : length of ship
    ships = { 'Aircraft Carrier' : 5, \
                'Battleship' : 4, \
                'Cruiser' : 3, \
                'Submarine' : 3, \
                'Destroyer' : 2 \
    }
    # ship symbol translation
    symbols = {'Aircraft Carrier' : 'A', \
                    'Battleship' : 'B', \
                    'Cruiser' : 'C', \
                    'Submarine': 'S', \
                    'Destroyer' : 'D', \
                    'Hit' : 'X', \
                    'Miss' : 'O', \
                    'Empty' : ' ',
                    'Sunk' : '#' \
    }
    def __init__(self):
        # Setup new players
        self.player1 = Player(comp=False, test=True)
        self.player2 = Player(comp=True)

    def takeShot(self, target, x, y):
        result = target.incoming(x, y)
        return result

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

    def getShips():
        return Battleships.ships
    
    def getSymbols():
        return Battleships.symbols
    
    def clear():
    # for windows
            if name == 'nt':
                _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')

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
        yLabels = range(10)
        yCount = 0
        string = '    0   1   2   3   4   5   6   7   8   9\n'
        for i in self.board:
            string += str(yLabels[yCount])
            for j in i:
                string += ' | ' + j
            string += ' |\n'
            yCount += 1
        return string

class Player:
    def __init__(self, comp=False, test=False):
        self.boardPrimary = GameBoard(10)
        self.boardTracking = GameBoard(10)
        # What remains of the fleet
        self.fleetSize = {\
            'A' : 5, \
            'B' : 4, \
            'C' : 3, \
            'S' : 3, \
            'D' : 2 }
        # Location of the ships in the fleet
        self.fleetLocation = { 'Aircraft Carrier': [(),()], \
            'Battleship': [(),()], \
            'Cruiser': [(),()], \
            'Submarine': [(),()], \
            'Destroyer': [(),()] }
        if comp:
            self.__computerPlayer()
        else:
            self.__humanPlayer(test)

    def getBoard(self):
        return self.boardPrimary

    def getTracking(self):
        return self.boardTracking

    def incoming(self, x, y):
        squareContents = self.boardPrimary.getSquare(x, y)
        shipName = [key for key, value in Battleships.getSymbols().items() if value == squareContents]
        # does not make clear what has been hit until ship has been destroyed
        if squareContents == ' ':
            return 'MISS'
        elif squareContents != ' ' and self.fleetSize[squareContents] == 1:
             self.fleetSize[squareContents] -= 1
             self.boardPrimary.setSquare(Battleships.getSymbols()['Sunk'], x, y)
             return 'SUNK'
        elif squareContents != ' ':
            self.fleetSize[squareContents] -= 1
            self.boardPrimary.setSquare(Battleships.getSymbols()['Hit'], x, y)
            return 'HIT'

    def __sinkShip(self, shipName):
        # determine vert/horiz

        # iterate over length of ship replacing symbol with sunk
        pass

    def __humanPlayer(self, test=False):
        self.__setBoard(self.boardPrimary, test=test)

    def __computerPlayer(self):
        self.__setBoard(self.boardPrimary, auto=True)
    
    def __writeShip(self, grid, xCoord, yCoord, direction, shipName):
        '''
        @param grid: a grid object.
        @param xCoord: the x coordinate indexed from 0.
        @param yCoord: the y coordinate indexed from 0.
        @param direction: 0=horizontal 1=vertical.
        @shipName: a name in the dictionary ships.
        Pre: ship can fit where placed without overlapping or extending out of 
        the grid. ShipName type has not been placed before.
        Post: ship is placed and grid is updated with ship symbol.
        '''
        self.fleetLocation[shipName][0] = (xCoord, yCoord)
        for i in range(Battleships.getShips()[shipName]):
            grid.getBoard()[yCoord][xCoord] = Battleships.getSymbols()[shipName]
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1
        self.fleetLocation[shipName][1] = (xCoord, yCoord)

    def __checkPlacement(self, grid, xCoord, yCoord, direction, shipName):
        '''
        @param grid: a grid object.
        @param xCoord: the x coordinate indexed from 0.
        @param yCoord: the y coordinate indexed from 0.
        @param direction: 0=horizontal 1=vertical.
        @shipName: a name in the dictionary ships.
        Pre: ShipName type has not been placed before.
        Post: True if ship can be placed without overlap or extending beyond the grid
         else False.
        '''
        if (xCoord+Battleships.getShips()[shipName] > 10 and direction == 0)\
            or (yCoord+Battleships.getShips()[shipName] > 10 and direction == 1):
            return False
        for i in range(Battleships.getShips()[shipName]):
            if grid.getBoard()[yCoord][xCoord] != ' ':
                return False
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1
        return True

    def __placeShip(self, grid, xCoord, yCoord, direction, shipName):
        '''
        @param grid: a grid object.
        @param xCoord: the x coordinate indexed from 0.
        @param yCoord: the y coordinate indexed from 0.
        @param direction: 0=horizontal 1=vertical.
        @shipName: a name in the dictionary ships.
        Pre: Ship of type shipName has not been previously placed.
        Post: writes ship to grid if possible and returns True, False otherwise
        '''
        if self.__checkPlacement(grid, xCoord, yCoord, direction, shipName):
            self.__writeShip(grid, xCoord, yCoord, direction, shipName)
            return True
        return False

    def __setBoard(self, board, auto=False, test=False):
        ''' Prompts to setup board for human players
        @param player: player number 1/2
        '''
        if not auto:
            if test:
                for eachShip in Battleships.getShips():
                    x, y, direction = 0, 0, 0
                    placed = False
                    while not placed:
                        placed = self.__placeShip(board, x, y, direction, eachShip)
                        y += 1
            else:
                for eachShip in Battleships.getShips():
                    placed = False
                    while not placed:
                        print(board)
                        print('Place your '+eachShip)
                        #TODO exception handling.
                        xCoord = int(input('X-coordinate (0-9): '))
                        yCoord = int(input('y-coordinate (0-9): '))
                        direction = input('To the right, or  down? (r/d): ')
                        if direction == 'r':
                            direction = 0
                        elif direction == 'd':
                            direction = 1
                        placed = self.__placeShip(board, xCoord, yCoord, direction, eachShip)
                        if not placed:
                            print("Sorry, you can't place it there")
                            time.sleep(2)
                        #Battleships.clear()
        elif auto:
            for eachShip in Battleships.getShips():
                placed = False
                while not placed:
                    x = random.randrange(10)
                    y = random.randrange(10)
                    direction = random.randrange(2)
                    placed = self.__placeShip(board, x, y, direction, eachShip)
    

game = Battleships()

print('player1\n', game.getPlayer1().getBoard())
#print('player2\n', game.getPlayer2Primary())

print(game.takeShot(game.getPlayer1(), 0, 4))
print(game.takeShot(game.getPlayer1(), 1, 4))

print('player1\n', game.getPlayer1().getBoard())
print(game.getPlayer1().fleetLocation)