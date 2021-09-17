from .Player import Player

class Battleships:
    '''
    Class that plays the game of Battleships with varying degrees of intelligence
    Singleton class
    '''

    def __init__(self, p1auto=False, p2auto=True, test=False, aiLevelP1=0, aiLevelP2=0, boardSize=10):
        """
        TODO document
        """
        # Setup new players
        self.player1 = Player(auto=p1auto, test=test, aiLevel=aiLevelP1, boardSize=boardSize)
        self.player2 = Player(auto=p2auto, test=test, aiLevel=aiLevelP2, boardSize=boardSize)

    # @param coords, int 0:size
    # @param activePlayer/target : P1/P2
    def takeShot(self, activePlayer, target, xCoord=False, yCoord=False):
        """ 
        Returns a tuple with first value of'Hit', 'Miss' or shipName and second value of the coordinate shot at, or
        a list of the coordinates of the sunken ship. If the shot coords are invalid, it will return -1. If the game
        detects a winner it will return the winner in the form 'P1' or 'P2' 
        """
        #TODO error if no coords passed for human player
        activePlayerActual = self.__getPlayer(activePlayer)
        targetActual = self.__getPlayer(target)
        result = activePlayerActual.takeShot(targetActual, xCoord, yCoord)
        activePlayerActual.movesMade += 1
        if self.getWinner():
            return self.getWinner()
        return result

    def setFleetLocation(self, activePlayer, shipLocations, randomise=False):
        """
        TODO document
        """
        return self.__getPlayer(activePlayer).setFleetLocation(shipLocations, randomise)

    def getPlayerBoard(self, player, tracking=False):
        """
        TODO document
        """
        if tracking:
            return self.__getPlayer(player).getTracking()
        else:
            return self.__getPlayer(player).getBoard()

    def getAutoPlayer(self, player):
        """
        TODO document
        """
        player = self.__getPlayer(player)
        return player.getAutoPlayer()

    def getLatestShot(self, player):
        """
        TODO document
        """
        return self.__getPlayer(player).getLatestShot()
        
    def __getPlayer(self, player):
        """
        TODO document
        """
        if player == "P1":
            return self.player1
        elif player == "P2":
            return self.player2

    def getMovesMade(self, player):
        """
        TODO document
        """
        return self.__getPlayer(player).getMoveMade()

    def getWinner(self):
        """
        TODO document
        """
        if self.__getPlayer('P2').fleetSize['shipsRemaining'] == 0:
            return 'P1'
        elif self.__getPlayer('P1').fleetSize['shipsRemaining'] == 0:
            return 'P2'
        else:
            return False

# For testing purposes ship placement TODO move into separate testing suite
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
    game = Battleships(p1auto=False, p2auto=True, aiLevelP2=1)
    print('Player1 fleet following placement')
    print(game.setFleetLocation('P1', shipLocs))
    printBoard(game.getPlayerBoard('P1', tracking=False))
    print('\nPlayer2 board after automatic random placement')
    printBoard(game.getPlayerBoard('P2', tracking=False))
    print(f"Is player2 computer controlled? {game.getAutoPlayer('P2')}")
    