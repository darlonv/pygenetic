import random

def fitness(individual, verbose=False):
    fit = None

    #######################################
    if verbose:
        print(f'Genetic fitness function for {individual}', end=' ')
    fit = 0
    for i in range(1,len(individual)):
        fit+=individual[i]*i

    if verbose:
        print(f'fit: {fit}')
    #######################################

    return fit
    # return 10


def crossover(indiv0, indiv1, verbose=False):
    son=indiv0.copy()


    #######################################
    if verbose:
        print('Genetic cross function')
    meio = round(len(indiv0)/2)

    son = indiv0[:meio]+indiv1[meio:]
    #######################################

    return son

def mutation(indiv, verbose=False):
    mutate = indiv.copy()

    #######################################
    if verbose:
        print('Genetic mutation function')
    random.shuffle(mutate)
    #######################################

    return mutate

def initial_population(size=10, verbose=False):
    pop = [] #Population

    #######################################
    if verbose:
        print(f'Generating initial population with size {size}')

    for i in range(size):
        x = list(range(12))
        random.shuffle(x)
        pop.append(x)
    


    #######################################

    #Return the population
    return pop