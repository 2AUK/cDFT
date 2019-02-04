import numpy as np

#Global constants
T = 300.0 #K
Na = 6.022E23 #mol^-1
kb = 1.38065E-26 #kJ/K
B = 1.0 / Na * kb * T #kJ/mol

#Grid constants
pts = 100.0
gridmax = 15.0 #A
dx  = gridmax / pts - 1.0

def grid(max_grid, dx):
    return np.arange(0, max_grid, dx)

def LJ():
    pass

def solvent_density():
    pass

def analytical_functional_solve():
    pass

