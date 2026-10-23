import sympy as sym 

from sympy import symbols, Eq, init_printing, latex
from sympy.printing.pretty import pretty_print

from sympy.abc import x,y

# Enable pretty printing in console
init_printing()

Fxy = (4 + x) * (2 - y)

numrange = range(0,3)

for xi in numrange:
    for yi in numrange:
        print('When x=%g and y=%g , f(x,y) = %g' %(xi,yi,Fxy.subs({x:xi,y:yi})))

#pretty_print(Fxy.subs({x:1,y:0}))

