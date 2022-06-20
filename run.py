import argparse

#Variables and default values
POP_SIZE = 100
MAX_GENERATIONS = 100
QUIT = 10
CROSSOVER_PROB= 0.5
MUTATION_PROB= 0.5
SELECTION_ALG = None
VERBOSE=False
QUIET = False
PROGRESS_BAR = True
SELECTION_PORC = 0.5
SELECTION_ALG = None

parser = argparse.ArgumentParser()
#parser.add_argument('echo', help='Echo the string you use here')
parser.add_argument('-p', '--population', help='population size', type=int, default=POP_SIZE)
parser.add_argument('-g', '--generations', help='Maximum number of iterations', type=int, default=MAX_GENERATIONS)
# parser.add_argument('-q', '--quit', help='Maximum generations to test without improvements', type=int, default = QUIT)
parser.add_argument('-q', '--quiet', help='No stdout output', type=bool, default = QUIET)
parser.add_argument('-b', '--progress', help='Show progress bar, according to the max number of iterations', type=bool, default = True)
parser.add_argument('-c', '--cross', help='Crossover probability', type=float, default=CROSSOVER_PROB)
parser.add_argument('-m', '--mutation', help='Mutation probability', type=float, default=MUTATION_PROB)
parser.add_argument('-sa', '--selectionalg', help='Selection algorithm', type=int, default=SELECTION_ALG)
parser.add_argument('-sp', '--selectionporcent', help='Selection algorithm', type=float, default=SELECTION_PORC)
parser.add_argument('-v', '--verbose', help='Detail output', action='store_true')


args = parser.parse_args()

if args.verbose:        VERBOSE=True
if args.population:     POPSIZE = args.population
if args.generations:    MAX_GENERATIONS = args.generations
# if args.quit:           QUIT = args.quit
if args.quiet:          QUIET=args.quiet
if args.progress:       PROGRESS_BAR = args.progress
if args.cross:          CROSSOVER_PROB = args.cross
if args.mutation:       MUTATION_PROB = args.mutation
if args.selectionporcent:     SELECTION_PORC = args.selectionporcent
if args.selectionalg:   SELECTION_ALG = args.selectionalg

from pygenetic import genetic

ag = genetic(pop_size = POPSIZE, max_gen = MAX_GENERATIONS, verbose = VERBOSE, porcent_selection=SELECTION_PORC)
ag.run()

# # ag.populate()
# ag.run()
# print(ag)