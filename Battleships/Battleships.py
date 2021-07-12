from Player import Player

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Singleton class
    '''

    displayDelay = 2
    def __init__(self, p1auto=False, p2auto=True, test=False, aiLevelP1=0, aiLevelP2=0, randomise=False):
        # Setup new players
        self.player1 = Player(auto=p1auto, test=test, aiLevel=aiLevelP1, randomise=randomise)
        self.player2 = Player(auto=p2auto, test=test, aiLevel=aiLevelP2, randomise=randomise)

    #TODO write documentation for the various return values
    # and ensure that the returns are only chars, player object should not be passed as an argument
    def takeShot(self, activePlayer, target):
        if activePlayer == "P1":
            activePlayer = self.__getP1()
        elif activePlayer == "P2":
            activePlayer = self.__getP2()
        if target == "P1":
            target = self.__getP1()
        elif target == "P2":
            target = self.__getP2()
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

    def __getP1(self):
        return self.player1

    def __getP2(self):
        return self.player2

    def getMovesMadeP1(self):
        return self.__getP1().movesMade
 
    def getMovesMadeP2(self):
        return self.__getP2().movesMade       

    def winner(self):
        if self.__getP2().fleetSize['shipsRemaining'] == 0:
            return 'Player 1 wins in '+str(self.__getP1().movesMade)
        elif self.__getP1().fleetSize['shipsRemaining'] == 0:
            return 'Player 2 wins in '+str(self.__getP2().movesMade)
        else:
            return False
