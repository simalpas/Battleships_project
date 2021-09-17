#class References:
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
# the delay used to display errors before clearing the screen
displayDelay =  2

# The size of the gameboard
#TODO update classes to use this variable, frontend will need to set this?
sizeOfBoard = 10

def getShips():
    return ships

def getSymbols():
    return symbols

def setSizeOfBoard(size):
    sizeOfBoard = size

def getSizeOfBoard():
    return sizeOfBoard

validInputs = ['y', 'yes', 'Y' 'Yes', 'YES', 'ok', 'Ok', 'OK', 'o']

ansiColours = {\
        'black' : '\033[30m', \
        'boldBlack' : '\033[30;1m', \
        'red': '\033[31m', \
        'boldRed': '\033[31;1m', \
        'green': '\033[32m', \
        'boldGreen': '\033[32;1m', \
        'yellow' : '\033[33m', \
        'boldYellow' : '\033[33;1m', \
        'blue': '\033[34m', \
        'boldBlue': '\033[34;1m', \
        'magenta' : '\033[35m', \
        'boldMagenta' : '\033[35;1m', \
        'cyan' : '\033[36m', \
        'boldCyan' : '\033[36;1m', \
        'white' : '\033[37m', \
        'boldWhite' : '\033[37;1m', \
        'reset': '\033[0m' \
        }

resetColour = ansiColours['reset']
boardColour = ansiColours['blue']
yLabelColour = ansiColours['boldWhite']
xLabelColour = ansiColours['boldWhite']
shipColour = ansiColours['yellow']
missColour = ansiColours['cyan']
hitColour  = ansiColours['boldRed']
sunkColour = ansiColours['red']
highlightColour = ansiColours['boldMagenta']
