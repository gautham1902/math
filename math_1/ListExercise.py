import sympy as sym 
import numpy as np
from sympy.abc import x,y

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print


# Enable pretty printing in console
init_printing()

e1 = 2*x + x*(4-6*x) + x
e2 = -x*(2/x + 4/x**2) + (4+x) / (4*x)
e3 = (x+3)*(x-3) *x *(1/(9*x))

    
alist = [(e1),(e2),(e3)]

for i in alist:
    pretty_print((sym.expand(i)))

