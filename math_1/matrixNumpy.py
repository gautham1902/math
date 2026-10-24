import sympy as sym 
import numpy as np

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print


A = np.array([[1,2],[3,4]])

mat = np.zeros([4,7])

numrange = range(0,4)
numrange2 = range(0,7)

for rowi in numrange:
    for coli in numrange2:
        mat[rowi,coli] = (-1)**(rowi+coli)

pretty_print(sym.simplify(mat))
