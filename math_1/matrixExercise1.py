import sympy as sym 
import numpy as np

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print

from sympy.abc import x,y


Fxy = (4 + x) * (2 - y)

xyset = range(0,3)

mat = np.zeros([len(xyset),len(xyset)])


for rowi in xyset:
    for coli in xyset:
        mat[rowi,coli] = Fxy.subs({x:rowi,y:coli})

pretty_print(sym.simplify(mat))
