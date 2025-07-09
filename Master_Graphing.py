import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

t = sp.symbols('t')

def gravity():
    
    while True:
        planet = input("Press 'p' for pluto, 'e' for earth, 'm' for mars, 's' for saturn, 'v' for venus, 'me' for mercury, 'n' for neptune: ").lower().strip()
    
        planet_options = {
        'p': ("Pluto",-0.62),
        'e': ("Earth",-9.81),
        'm': ("Mars",-3.71),
        's': ("Saturn",-10.4),
        'v': ("Venus", -8.87),
        'me': ("Mercury", -3.7),
        'n': ("Neptune", -11.15)
        }

        planet_tuple = planet_options.get(planet)
    
        if planet_tuple is None:
            print("Aliens!!! Try p, e, m, me, n, v or s.")
        else:
            break

    planet_name, g = planet_tuple
    
    print(f"g on that body = {g} m/s^2")
    return planet_name, g

def jump_velocity():
    max_height_earth = float(input("How high can you jump in meters: "))
    #initial vertical velocity formula: sqrt(2g(max height))
    v_o = math.sqrt(2*9.81*max_height_earth)
    return max_height_earth, v_o

def height_as_a_function_of_time():

    planet_name, g_other = gravity()
    max_height_earth, v_o = jump_velocity()
    max_height_other = math.fabs((v_o ** 2) / (2*g_other))
    p_o = float(input("Enter start height, recomended start height is 0. Start height: "))

    v_of_t = sp.integrate(g_other, t) + v_o
    p_of_t = sp.integrate(v_of_t, t) + p_o

    print(f"Acceleration on {planet_name} is a constant {g_other} (m/s^2). If on Earth you can jump {max_height_earth} m, then on {planet_name} you can jump {max_height_other} m. With an inital velocity, and position of {v_o} (m/s) and {p_o} m repectively your position is given by f(t) = {p_of_t}")

    return p_of_t

def graph_height():
    p_of_t = height_as_a_function_of_time()
    height_graph = sp.lambdify(t, p_of_t, "numpy")


    t_max = float(max(sp.solve(p_of_t, t)))
    num_of_t_points = math.ceil(t_max*100)
    t_vals = np.linspace(0, t_max, num=num_of_t_points)
    height_vals = height_graph(t_vals)

    plt.plot(t_vals, height_vals)
    plt.title("Height on your planet of choice")
    plt.xlabel("time (s)")
    plt.ylabel("height (m)")
    plt.show()

graph_height()
