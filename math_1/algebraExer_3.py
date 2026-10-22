import sympy as sym 

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print

# Enable pretty printing in console
init_printing()

q = sym.symbols('q')

expr = (sym.sqrt(3) + sym.sqrt(15) * q) / (sym.sqrt(2) + sym.sqrt(10) * q)

pretty_print(expr)

pretty_print(expr.subs(q,3).evalf())