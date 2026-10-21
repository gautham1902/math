import sympy as sym 
from IPython.display import display,Math

x = sym.symbols('x')

expr = 2*x + 4 - 9

sym.solve(expr) #display tp print solve output

#display(sym.latex(sym.solve(expr)))
display(Math('\\text{The solution is } %s \\text {is x=} %g' %(sym.latex(expr),sym.solve(expr)[0])))

y = sym.symbols('y')

expr = x/4 - x*y + 5

display(sym.solve(expr,x))#pass 2nd param to solve for which value
