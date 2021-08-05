from Player import Player

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Singleton class
    '''

    def __init__(self, p1auto=False, p2auto=True, test=False, aiLevelP1=0, aiLevelP2=0):
        # Setup new players
        self.player1 = Player(auto=p1auto, test=test, aiLevel=aiLevelP1)
        self.player2 = Player(auto=p2auto, test=test, aiLevel=aiLevelP2)

    #TODO write documentation for the various return values
    # @param coords, int 0:size
    # @param activePlayer/target : P1/P2
    def takeShot(self, activePlayer, target, xCoord=False, yCoord=False):
        #TODO error if no coords passed for human player
        """
        if activePlayer == "P1":
            activePlayer = self.__getP1()
        elif activePlayer == "P2":
            activePlayer = self.__getP2()
        if target == "P1":
            target = self.__getP1()
        elif target == "P2":
            target = self.__getP2()
            """
        activePlayerActual = self.__getPlayer(activePlayer)
        targetActual = self.__getPlayer(target)
        result = activePlayerActual.takeShot(targetActual, xCoord, yCoord)
        activePlayerActual.movesMade += 1
        if self.getWinner():
            return self.getWinner()
        return result

    def setFleetLocation(self, activePlayer, shipLocations, randomise=False):
        print('battleships arg ',shipLocations)
        return self.__getPlayer(activePlayer).setFleetLocation(shipLocations, randomise)

    def getPlayerBoard(self, player, tracking=False):
        if tracking:
            return self.__getPlayer(player).getTracking()
        else:
            return self.__getPlayer(player).getBoard()
    """
    probably redundant
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
    """

    def getAutoPlayer(self, player):
        player = self.__getPlayer(player)
        return player.getAutoPlayer()

    def __getPlayer(self, player):
        if player == "P1":
            return self.player1
        elif player == "P2":
            return self.player2

    def getMovesMade(self, player):
        return self.__getPlayer(player).getMoveMade()

    def getWinner(self):
        if self.__getPlayer('P2').fleetSize['shipsRemaining'] == 0:
            return 'P1'
        elif self.__getPlayer('P1').fleetSize['shipsRemaining'] == 0:
            return 'P2'
        else:
            return False

if __name__ == '__main__':
    def printBoard(board):
        yLabel = 9
        string = '   _______________________________________\n'
        for i in range(len(board)-1, -1, -1):
            string += str(yLabel)
            for j in board[i]:
                string += ' | ' + j
            string += ' |\n'
            yLabel -= 1
        string += '    0   1   2   3   4   5   6   7   8   9'
        print(string)

    shipLocs = [['Aircraft Carrier', (3,0), 0], \
                ['Battleship',(3,1),0], \
                ['Cruiser',(3,2),0], \
                ['Submarine',(3,3),0], \
                ['Destroyer',(3,4),0]]
    game = Battleships(p1auto=True, p2auto=True, test=False, aiLevelP1=1, aiLevelP2=1, randomise=False)
#    print(game.setFleetLocation('P1', shipLocs))
    printBoard(game.getPlayerBoard('P1', tracking=False))
#    print(game.getPlayerBoard('P1', tracking=False))
    print(game.getAutoPlayer('P1'))
    