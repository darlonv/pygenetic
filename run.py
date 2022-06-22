import argparse
import sys

from pygenetic import Genetic

#Variables and default values
POP_SIZE = 100
MAX_GENERATIONS = 100
QUIT = 10

VERBOSE=False
OUTPUT = True
PROGRESS_BAR = True

SELECTION_ALG = 'roulette'

# PORC_CROSSOVER= 0.5
PROB_MUTATION= 0.3
# PORC_ELITE = 0.5

ALG_SELECTION = 'roulette'

N_REPORT=1

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--population', help=f'Population size. Default: {POP_SIZE}', type=int, default=POP_SIZE)
parser.add_argument('-g', '--generations', help=f'Maximum number of generations. Default: {MAX_GENERATIONS}', type=int, default=MAX_GENERATIONS)

parser.add_argument('-sa', '--selection', help=f'Selection algorithm. Default: {ALG_SELECTION}', choices=['roulette','fitness','tournament','ranking'])
parser.add_argument('-mp', '--mutation', help=f'Mutation probability. Default: {PROB_MUTATION}', type=float, default=PROB_MUTATION)

parser.add_argument('-q', '--quiet', help='No output', action='store_true')
parser.add_argument('-r', '--report', help=f'Show final population, ordered by fitness. Default: {N_REPORT}', type=int, default=N_REPORT)
parser.add_argument('-v', '--verbose', help='Detail output', action='store_true')


args = parser.parse_args()

if args.verbose:        VERBOSE=True
if args.population:     POPSIZE = args.population
if args.mutation:       PROB_MUTATION = args.mutation
if args.generations:    MAX_GENERATIONS = args.generations
if args.quiet:          OUTPUT=False
if args.report:         N_REPORT=args.report
# if args.noprogress:     PROGRESS_BAR = False

if args.selection:   ALG_SELECTION = args.selection

# if args.elite:          PORC_ELITE = args.elite
# if args.crossover:      PORC_CROSSOVER = args.crossover
if args.mutation:       PROB_MUTATION = args.mutation


ag = Genetic(pop_size = POPSIZE,
    max_gen = MAX_GENERATIONS,
    verbose = VERBOSE,
    alg_selection=ALG_SELECTION,
    output=OUTPUT,
    report=N_REPORT)

ag.run()

# # ag.populate()
# ag.run()
# print(ag)