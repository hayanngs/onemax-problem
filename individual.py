import _random


class Individual:
    '''
        Individual - Classe que Representa um individuo.
        É um bytearray.
        No byte temos, 0 como 48 e 1 como 49
    '''

    def __init__(self, size):
        self.caracteristica = bytearray()
        self.size = size
        self.fitness = 0
        n = 0
        while n < self.size:
            rand = _random.Random()
            number = rand.random()
            if number < 0.5:
                self.caracteristica.append(48)
            else:
                self.caracteristica.append(49)
            n += 1

    #        for b in self.caracteristica:
    #            print( b )

    def calc_fitness(self):
        score = 0
        counter = 0
        while counter < self.size:
            if self.caracteristica[counter] == 49:
                score += 1
            counter += 1
        #            print( 'in calc_fitness, counter is: {0}, score is {1}'.format( counter, score ) )
        self.fitness = score
        return score

    def mutate(self):
        index = 0

        rand = _random.Random()
        number = rand.random()

        number2 = number * self.size

        index = int(number2)

        if self.caracteristica[index] == 48:
            self.caracteristica[index] = 49
        else:
            self.caracteristica[index] = 48

#        i = 0
#        while i < self.size:
#            print( 'byte is : {0}'.format( self.caracteristica[ i ] ) )
#            i += 1
