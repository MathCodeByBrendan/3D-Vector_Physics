from sympy import *
from sympy.physics.mechanics import *
init_vprinting()

# define symbols
m, g, k, t = symbols('m g k t')
x = dynamicsymbols('x')

# take derivatives
x_dot = diff(x, t)
x_ddot = diff(x_dot, t)

# Lagrangian
T = 0.5 * m * x_dot**2
V =  -m*g*x + 0.5 * k * x**2
L = T - V

# Solve Euler-Lagrange
eqn = diff((L, x_dot), t, 2)
sln = solve(eqn, x_ddot)[0]
print(Eq(x_ddot, sln))