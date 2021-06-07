from Battleships import Battleships
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print("Battleships - Shoot to win!")
clear()
game = Battleships(p1auto=False, p2auto=True, test=True, aiLevelP2=1)

i = 0
#while not game.winner():
while i<5:
    clear()
    result, location = game.takeShot(game.getP2(), game.getP1())
    print('\nComputer fired at: \n{loc} and it was a {res}\n'.format(loc=location, res=result))
    print("Player 1 fleet")
    print(game.getPlayer1Board())
    print("\nPlayer 1 tracking")
    print(game.getPlayer1Board(tracking=True))
    print("\nCheating by looking at the computer's board\n{board}".format(board=game.getPlayer2Board()))
    game.takeShot(game.getP1(), game.getP2())
    #print('Computer player tracking: \n', game.getP2().aIPlayer.shiptracking)
    #print('Computer player possible shots remaining: ', len(game.getP2().aIPlayer.possibleShots))
    #print('Player 1 Primary\n', game.getPlayerBoard(game.getP1(), tracking=False))
    print('END OF TURN')
    i+=1


print(game.winner())
#print('Player 1 Primary\n', game.getPlayerBoard(game.getP1(), tracking=False))

#print('Computer player tracking: \n', game.getP2().aIPlayer.shiptracking)

#TODO write the class that will make the calls in order to run the game.