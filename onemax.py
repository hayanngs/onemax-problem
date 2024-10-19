from individual import Individual
import _random

#    algorithm parameters
genotype_size = 100
pop_size = 100
crossover_rate = 0.75

num_gen = 25
num_runs = 25


#    -----------------------------------------------------------------

def show_average_population_fitness(population):
    sum = 0
    for ind in population:
        #        ind.calc_fitness( )
        #print('Caracteristica: {0}'.format(ind.caracteristica))
        sum += ind.fitness
    print('Soma é: {0}'.format(sum))
    print('\tMédia de aptidão da população é: {0:.3f}'.format(sum / pop_size))


def select_parents(population, mating_pool):
    n = 0
    while n < pop_size:
        rand = _random.Random()
        number1 = rand.random()
        number1 = number1 * pop_size
        index1 = int(number1)
        number2 = rand.random()
        number2 = number2 * pop_size
        index2 = int(number2)
        #        print( 'index1 is: {0} and index2 is: {1}'.format( index1, index2 ) )
        if population[index1].fitness > population[index2].fitness:
            mating_pool.append(population[index1])
        else:
            mating_pool.append(population[index2])
        n += 1

#    print( 'size of mating pool is: {0}'.format( n ) )
#    n = 0
#    while n < pop_size:
#        print( mating_pool[ n ].fitness )
#        n += 1


def recombine(mating_pool):
    crossover_number = int(pop_size * crossover_rate)
    # Crossover precisa ser sempre número par
    if crossover_number % 2 == 1:
        crossover_number -= 1

    rand = _random.Random()
    # temp = rand.random()
    # crossover_point = int( temp * genotype_size )
    crossover_point = int(0.5 * genotype_size)

    #    Crossover precisa de 2 pais
    loop_counter = 0
    loop_counter = crossover_number / 2

    ints = []
    for i in range(genotype_size):
        ints.append(i)

    n = 0
    while n < loop_counter:
        number1 = rand.random()

        number1 = number1 * len(ints)
        temp1 = int(number1)

        index1 = ints[temp1]

        del ints[temp1]

        number2 = rand.random()

        number2 = number2 * len(ints)
        temp2 = int(number2)

        index2 = ints[temp2]

        del ints[temp2]

        # Pegar dois individuos para a recombinação
        ind1 = mating_pool[index1]
        ind2 = mating_pool[index2]

        i = crossover_point
        caracteristica1 = bytearray()
        caracteristica2 = bytearray()

        # Obter as caracteristicas dos dois individuos do crossover_point pra frente
        while i < genotype_size:
            caracteristica1.append(ind1.caracteristica[i])
            caracteristica2.append(ind2.caracteristica[i])
            i += 1

        # Retirar caracteristicas desses dois individuos ate o crossover_point
        i = 0
        while i < crossover_point:
            ind1.caracteristica.pop()
            ind2.caracteristica.pop()
            i += 1

        # Recombinar as caracteristicas de cada individuo
        i = crossover_point
        caracteristica_counter = 0
        while i < genotype_size:
            ind1.caracteristica.append(caracteristica2[caracteristica_counter])
            ind2.caracteristica.append(caracteristica1[caracteristica_counter])
            i += 1
            caracteristica_counter += 1

        n += 1


def mutate(mating_pool):
    rand = _random.Random()
    number1 = rand.random()
    number1 = number1 * pop_size
    index1 = int(number1)
    mating_pool[index1].mutate()


def evaluate(mating_pool):
    n = 0
    while n < pop_size:
        mating_pool[n].calc_fitness()
        n += 1
#    show_average_population_fitness( mating_pool )


def select_candidates_for_next_generation(population, mating_pool):
    population.clear()

    population.extend(mating_pool)

    mating_pool.clear()


#    -----------------------------------------------------------------


population = []
mating_pool = []

for run in range(num_runs):
    print('\nRodada: {0}'.format(run))
    population.clear()
    n = 0
    # Criando população
    while n < pop_size:
        individual = Individual(genotype_size)
        population.append(individual)
        n += 1

    # Calcular o fitness (Aptidão)
    evaluate(population)

    #    Loop geracional
    for n in range(1, num_gen+1):
        print('\n\tGeração: {0}'.format(n))
        # Selecionar os pais
        select_parents(population, mating_pool)

        # Crossover
        recombine(mating_pool)

        # Mutação
        mutate(mating_pool)

        # Calcular o fitness (Aptidão) da mating_pool
        evaluate(mating_pool)

        select_candidates_for_next_generation(population, mating_pool)
        evaluate(population)
        show_average_population_fitness(population)

# Mostrando a populaçao final
print("\nPopulação final:\n")
show_average_population_fitness(population)
for n in range(pop_size):
    print(population[n].caracteristica)
