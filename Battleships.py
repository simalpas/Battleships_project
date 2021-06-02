# import only system from os
from os import system, name
import time

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    '''
    def __init__(self):
        # The ships : (length of ship, quantity)
        self.ships = { 'Aircraft Carrier' : 5, \
                    'Battleship' : 4, \
                    'Cruiser' : 3, \
                    'Submarine' : 3, \
                    'Destroyer' : 2 \
        }
        # ship symbol translation
        self.symbols = {'Aircraft Carrier' : 'A', \
                        'Battleship' : 'B', \
                        'Cruiser' : 'C', \
                        'Submarine': 'S', \
                        'Destroyer' : 'D', \
                        'Hit' : 'x', \
                        'Miss' : 'o' \
        }

        # initialise grids 10x10
        self.player1Primary = self.__newBoard(10)
        self.player1Tracking = self.__newBoard(10)
        self.player2Primary = self.__newBoard(10)
        self.player2Tracking = self.__newBoard(10)

    def __newBoard(self, size):
        '''Creates a 2 dimensional array filled with a blank spaces to be used as a board'''
        board = []
        for i in range(size):
            row = []
            for i in range(size):
                row.append(' ')
            board.append(row)
        return board

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
        for i in range(self.ships[shipName]):
            grid[yCoord][xCoord] = self.symbols[shipName]
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1

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
        if (xCoord+self.ships[shipName] > 10) or (yCoord+self.ships[shipName] > 10):
            return False
        for i in range(self.ships[shipName]):
            if grid[yCoord][xCoord] != ' ':
                return False
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1
        return True

    def placeShip(self, grid, xCoord, yCoord, direction, shipName):
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

    def setBoard(self, player):
        ''' Prompts to setup board for human players
        @param player: player number 1/2
        '''
        if player == 1:
            board = self.player1Primary
        elif player == 2:
            board = self.player2Primary
        for eachShip in self.ships:
            placed = False
            while not placed:
                self.printGrid(board)
                print('Place your '+eachShip)
                #TODO exception handling.
                xCoord = int(input('X-coordinate for '+eachShip+' (0-9): '))
                yCoord = int(input('y-coordinate for '+eachShip+' (0-9): '))
                direction = input('To the right, or  down? (r/d)')
                if direction == 'r':
                    direction = 0
                elif direction == 'd':
                    direction = 1
                placed = self.placeShip(board, xCoord, yCoord, direction, eachShip)
                if not placed:
                    print("Sorry, you can't place it there")
                    time.sleep(2)
                self.clear()
                

    
    def printGrid(self, grid):
        yLabels = range(10)
        yCount = 0
        print('    0   1   2   3   4   5   6   7   8   9')
        for i in grid:
            print(yLabels[yCount], end='')
            for j in i:
                print(' | '+j, end='')
            print(' |')
            yCount += 1
        print('-----------------------')
    
    def clear(self):
    # for windows
            if name == 'nt':
                _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')

game = Battleships()


#print(game.player1Primary)

#game.placeShip(game.player1Primary, 0, 0, 0, 'Aircraft Carrier')
#game.placeShip(game.player1Primary, 6, 4, 1, 'Battleship')
game.setBoard(1)




game.printGrid(game.player1Primary)