import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

G = -9.81

def height():
    t = sp.symbols("t", real = True)

    h_o = float(input("How high are you: "))
    v_o = float(input("How fast are you: "))

    v = sp.integrate(G,t)+v_o
    p =(sp.integrate(v, t) + h_o)
    
    t_end = max(sp.solve(p, t))
    pf = sp.lambdify(t, p,"numpy")
    t_vals = np.linspace(0, float(t_end), 400)
    p_vals = pf(t_vals)

    plt.plot(t_vals, p_vals)
    plt.title("Position(y)")
    plt.xlabel("Time t(s)")
    plt.ylabel("y")
    plt.show()

height()
