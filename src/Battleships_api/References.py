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

