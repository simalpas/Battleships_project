class References:
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
                    'Hit' : '\033[1;31;40mX\033[1;37;40m', \
                    'Miss' : '\033[1;34;40mo\033[1;37;40m', \
                    'Empty' : ' ',
                    'Sunk' : '\033[1;31;40m#\033[1;37;40m' \
    }
    # the delay used to display errors before clearing the screen
    displayDelay =  2

    def getShips():
        return References.ships
    
    def getSymbols():
        return References.symbols
