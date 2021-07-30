from Player import Player

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Singleton class
    '''

    def __init__(self, p1auto=False, p2auto=True, test=False, aiLevelP1=0, aiLevelP2=0, randomise=False):
        # Setup new players
        self.player1 = Player(auto=p1auto, test=test, aiLevel=aiLevelP1, randomise=randomise)
        self.player2 = Player(auto=p2auto, test=test, aiLevel=aiLevelP2, randomise=randomise)

    #TODO write documentation for the various return values
    # TODO should take coordinates as arguments, returning what was hit.
    # curently runs an algorithm that gathers the inputs.
    # and ensure that the returns are only chars.
    # @param coords, int 0:size
    # @param activePlayer/target : P1/P2
    def takeShot(self, activePlayer, target, xCoord=False, yCoord=False):
#        print(xCoord, yCoord)
        if activePlayer == "P1":
            activePlayer = self.__getP1()
        elif activePlayer == "P2":
            activePlayer = self.__getP2()
        if target == "P1":
            target = self.__getP1()
        elif target == "P2":
            target = self.__getP2()
        # TODO add code to handle Ai player, and process received coords
        result = activePlayer.takeShot(target, xCoord, yCoord)
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

    def getAutoPlayer(self, player):
        if player == 'P1':
            return self.__getP1().getAutoPlayer()
        elif player == 'P2':
            return self.__getP2().getAutoPlayer()

    def __getP1(self):
        return self.player1

    def __getP2(self):
        return self.player2

    def getMovesMadeP1(self):
        return self.__getP1().movesMade
 
    def getMovesMadeP2(self):
        return self.__getP2().movesMade       

    def movesMade(self, player):
        if player == 'P1':
            return str(self.__getP1().movesMade())
        elif player == 'P2':
            return str(self.__getP2().mavesMade())

    def winner(self):
        if self.__getP2().fleetSize['shipsRemaining'] == 0:
            return 'P2'
        elif self.__getP1().fleetSize['shipsRemaining'] == 0:
            return 'P1'
        else:
            return False
