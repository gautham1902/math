
import math

from IPython.display import display,Math
from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print


# Enable pretty printing in console
init_printing(use_unicode=True)

a = 4
b = 5

numGcd =math.gcd(a,b)
display(Math('\\frac{a}{b} = \\frac{a\\times c}{b\\times c}'))
