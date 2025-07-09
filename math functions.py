import sympy as sp, numpy as np

t = sp.symbols('t')

def square_roots():
    a, b, c = map(float, input("Enter a, b, c: ").split())
    f = a*t**2 + b*t + c
    square_roots = sp.solve(f, t)
    print(f"Square roots are: {square_roots}")

def matrix_solver():
    selected_vars = input("What are the variables in your equations. Input them in them in order: ").split()
    variables = []
    for _ in range(len(selected_vars)):
        supported_var = sp.symbols(selected_vars[_])
        variables.append(supported_var)
    sol = sp.solve((variables[0])+1, variables[0])
    print(f"{selected_vars[0]} = {sol}")

