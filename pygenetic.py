
#External functions
from operator import index
from functions import fitness, crossover, mutation, initial_population

from tqdm import tqdm
import pandas as pd
import numpy as np

from time import sleep
import random


class Genetic:
    fit = None
    population = None
    pop_size = None
    max_gen = None

    df_pop = None

    #Parâmetros
    prob_mutation = 0.5

    output = None
    report = None

    #Algoritmos
    alg_selection = None

    def __init__(self, pop_size=100, max_gen=10, verbose=False, prob_mutation=0.3,  alg_selection='roulette', output=True, report=0):
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.verbose = verbose
        self.prob_mutation  = porcentprob_mutation_mutation
        self.alg_selection = alg_selection
        self.output = output
        self.report = report

    def populate(self):
        self.population = initial_population(self.pop_size)
        self.df_pop = pd.DataFrame({'Individuals': self.population})

    def fitness(self):
        #Calculate Fitness
        self.df_pop['Fitness'] = list(map(fitness, self.df_pop['Individuals']))

    def relative_fitness(self):
        #Calculate Relative Fitness
        self.df_pop['Fitness_relative'] = self.df_pop['Fitness'] / self.df_pop['Fitness'].sum()
        self.df_pop.sort_values('Fitness', ascending=False, inplace=True, ignore_index=True)
        self.df_pop['Interval_max'] = self.df_pop['Fitness_relative'].cumsum()
        self.df_pop['Interval_min'] = self.df_pop['Interval_max']-self.df_pop['Fitness_relative']

    def evolve(self):
        if self.verbose:
            print('Evolving..')

        #Crossover
        sons_cross = []
        while len(sons_cross) < self.pop_size:
            if self.alg_selection == 'roulette':
                father, mother = self.selection_roulette(), self.selection_roulette()
            
            sons_cross.append(crossover(father, mother))
        
 
        #Mutation
        sons_mutation = []
        for son in sons_cross:
            r = random.random()
            if r < self.prob_mutation:
                son = mutation(son)
            sons_mutation.append(son)
        self.df_pop['Individuals'] = sons_mutation

        self.fitness()
        if self.alg_selection == 'roulette':
            self.relative_fitness()
        


    def run(self):
        if not self.population:
            self.populate()
            self.fitness()
            if self.alg_selection == 'roulette':
                self.relative_fitness()
        else:
            if self.verbose:
                print('Population generated')

        

        if self.verbose:
            print('Running...')

        if self.output:
            #Evolve showing a progress bar
            for gen in tqdm(range(self.max_gen)):
                if self.verbose: print(f'Generation {gen}')

                #Evolve a generation
                self.evolve()
        else:
            #Evolve without show a progress bar.
            for gen in range(self.max_gen):
                if self.verbose: print(f'Generation {gen}')

                #Evolve a generation
                self.evolve()

            
        self.df_pop['Fitness'] = list(map(fitness, self.df_pop['Individuals']))
        self.df_pop.sort_values('Fitness', ascending=False, inplace=True, ignore_index=True)
        if self.report:
            print(self.df_pop.head(self.report)[['Individuals','Fitness']])
        else:
            print(self.df_pop.head(1)[['Individuals','Fitness']])
        
        if self.verbose:
            print('Finished')

    def selection_roulette(self):
        
        r = random.random()
        return self.df_pop[(self.df_pop['Interval_min']<= r) & ((self.df_pop['Interval_max']>= r)) ]['Individuals'].values[0]


        

    def __str__(self):
        return str(self.population)