import sympy as sym 

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print

from sympy.abc import x,y

# Enable pretty printing in console
init_printing()

term1 = (4*x + 5)
term2 = x

pretty_print( sym.expand(term1 * term2))

term3 = x - 7

pretty_print (sym.expand (term1 * term3))

expr = x*(2*y**2 - 5**x/x)

pretty_print(sym.expand(expr))

#%whos will list all variable and module imported