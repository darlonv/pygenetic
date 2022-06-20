
#External functions
from functions import fitness, crossover, mutation, initial_population

from tqdm import tqdm
import pandas as pd
import numpy as np

from time import sleep
import random


class genetic:
    fit = None
    fit_old = None
    fit_sum = None
    population = None
    pop_size = None
    max_gen = None

    df_pop = None

    #Parâmetros
    porcent_selection = None
    porcent_crossover = None
    porcent_mutation = None

    #Funções externas
    # fitness = fitness
    # cross = cross
    # mutation = mutation

    def __init__(self, pop_size=100, max_gen=10, verbose=False, porcent_selection=0.4, porcent_mutation=0.3, porcent_crossover=0.3):
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.verbose = verbose
        self.porcent_selection = porcent_selection
        self.porcent_crossover = porcent_crossover
        self.porcent_mutation  = porcent_mutation

    def populate(self):
        self.population = initial_population(self.pop_size)
        self.df_pop = pd.DataFrame({'Individuals': self.population})
        print(self.df_pop)

    def evolve(self):
        if self.verbose:
            print('Evolving..')

        #Calculate Fitness
        self.df_pop['Fitness'] = list(map(fitness, self.df_pop['Individuals']))
        self.fit_sum = self.df_pop['Fitness'].sum()
        #Calculate Relative Fitness
        self.df_pop['Fitness_relative'] = self.df_pop['Fitness'] / self.fit_sum 
        self.df_pop.sort_values('Fitness', ascending=False, inplace=True, ignore_index=True)
        self.df_pop['Interval_max'] = self.df_pop['Fitness_relative'].cumsum()
        self.df_pop['Interval_min'] = self.df_pop['Interval_max']-self.df_pop['Fitness_relative']
        # print(self.df_pop)

        #Elite
        df_elite = self.selection_roulette(self.porcent_selection)

        #Crossover
        df_crossover_p1 = self.selection_roulette(self.porcent_crossover)
        df_crossover_p2 = self.selection_roulette(self.porcent_crossover)

        df_crossover = pd.DataFrame({'p1':df_crossover_p1['Individuals'].tolist(), 'p2':df_crossover_p2['Individuals'].tolist()})
        df_crossover['Individuals'] = list(map(crossover, df_crossover['p1'], df_crossover['p2']))


        #Mutation
        df_mutation = self.selection_roulette(self.porcent_mutation)
        df_mutation['Individuals'] = list(map(mutation, df_mutation['Individuals']))

        #Get Elite, Crossover and Mutation results as the new population
        col='Individuals'        
        self.df_pop = pd.concat([df_elite[[col]], df_crossover[[col]], df_mutation[[col]]], ignore_index=True)
        


    def run(self):
        if not self.population:
            self.populate()
        else:
            if self.verbose:
                print('Population generated')

        

        if self.verbose:
            print('Running...')
        for gen in tqdm(range(self.max_gen)):
            if self.verbose:
                print(f'Generation {gen}')

            #Evolve onde generation
            self.evolve()
            
        print('Final population:')
        self.df_pop['Fitness'] = list(map(fitness, self.df_pop['Individuals']))
        self.df_pop.sort_values('Fitness', ascending=False, inplace=True, ignore_index=True)
        print(self.df_pop.iloc[0])





        if self.verbose:
            print('Finished')

    def selection_roulette(self, porc):
        if self.verbose:
            print('Selection Roulette')

        selected_idx = []
        n_selection = round(self.pop_size * porc)
        # print(n_selection, porc)
        for i in range(n_selection):
            r = random.random()
            # print('r:',r)
            selected_idx.append(self.df_pop[(self.df_pop['Interval_min']<= r) & ((self.df_pop['Interval_max']>= r)) ].index.values[0])
        # print(selected_idx)
        
        df_select = self.df_pop.loc[self.df_pop.index[selected_idx]]
        return df_select

        

    def __str__(self):
        return str(self.population)