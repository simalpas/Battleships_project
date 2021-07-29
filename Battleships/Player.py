from GameBoard import GameBoard
from Ai import Ai
import References
import time
import random

class Player:
    def __init__(self, auto=False, test=False, aiLevel=0, randomise=False):
        # TODO remove gameboards for computer players
        self.boardPrimary = GameBoard(10)
        self.boardTracking = GameBoard(10)
        # What remains of the fleet
        self.fleetSize = {\
            'A' : 5, \
            'B' : 4, \
            'C' : 3, \
            'S' : 3, \
            'D' : 2, \
            'shipsRemaining': 5 }
        # Location of the ships in the fleet
        self.fleetLocation = { 'Aircraft Carrier': [], \
            'Battleship': [], \
            'Cruiser': [], \
            'Submarine': [], \
            'Destroyer': [] }
        self.shotsTaken = []
        self.movesMade = 0
        self.__setBoard(self.boardPrimary, auto=auto, test=test, randomise=randomise)
        self.autoPlayer = auto
        if auto:
            self.aIPlayer = Ai(aiLevel=aiLevel)

    def getBoard(self):
        return self.boardPrimary.getBoard()

    def movesMade(self):
        return self.movesMade

    def getTracking(self):
        return self.boardTracking.getBoard()

    def incoming(self, x, y):
        squareContents = self.boardPrimary.getSquare(x, y)
        # reverse lookup of symbol to shipname from dictionary
        shipName = next(key for key, value in References.symbols.items() if value == squareContents)
        # does not make clear what has been hit until ship has been destroyed
        if squareContents == ' ':
            self.boardPrimary.setSquare(x, y, References.getSymbols()['Miss'])
            return 'Miss', (x, y)
        elif squareContents != ' ' and self.fleetSize[squareContents] == 1:
             self.fleetSize[squareContents] -= 1
             self.fleetSize['shipsRemaining'] -= 1
             self.boardPrimary.setSquare(x, y, References.getSymbols()['Sunk'])
             self.__sinkShip(self.fleetLocation[shipName], self.boardPrimary)
             return shipName, self.fleetLocation[shipName]
        elif squareContents != ' ':
            self.fleetSize[squareContents] -= 1
            self.boardPrimary.setSquare(x, y, References.getSymbols()['Hit'])
            return 'Hit', (x, y)

    def takeShot(self, target):
        if self.autoPlayer:
            x, y = self.aIPlayer.takeShot()
            result = target.incoming(x, y)
            self.__recordShot(result, x, y)
        else:
            invalid = True
            while invalid:
                x, y = self.__getCoords()
                if (x,y) in self.shotsTaken:
                    print("You've already shot there, try again")
                else:
                    invalid = False
            self.shotsTaken.append((x,y))
            result = target.incoming(x, y)
            self.__recordShot(result, x, y)
        return result

    def __recordShot(self, result, x, y):
        if self.autoPlayer:
            self.aIPlayer.recordShot(result, x, y)
        elif result[0] in References.getShips():
            self.__sinkShip(result[1], self.boardTracking)
        else:
            self.boardTracking.setSquare(x, y, References.symbols[result[0]])

    def __sinkShip(self, locations, board):
        # iterate over length of ship replacing hit symbol with sunk symbol
        for i in locations:
            board.setSquare(i[0], i[1], References.getSymbols()['Sunk'])

    def __writeShip(self, grid, xCoord, yCoord, direction, shipName):
        # sends messages to board to set the locations of the fleet.
        for i in range(References.getShips()[shipName]):
            grid.setSquare(xCoord, yCoord, References.getSymbols()[shipName])
            #record ship coords.
            self.fleetLocation[shipName].append((xCoord, yCoord))
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1

    def __checkPlacement(self, grid, xCoord, yCoord, direction, shipName):
        if (xCoord+References.getShips()[shipName] > 10 and direction == 0)\
            or (yCoord+References.getShips()[shipName] > 10 and direction == 1):
            return False
        for i in range(References.getShips()[shipName]):
            if grid.getBoard()[yCoord][xCoord] != ' ':
                return False
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1
        return True

    def __placeShip(self, grid, xCoord, yCoord, direction, shipName):
        # broken, see self.__writeShip
        if self.__checkPlacement(grid, xCoord, yCoord, direction, shipName):
            self.__writeShip(grid, xCoord, yCoord, direction, shipName)
            return True
        return False

    def __setBoard(self, board, auto=False, test=False, randomise=False):
        # Broken, see self.__writeShip
        ''' Prompts to setup board for human players
        @param player: player number 1/2
        TODO should just accept a coord, and direction, then check for validity, then return either
        true of false depending on sucessful placement.
        '''
        # TODO refactor to place each ship individualy with
        # separate calls to a new function
        #TODO move functions to print the board into front end.
        if not auto:
            if test:
                # places ships in the bottom left corner for shot testing.
                for eachShip in References.getShips():
                    x, y, direction = 0, 0, 0
                    placed = False
                    while not placed:
                        placed = self.__placeShip(board, x, y, direction, eachShip)
                        y += 1
            elif randomise:
                self.__randomPlacement(board)
            else:
                # goes through the defined ships, asks for intended location
                # checks if valid loaction, and places if so.
                for eachShip in References.getShips():
                    placed = False
                    while not placed:
                        print(board)
                        print('Place your '+eachShip)
                        xCoord, yCoord, direction = self.__getCoords(placing=True)
                        placed = self.__placeShip(board, xCoord, yCoord, direction, eachShip)
                        if not placed:
                            print("Sorry, you can't place it there")
                            time.sleep(References.displayDelay)
        elif auto or randomise:
            self.__randomPlacement(board)

    def __randomPlacement(self, board):
        for eachShip in References.getShips():
            placed = False
            while not placed:
                x = random.randrange(10)
                y = random.randrange(10)
                direction = random.randrange(2)
                placed = self.__placeShip(board, x, y, direction, eachShip)

    def __getCoords(self, placing=False):
        failed = True
        while failed:
            try:
                xCoord = int(input('X-coordinate (0-9): '))
                if xCoord < 0 or xCoord > 9:
                    raise ValueError
                yCoord = int(input('y-coordinate (0-9): '))
                if yCoord < 0 or yCoord > 9:
                    raise ValueError
                direction = False #default for reuse
                if placing:
                    direction = input('To the right, or up? (r/u): ')
                    if not(direction == 'r' or direction == 'u'):
                        raise ValueError
                    elif direction == 'r':
                        direction = 0
                    elif direction == 'u':
                        direction = 1
                failed = False
            except ValueError:
                print('Sorry, your input was not recognised, please try again')
        if placing == False:
            return xCoord, yCoord, direction
        return xCoord, yCoord, direction


