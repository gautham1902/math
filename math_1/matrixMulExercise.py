import sympy as sym 
import numpy as np

from sympy.printing.pretty import pretty_print

xyset = range(0,10)

mat = np.zeros([len(xyset),len(xyset)],dtype = int)


for rowi in xyset:
    for coli in xyset:
        mat[rowi,coli] = (rowi+1) * (coli+1)
        

pretty_print(sym.simplify(sym.sympify(mat)))
