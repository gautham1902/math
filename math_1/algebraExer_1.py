import sympy as sym 

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print

# Enable pretty printing in console
init_printing()

q = sym.symbols('q')

eq = 3*q + 4/q +3 - 5*q - 1/q - 1

#display(Math(sym.latex(eq)))


# Pretty print in console
pretty_print(eq.simplify())   # FURTHER SIMPLY

pretty_print(sym.solve(eq,q))

