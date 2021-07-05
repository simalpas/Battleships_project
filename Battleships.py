# import only system from os
from os import system, name
import time
import random
from Player import Player

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Built to be used as an API
    Singleton class
    '''

    displayDelay = 2
    def __init__(self, p1auto=False, p2auto=True, test=False, aiLevelP1=0, aiLevelP2=0, randomise=False):
        # Setup new players
        self.player1 = Player(auto=p1auto, test=test, aiLevel=aiLevelP1, randomise=randomise)
        self.player2 = Player(auto=p2auto, test=test, aiLevel=aiLevelP2, randomise=randomise)

    def takeShot(self, activePlayer, target):
        result = activePlayer.takeShot(target)
        activePlayer.movesMade += 1
        checkForWin = self.winner()
        if checkForWin:
            return checkForWin
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


        

