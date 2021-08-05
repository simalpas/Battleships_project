from Battleships import Battleships
import References
from os import system, name
import time

# DONE move algorithm to set ship locations into cli, and remove from player class
# TODO (low) change coord system in cli to use letters and then numbers
# DONE move function to get shot coords from player into cli.

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

def printBoard(board):
    # TODO aloow printing of boards side by side
    # TODO move cursor to print only changing information (low)
    yLabel = 9
    string = boardColour+'   _______________________________________\n'+resetColour
    for i in range(len(board)-1, -1, -1):
        string += yLabelColour+str(yLabel)+resetColour
        for j in board[i]:
            string += boardColour+' | ' 
            if j == References.symbols['Hit']:
                string += hitColour + j + resetColour
            elif j == References.symbols['Miss']:
                string += missColour + j + resetColour
            elif j == References.symbols['Sunk']:
                string += sunkColour + j + resetColour
            else:
                string += shipColour + j + resetColour
        string += boardColour + ' |\n' + resetColour
        yLabel -= 1
    string += xLabelColour + '    0   1   2   3   4   5   6   7   8   9' + resetColour
    print(string)

def printWinner(state):
    clear()
    if state == 'lose':
        print('\nYou Lose\n\n')
    elif state == 'win':
        print('\nYou Win!\n\n')
    print("Player 1 fleet")
    printBoard(game.getPlayerBoard('P1'))
    print("\nPlayer 1 tracking")
    printBoard(game.getPlayerBoard('P1', tracking=True))
    print('')

def runGame():
    """ Sets up the game, aiplayers, ships placement"""
    if input('Single player game? ') in validInputs:
        humanVcomp()
    elif input('Fully automatic? ') in validInputs:
        compvcomp()
    else:
        print('Exiting game.')

def setBoard(gameInstance, player):
    # TODO 
    ''' Prompts to setup board for human players
    @param player: player number 1/2
    '''
    auto = gameInstance.getAutoPlayer(player)
    # TODO handle errors, and widen valid inputs
    test = False
    #test = True if input('Do you want a test placement? ') in validInputs else False
    if not test:
        randomise = True if input('Do you want to place the ships at random? ') in validInputs else False
    if not auto:
        if test:
            # places ships in the bottom left corner for shot testing.
            x, y, direction = 0, 0, 0
            for eachShip in References.getShips():
                # in case the ships can't be placed for whatever reason
                placed = gameInstance.setFleetLocation(player, [[eachShip, (x,y), direction]])
                if not placed:
                    print('failed to place')
                    return False
                y += 1
            result = True
        elif randomise:
            # places ships at random
            result = gameInstance.setFleetLocation(player, [], randomise=True)
        else:
            # goes through the defined ships, asks for intended location
            # checks if valid loaction, and places if so.
            for eachShip in References.getShips():
                print(eachShip)
                placed = False
                index = 0
                while not placed:
                    clear()
                    print('\n')
                    printBoard(gameInstance.getPlayerBoard(player))
                    print('Place your '+eachShip)
                    xCoord, yCoord, direction = getCoords(placing=True)
                    # could check the placement in cli, but to avoid repeating myself, using functions in backend.
                    placed =  gameInstance.setFleetLocation(player, [[eachShip, (xCoord, yCoord), direction]])
                    if not placed:
                        print("Sorry, you can't place it there cli")
                        time.sleep(References.displayDelay)
                index += 1
                result = True
    elif auto or randomise:
        result = False
    return result

def checkPlacement(shipName, xCoord, yCoord, direction):
    #iterate through list checking that ships stay inside grid, and don't start at the same place.
    # TODO check for overlap (may involve passing all coords of ships to placeship)
    if (xCoord+References.getShips()[shipName] > 10 and direction == 0)\
        or (yCoord+References.getShips()[shipName] > 10 and direction == 1):
        print('nope to check cli')
        return False
    """for i in range(References.getShips()[shipName]):
        if [yCoord][xCoord] != ' ':
            return False
        if direction == 0:
            xCoord += 1
        elif direction == 1:
            yCoord += 1"""
    return True


def takeShotAt(gameInstance, activePlayer, target):
    invalid = True
    if gameInstance.getAutoPlayer(activePlayer):
        result = gameInstance.takeShot(activePlayer, target)
        invalid = False
    while invalid:
        x, y, direction = getCoords()
        result = gameInstance.takeShot(activePlayer, target, xCoord=x, yCoord=y)
        if result == -1:
            print("You've already shot there, try again")
        else:
            invalid = False
    return result

def getCoords(placing=False):
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

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print("Battleships - Shoot to win!")

#i=0

def humanVcomp():
    humanVcomp = True
    while humanVcomp:
        clear()
        game = Battleships(p1auto=False, p2auto=True, aiLevelP2=1)
        playerFirst = 0
        setBoard(game, 'P1')
        while not game.getWinner():
            clear()
            if playerFirst != 0:
                result, location = takeShotAt(game, "P2", "P1")
                if result == 'P':
                    printWinner('lose')
                    break
                # when a ship is sunk, all squares from that ship are returned, not in hit order
                # TODO could rewrite so that only the last shot taken is reported and a sunk message given.
                if result in References.ships: # ship name only returned on sink event
                    print(f"\nComputer fired at {location[0]} \nand sunk your {result}\n")
                else:
                    print('\nComputer fired at: {loc} \nand it was a {res}\n'.format(loc=location, res=result))
            else:
                print('\n\n\n')
            print("Player 1 fleet")
            printBoard(game.getPlayerBoard('P1'))
            print("\nPlayer 1 tracking")
            printBoard(game.getPlayerBoard('P1', tracking=True))
            print('')
            if cheat:
                print('CHEATING COMPUTER BOARD')
                print(f"Computer fleet size = {game.player2.fleetSize['shipsRemaining']}")
                printBoard(game.getPlayerBoard('P2'))
                print()
            result = takeShotAt(game, 'P1', 'P2')
            if result == 'P1':
                printWinner('win')
                break
            playerFirst = 1
        humanVcomp=False

def compvcomp():
    winner = 0
    compVcomp = True
    while compVcomp:
        clear()
        print()
        game = Battleships(p1auto=True, p2auto=True, aiLevelP2=1, aiLevelP1=1)
        while not game.getWinner():
            if takeShotAt(game, "P1", "P2") == "P1":
                winner = 'Player 1 wins'
                break
            clear()
            #print('player one taken a shot')
            if takeShotAt(game, "P2", "P1") == "P2":
                winner = 'Player 2 wins'
                break
            print('\n\n\n\n')
            #print('p2 has taken a shot\n')
            #print(f"\nplayer 1 moves = {game.player1.movesMade}")
            #print(f"p1 shipsRemaining = {game.player1.fleetSize['shipsRemaining']}")
            #print(f"player 2 moves = {game.player2.movesMade}")
            #print(f"p2 shipsRemaining = {game.player2.fleetSize['shipsRemaining']}")
            print("Player 1 fleet")
            printBoard(game.getPlayerBoard('P1'))
            print("\n\nPlayer 2 fleet")
            printBoard(game.getPlayerBoard('P2'))
            #time.sleep(1)
        clear()
        print('\n--', winner, '--\n')
        print(f"player 1 moves = {game.player1.movesMade}")
        print(f"player 2 moves = {game.player2.movesMade}")
        print("Player 1 fleet")
        printBoard(game.getPlayerBoard('P1'))
        print("\n\nPlayer 2 fleet")
        printBoard(game.getPlayerBoard('P2'))
        print()
        compVcomp = False

if __name__ == '__main__':
    cheat = True if input('Cheat mode? ') in validInputs else False
    runGame()