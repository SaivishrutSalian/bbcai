from __future__ import print_function
from simpleai.search import CspProblem, backtrack, min_conflicts
from simpleai.search import MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')
domains = dict((v, ['red', 'green', 'blue']) for v in variables)

def const_different(variables, values):
    return values[0] != values[1]

constraints = [
    (('WA', 'NT'), const_different),
    (('WA', 'SA'), const_different),
    (('SA', 'NT'), const_different),
    (('SA', 'Q'), const_different),
    (('NT', 'Q'), const_different),
    (('SA', 'NSW'), const_different),
    (('Q', 'NSW'), const_different),
    (('SA', 'V'), const_different),
    (('NSW', 'V'), const_different)
]

my_problem = CspProblem(variables, domains, constraints)


print("Solution without heuristics:")
print(backtrack(my_problem))

print("\nSolution with MOST_CONSTRAINED_VARIABLE heuristic:")
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))

print("\nSolution with HIGHEST_DEGREE_VARIABLE heuristic:")
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))

print("\nSolution with LEAST_CONSTRAINING_VALUE heuristic:")
print(backtrack(my_problem, variable_heuristic=LEAST_CONSTRAINING_VALUE))

print("\nSolution with MOST_CONSTRAINED_VARIABLE and LEAST_CONSTRAINING_VALUE heuristics:")
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))

print("\nSolution with HIGHEST_DEGREE_VARIABLE and LEAST_CONSTRAINING_VALUE heuristics:")
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))

print("\nSolution using min_conflicts:")
print(min_conflicts(my_problem))
