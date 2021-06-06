from Battleships import Battleships

game = Battleships(p1auto=False, p2auto=True, test=True, aiLevelP2=1)

i = 0
while not game.winner():
    print('Taken a shot at ',game.takeShot(game.getP2(), game.getP1()))
    #print('Computer player tracking: \n', game.getP2().aIPlayer.shiptracking)
    #print('Computer player possible shots remaining: ', len(game.getP2().aIPlayer.possibleShots))
    print('Player 1 Primary\n', game.getPlayerBoard(game.getP1(), tracking=False))
    print('END OF TURN')


print(game.winner())
#print('Player 1 Primary\n', game.getPlayerBoard(game.getP1(), tracking=False))

#print('Computer player tracking: \n', game.getP2().aIPlayer.shiptracking)

#TODO write the class that will make the calls in order to run the game.