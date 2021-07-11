# import only system from os
from os import system, name
import time
import random

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Built to be used as an API
    Singleton class
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
                    'Miss' : 'o', \
                    'Empty' : ' ',
                    'Sunk' : '#' \
                    }
    # colours and their escape sequences
    ansiColours = {\
        'red': '\033[31m', \
        'blue': '\033[34m', \
        'green': '\033[32m', \
        'darkRed': '\033[31;1m', \
        'reset': '\033[0m' \
        }
    # adjust any display delay
    displayDelay = 2

    def __init__(self, p1auto=False, p2auto=True, test=False, aiLevelP1=0, aiLevelP2=0, randomise=False):
        # Setup new players
        self.player1 = Player(auto=p1auto, test=test, aiLevel=aiLevelP1, randomise=randomise)
        self.player2 = Player(auto=p2auto, test=test, aiLevel=aiLevelP2, randomise=randomise)

    def takeShot(self, activePlayer, target):
        result = activePlayer.takeShot(target)
        activePlayer.movesMade += 1
        return result

    def getPlayer1Board(self, tracking=False):
        if not tracking:
            return self.player1.getBoard()
        else:
            return self.player1.getTracking()

    def getPlayer2Board(self, tracking=False):
        if not tracking:
            return self.player2.getBoard()
        else:
            return self.player2.getTracking()

    def getP1(self):
        return self.player1

    def getP2(self):
        return self.player2

    def winner(self):
        if self.getP2().fleetSize['shipsRemaining'] == 0:
            return 'Player 1 wins in '+str(self.getP1().movesMade)
        elif self.getP1().fleetSize['shipsRemaining'] == 0:
            return 'Player 2 wins in '+str(self.getP2().movesMade)
        else:
            return False

    def getShips():
        return Battleships.ships
    
    def getSymbols():
        return Battleships.symbols
        
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
    
    def __colourShip(self, string):
        return Battleships.ansiColours['green']+string+Battleships.ansiColours['reset']
    
    def __colourMiss(self, string):
        return Battleships.ansiColours['blue']+string+Battleships.ansiColours['reset']

    def __colourHit(self, string):
        return Battleships.ansiColours['red']+string+Battleships.ansiColours['reset']

    def __colourSunk(self, string):
        return Battleships.ansiColours['darkRed']+string+Battleships.ansiColours['reset']

    def __str__(self):
        yLabel = 9
        string = '   _______________________________________\n'
        for i in range(len(self.board)-1, -1, -1):
            string += str(yLabel)
            for j in self.board[i]:
                if j == Battleships.getSymbols()['Aircraft Carrier'] or \
                j == Battleships.getSymbols()['Battleship'] or \
                j == Battleships.getSymbols()['Cruiser'] or \
                j == Battleships.getSymbols()['Submarine'] or \
                j == Battleships.getSymbols()['Destroyer']:
                    j = self.__colourShip(j)
                elif  j == Battleships.getSymbols()['Miss']:
                    j = self.__colourMiss(j)
                elif j == Battleships.getSymbols()['Hit']:
                    j = self.__colourHit(j)
                elif j == Battleships.getSymbols()['Sunk']:
                    j = self.__colourSunk(j)
                string += ' | ' + j
            string += ' |\n'
            yLabel -= 1
        string += '    0   1   2   3   4   5   6   7   8   9'
        return string

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
            self.aIPlayer = aI(aiLevel=aiLevel)

    def getBoard(self):
        return self.boardPrimary

    def getTracking(self):
        return self.boardTracking

    def incoming(self, x, y):
        squareContents = self.boardPrimary.getSquare(x, y)
        # reverse lookup of symbol to shipname from dictionary
        shipName = next(key for key, value in Battleships.symbols.items() if value == squareContents)
        # does not make clear what has been hit until ship has been destroyed
        if squareContents == ' ':
            #colour symbol
            self.boardPrimary.setSquare(Battleships.getSymbols()['Miss'], x, y)
            return 'Miss', (x, y)
        elif squareContents != ' ' and self.fleetSize[squareContents] == 1:
             self.fleetSize[squareContents] -= 1
             self.fleetSize['shipsRemaining'] -= 1
             self.boardPrimary.setSquare(Battleships.getSymbols()['Sunk'], x, y)
             self.__sinkShip(self.fleetLocation[shipName], self.boardPrimary)
             return shipName, self.fleetLocation[shipName]
        elif squareContents != ' ':
            self.fleetSize[squareContents] -= 1
            self.boardPrimary.setSquare(Battleships.getSymbols()['Hit'], x, y)
            return 'Hit', (x, y)

    def takeShot(self, target):
        if self.autoPlayer:
            x, y = self.aIPlayer.takeShot()
            result = target.incoming(x, y)
            self.__recordShot(result, x, y)
        else:
            invalid = True
            while invalid:
                x, y, direction = self.__getCoords()
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
        elif result[0] in Battleships.getShips():
            self.__sinkShip(result[1], self.boardTracking)
        else:
            self.boardTracking.setSquare(Battleships.symbols[result[0]], x, y)

    def __sinkShip(self, locations, board):
        # iterate over length of ship replacing hit symbol with sunk symbol
        for i in locations:
            board.setSquare(Battleships.getSymbols()['Sunk'], i[0], i[1])

    def __writeShip(self, grid, xCoord, yCoord, direction, shipName):
        for i in range(Battleships.getShips()[shipName]):
            grid.getBoard()[yCoord][xCoord] = Battleships.getSymbols()[shipName]
            #record ship coords.
            self.fleetLocation[shipName].append((xCoord, yCoord))
            if direction == 0:
                xCoord += 1
            elif direction == 1:
                yCoord += 1

    def __checkPlacement(self, grid, xCoord, yCoord, direction, shipName):
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
        if self.__checkPlacement(grid, xCoord, yCoord, direction, shipName):
            self.__writeShip(grid, xCoord, yCoord, direction, shipName)
            return True
        return False

    def __setBoard(self, board, auto=False, test=False, randomise=False):
        ''' Prompts to setup board for human players
        @param player: player number 1/2
        '''
        # TODO refactor to place each ship individualy with
        # separate calls to a new function
        if not auto:
            if test:
                # places ships in the bottom left corner for shot testing.
                for eachShip in Battleships.getShips():
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
                for eachShip in Battleships.getShips():
                    placed = False
                    while not placed:
                        print(board)
                        print('Place your '+eachShip)
                        xCoord, yCoord, direction = self.__getCoords(placing=True)
                        placed = self.__placeShip(board, xCoord, yCoord, direction, eachShip)
                        if not placed:
                            print("Sorry, you can't place it there")
                            time.sleep(Battleships.displayDelay)
        elif auto or randomise:
            self.__randomPlacement(board)

    def __randomPlacement(self, board):
        for eachShip in Battleships.getShips():
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
        if direction == False:
            return xCoord, yCoord, direction
        return xCoord, yCoord, direction

class aI:
    def __init__(self, aiLevel=0):
        self.aiLevel = aiLevel
        self.possibleShots = []
        self.shiptracking = {\
            'unsunk': [], \
            'Aircraft Carrier' : 0, \
            'Battleship': 0, \
            'Cruiser': 0, \
            'Submarine': 0, \
            'Destroyer': 0}
        self.__initialisePossibleShots()
        self.testingShots = [(0,4), (1,4)]
    
    def takeShot(self):
        # selects a square to shoot at
        if self.aiLevel == 0:
            return self.__randomShots()
        elif self.aiLevel == 1:
            return self.__randomWithShipTracking()
        elif self.aiLevel == 'testing':
            return self.__testingShots()
        else:
            pass

    def recordShot(self, result, x, y):
        # records in the hit list (shiptracking) when a ship has been sunk or just hit
        if result[0] == 'Hit':
            self.shiptracking['unsunk'].append((x, y))
        if result[0] in Battleships.getShips():
            self.shiptracking['unsunk'].append((x, y))
            # removes the locations of unknown hits when informed of a sinking 
            # and updates tracking with sunken ship allowing length tracking.
            for i in result[1]:
                self.shiptracking['unsunk'].pop(self.shiptracking['unsunk'].index(i))
            self.shiptracking[result[0]] = 1
        
    def __randomShots(self):
        random.shuffle(self.possibleShots)
        return self.possibleShots.pop()

    def __randomWithShipTracking(self):
        potentialShot = self.__shipTrackingAlgorithm()
        if potentialShot != False:
            self.possibleShots.pop(self.possibleShots.index(potentialShot))
        if potentialShot == False:
            potentialShot = self.__randomShots()
        return potentialShot

    def __systematicWithShipTracking(self):
        pass

    def __testingShots(self):
        return self.testingShots.pop()

    def __shipTrackingAlgorithm(self):
        # TODO logical deduction of ship location from all previous shots including misses
        # if no hits, return False
        #print('length of unsunk list', len(self.shiptracking['unsunk']))
        if len(self.shiptracking['unsunk']) == 0:
            return False
        # go through the unsunk locations, if only one: generate possible shots, check if 
        # legal shots, remove those that are not, randomly choose from remaining
        # and return one of them.
        if len(self.shiptracking['unsunk']) == 1:
            knownHit = self.shiptracking['unsunk'][0]
            #print('knownHit: ', knownHit)
            bestGuesses = self.__generatePotentialShots(knownHit)
            #print('bestGuesses: ',bestGuesses)
            readyToFire = random.choice(bestGuesses)
            #print('Ready to fire at: ', readyToFire)
            return readyToFire
        # if there are two or more check if they are adjacent and record if in x or y direction
        # generate possible shots, check if legal, remove those that are not, randomly choose
        # from remaining and return.
        if len(self.shiptracking['unsunk']) >=2:
            # determine if x or y direction
            knownHits = self.shiptracking['unsunk']
            if knownHits[len(knownHits)-1][0] == knownHits[len(knownHits)-2][0]:
                direction = 1
            else:
                direction = 0
            # TODO deal with edge cases where unsunk ships length is same as max unsunk
            # and location on board means it cannot continue in that direction.
            #print('direction found: ', direction)
            # generate possible shots for all coordinates along that axis. Previously taken
            # shots will be automatically removed. Not an efficient way of doing this!
            # However as board is a max of 100 squares, processing power not a premium.
            # TODO refactor to only generate for the extremes of unsunk ships
            bestGuesses = []
            for eachHit in knownHits:
                #print('Generating for: ', eachHit)
                for eachGuess in self.__generatePotentialShots(eachHit, direction=direction):
                    bestGuesses.append(eachGuess)
            # if possible shots are empty choose one of the hits in unsunk and assume single hit
            #print('bestGuesses generated: ', bestGuesses)
            bestGuesses = self.__sanitiseList(bestGuesses)
            #print('sanitised: ', bestGuesses)
            if len(bestGuesses) == 0:
                while len(bestGuesses) == 0:
                    # print('looking for something to shoot at')
                    bestGuesses = self.__generatePotentialShots(random.choice(knownHits))
                readyToFire = random.choice(bestGuesses)
                #print("found this though ", bestGuesses)
            else:
                readyToFire = random.choice(bestGuesses)
            #print('readyToFire: ', readyToFire)
            return readyToFire

    def __generatePotentialShots(self, knownHit, direction='all'):
        potentialShots = []
        x = knownHit[0]
        y = knownHit[1]
        # generate possible shots orthagonally adjacent taking into account direction
        # direction == False : all orthagonally adjacent
        # direction == 0 : horizontal
        # direction == 1 : vertical
        if direction == 0 or direction == 'all':
            for i in [x-1, x+1]:
                potentialShots.append((i, y))
        if direction == 1 or direction == 'all':
            for j in [y-1, y+1]:
                    potentialShots.append((x, j))
        #print('generated tuples: ',potentialShots)
        potentialShots = self.__sanitiseList(potentialShots)
        return potentialShots

    def __sanitiseList(self, guesses):
        potentialShots = []
        for eachTuple in guesses:
            if eachTuple in self.possibleShots:
                potentialShots.append(eachTuple)
        #print('reduced list: ', potentialShots)
        return potentialShots

    def __maxShipLength(self):
        if self.shiptracking['Aircraft Carrier'] == 0:
            return 5
        elif self.shiptracking['Battleship'] == 0:
            return 4
        elif (self.shiptracking['Cruiser'] == 1) or (self.shiptracking['Submarine'] == 1):
            return 3
        return 2

    def __initialisePossibleShots(self):
        for i in range(10):
            for j in range(10):
                self.possibleShots.append((i,j))