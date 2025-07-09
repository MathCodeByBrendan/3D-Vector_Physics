import math
import numpy as np

def print():
    print("Hello World.")

def moment_math():

    # get vect. u & v
    a = list(map(float, input("Enter the position vector:").split()))
    b = list(map(float, input("Enter the force vector:").split()))
    c = list(map(float, input("Enter the axis vector:").split()))
    # convert axis vector into unit vector
    axis_mag = np.linalg.norm(c)
    unit_axis = c / axis_mag
    # print unit axis conversion
    print(f"The unit axis vector is given by u = < {unit_axis[0]: .2f} , {unit_axis[1]:.2f} , {unit_axis[2]:.2f} ." )
    # determine moment about unit axis
    normal_ab = np.cross(a, b)
    print(f"The moment is {normal_ab}.")
    Moment_about_unit_axis = np.dot(normal_ab, unit_axis)
    print("The moment the unit axis is", Moment_about_unit_axis, ".")

print()

moment_math()

