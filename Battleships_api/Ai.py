from . import References
import random

class Ai():
    def __init__(self, aiLevel=0):
        self.aiLevel = aiLevel
        self.possibleShots = []
        self.__initialisePossibleShots()
        self.shiptracking = {\
            'unsunk': [], \
            'Aircraft Carrier' : 0, \
            'Battleship': 0, \
            'Cruiser': 0, \
            'Submarine': 0, \
            'Destroyer': 0}
        self.latestShot = (0,0)
        self.testingShots = [(0,4), (1,4)]
    
    def takeShot(self):
        # selects a square to shoot at
        if self.aiLevel == 0:
            self.latestShot = self.__randomShots()
        elif self.aiLevel == 1:
            self.latestShot = self.__randomWithShipTracking()
        elif self.aiLevel == 'testing':
            self.latestShot = self.__testingShots()
        else:
            self.latestShot = self.__randomWithShipTracking()
        return self.latestShot

    def recordShot(self, result, x, y):
        # records in the hit list (shiptracking) when a ship has been sunk or just hit
        # requires the sunken ship locations to be passed to it from Player.takeShot()
        if result[0] == 'Hit':
            self.shiptracking['unsunk'].append((x, y))
        if result[0] in References.getShips():
            self.shiptracking['unsunk'].append((x, y))
            # removes the locations of unknown hits when informed of a sinking 
            # and updates tracking with sunken ship allowing length tracking.
            for i in result[1]:
                self.shiptracking['unsunk'].pop(self.shiptracking['unsunk'].index(i))
            self.shiptracking[result[0]] = 1
        
    def getLatestShot(self):
        return self.latestShot

    def __randomShots(self):
        random.shuffle(self.possibleShots)
        return self.possibleShots.pop()

    def __randomWithShipTracking(self):
        potentialShot = self.__shipTrackingAlgorithm()
        if potentialShot != False:
            self.possibleShots.pop(self.possibleShots.index(potentialShot))
        if potentialShot == False:
            potentialShot = self.__randomShots()
        return potentialShot

    def __systematicWithShipTracking(self):
        pass

    def __testingShots(self):
        return self.testingShots.pop()

    def __shipTrackingAlgorithm(self):
        # TODO logical deduction of ship location from all previous shots including misses
        # if no hits, return False
        #print('length of unsunk list', len(self.shiptracking['unsunk']))
        if len(self.shiptracking['unsunk']) == 0:
            return False
        # go through the unsunk locations, if only one: generate possible shots, check if 
        # legal shots, remove those that are not, randomly choose from remaining
        # and return one of them.
        if len(self.shiptracking['unsunk']) == 1:
            knownHit = self.shiptracking['unsunk'][0]
            #print('knownHit: ', knownHit)
            bestGuesses = self.__generatePotentialShots(knownHit)
            #print('bestGuesses: ',bestGuesses)
            readyToFire = random.choice(bestGuesses)
            #print('Ready to fire at: ', readyToFire)
            return readyToFire
        # if there are two or more check if they are adjacent and record if in x or y direction
        # generate possible shots, check if legal, remove those that are not, randomly choose
        # from remaining and return.
        if len(self.shiptracking['unsunk']) >=2:
            # determine if x or y direction
            knownHits = self.shiptracking['unsunk']
            if knownHits[len(knownHits)-1][0] == knownHits[len(knownHits)-2][0]:
                direction = 1
            else:
                direction = 0
            # TODO deal with edge cases where unsunk ships length is same as max unsunk
            # and location on board means it cannot continue in that direction.
            #print('direction found: ', direction)
            # generate possible shots for all coordinates along that axis. Previously taken
            # shots will be automatically removed. Not an efficient way of doing this!
            # However as board is a max of 100 squares, processing power not a premium.
            # TODO refactor to only generate for the extremes of unsunk ships
            bestGuesses = []
            for eachHit in knownHits:
                #print('Generating for: ', eachHit)
                for eachGuess in self.__generatePotentialShots(eachHit, direction=direction):
                    bestGuesses.append(eachGuess)
            # if possible shots are empty choose one of the hits in unsunk and assume single hit
            #print('bestGuesses generated: ', bestGuesses)
            bestGuesses = self.__sanitiseList(bestGuesses)
            #print('sanitised: ', bestGuesses)
            if len(bestGuesses) == 0:
                while len(bestGuesses) == 0:
                    # print('looking for something to shoot at')
                    bestGuesses = self.__generatePotentialShots(random.choice(knownHits))
                readyToFire = random.choice(bestGuesses)
                #print("found this though ", bestGuesses)
            else:
                readyToFire = random.choice(bestGuesses)
            #print('readyToFire: ', readyToFire)
            return readyToFire

    def __generatePotentialShots(self, knownHit, direction='all'):
        potentialShots = []
        x = knownHit[0]
        y = knownHit[1]
        # generate possible shots orthagonally adjacent taking into account direction
        # direction == False : all orthagonally adjacent
        # direction == 0 : horizontal
        # direction == 1 : vertical
        if direction == 0 or direction == 'all':
            for i in [x-1, x+1]:
                potentialShots.append((i, y))
        if direction == 1 or direction == 'all':
            for j in [y-1, y+1]:
                    potentialShots.append((x, j))
        #print('generated tuples: ',potentialShots)
        potentialShots = self.__sanitiseList(potentialShots)
        return potentialShots

    def __sanitiseList(self, guesses):
        potentialShots = []
        for eachTuple in guesses:
            if eachTuple in self.possibleShots:
                potentialShots.append(eachTuple)
        #print('reduced list: ', potentialShots)
        return potentialShots

    def __maxShipLength(self):
        if self.shiptracking['Aircraft Carrier'] == 0:
            return 5
        elif self.shiptracking['Battleship'] == 0:
            return 4
        elif (self.shiptracking['Cruiser'] == 1) or (self.shiptracking['Submarine'] == 1):
            return 3
        return 2

    def __initialisePossibleShots(self):
        for i in range(10):
            for j in range(10):
                self.possibleShots.append((i,j))

#testInstance = Ai(aiLevel=1)
#print(testInstance.possibleShots)