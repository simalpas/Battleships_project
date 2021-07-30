from Battleships import Battleships
import References
from os import system, name

# TODO move algorithm to set ship locations into cli, and remove from player class
# TODO change coord system in cli to use letters and then numbers
# TODO move function to get shot coords from player into cli.


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
boardColour = ansiColours['white']
yLabelColour = ansiColours['boldWhite']
xLabelColour = ansiColours['boldWhite']
shipColour = ansiColours['yellow']
missColour = ansiColours['cyan']
hitColour  = ansiColours['boldRed']
sunkColour = ansiColours['red']

def printBoard(board):
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
    printBoard(game.getPlayer1Board())
    print("\nPlayer 1 tracking")
    printBoard(game.getPlayer1Board(tracking=True))
    print('')

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

compVcomp = False
humanVcomp = True
i=0
while humanVcomp:
# TODO check for win after each turn
    clear()
    game = Battleships(p1auto=False, p2auto=True, randomise=False, aiLevelP2=1, test=True)
    playerFirst = 0
    while not game.winner():
        clear()
        if playerFirst != 0:
            result, location = takeShotAt(game, "P2", "P1")
            if result == 'P':
                printWinner('lose')
                break
            print('\nComputer fired at: {loc} \nand it was a {res}\n'.format(loc=location, res=result))
        else:
            print('\n\n\n')
        print("Player 1 fleet")
        printBoard(game.getPlayer1Board())
        print("\nPlayer 1 tracking")
        printBoard(game.getPlayer1Board(tracking=True))
        print('')
        cheat = True
        if cheat:
            print('CHEATING COMPUTER BOARD')
            printBoard(game.getPlayer2Board())
            print()
        result = takeShotAt(game, 'P1', 'P2')
        if result == 'P1':
            printWinner('win')
            break
        playerFirst = 1
    humanVcomp=False



while compVcomp:
    clear()
    game = Battleships(p1auto=True, p2auto=True, randomise=True, aiLevelP2=1, aiLevelP1=1)
    while not game.winner():
        takeShotAt(game, "P1", "P2")
        takeShotAt(game, "P2", "P1")
    print("Player 1 fleet")
    printBoard(game.getPlayer1Board())
    print("\n\nPlayer 2 fleet")
    printBoard(game.getPlayer2Board())
    compVcomp = False

#print(game.winner())