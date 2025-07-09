import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def ball_position():
    # declare the integration variable
    t = sp.symbols('t', real=True)
    
    # constant acceleration due to gravity (m s⁻², downward)
    g = -9.81
    
    # user-supplied initial conditions
    p0 = float(input("Original height p₀ (m): "))
    v0 = float(input("Original vertical speed v₀ (m/s): "))
    
    # integrate acceleration to get velocity
    v = sp.integrate(g, t) + v0          # → -9.81*t + v₀
    
    # integrate velocity to get position
    p = sp.integrate(v, t) + p0          # → -4.905*t² + v₀*t + p₀

    t_roots = sp.solve(p, t)
    t_end = max(t_roots)
    
    # pretty output
    print("\nAcceleration a(t) =", g)
    print("Velocity     v(t) =", sp.simplify(v))
    print("Position     p(t) =", sp.simplify(p))

    print(f" The ball hits the ground at t = {t_end}")

    pf=sp.lambdify(t, p, "numpy")
    t_vals = np.linspace(0, float(t_end), 400)
    p_vals = pf(t_vals)

    plt.plot(t_vals, p_vals)
    plt.title("Position(y)")
    plt.xlabel("Time t(s)")
    plt.ylabel("y")
    plt.show()


    # optional: evaluate at t = 2 s
    # print("Height at 2 s:", p.subs(t, 2))

ball_position()