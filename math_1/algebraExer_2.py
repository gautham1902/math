import sympy as sym 

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print

# Enable pretty printing in console
init_printing()

q = sym.symbols('q')

eq = 2*q + 3*q**2 - 5/q - 4/(q**3) #PENDAS

pretty_print(eq.simplify())

pretty_print(eq.cancel())