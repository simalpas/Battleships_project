class PositiveFractions:
    """ Creates a list of all the positive fractions.
    @param n largest denominator
    pre: n > 0
    defensively takes absolute if -ve number input 
    PAYG : no or y default is no. Will not print in order"""
    
    def __init__(self, n, PAYG=None):
        self.n = abs(n)
        # use a set to automatically ignore duplicates
        self.fractions = {}
        if PAYG == 'y':
            self.__printAsYouGo()
        else:
            self.__allPositiveFractions()

    def __factorise(self,n):
        factors = []
        for i in range(1,n+1):
            if float(n/i)%1 == 0:
                factors.append(int(n/i))
                i += 1
        return factors

    def __largestCommon(self, a, b):
        aFactors = self.__factorise(a)
        bFactors = self.__factorise(b)
        for i in aFactors:
            for j in bFactors:
                if i == j:
                    return i

    def __simplify(self,a,b):
        factor = self.__largestCommon(a,b)
        top = a / factor
        bottom = b / factor        
        return (int(top), int(bottom))

    def __allPositiveFractions(self):
        count = 1
        while self.n > 0:
            #nested loops to ensure all combinations are considered
            for i in range(1, count+1):
                for j in range(1, count+1):
                    # Simplify the fraction before adding to set.
                    self.fractions[self.__simplify(j,i)] = ""
            # increase the count, and decrease n to get closer to end condition.
            count+=1
            self.n -=1

    def __printAsYouGo(self):
        count = 1
        currentFraction = {}
        while self.n > 0:
            #nested loops to ensure all combinations are considered
            for i in range(1, count+1):
                for j in range(1, count+1):
                    # Simplify the fraction before adding to set.
                    currentFraction[self.__simplify(j,i)] = ""
                    for x in currentFraction.keys():
                        print('{a}/{b}'.format(a=x[0], b=x[1]), end="  ")
                    currentFraction.clear()
                    self.fractions[self.__simplify(j,i)] = ""
            # increase the count, and decrease n to get closer to end condition.
            count+=1
            self.n -=1

    def __str__(self):
        string = ""
        # iterate through the keys (automatically sorted in python 3.7 
        # and above) printing the first element of the list over the second.
        for x in self.fractions.keys():
            string += ('{a}/{b}'.format(a=x[0], b=x[1])) + "  "
        return string

print(PositiveFractions(9))