import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# --- data ---
x      = np.linspace(0, 6*np.pi, 1000)
cos_x  = np.cos(x)          # predefined as requested
sin_x  = np.sin(x)
y = 0

# --- plot ---
plt.plot(x, cos_x, color = "green", label = 'cos(x)')
plt.plot(x, sin_x, color = "blue",  label = 'sin(x)')
plt.plot(x, y, color='black')

# --- π-spaced x-ticks ---
ticks = np.pi * np.arange(0, 7)            # 0, π, 2π, …, 6π
plt.xticks(ticks)
plt.gca().xaxis.set_major_formatter(
    FuncFormatter(lambda v, _: '0' if v == 0 else rf'{v/np.pi:.0g}π')
)

plt.xlim(0, 6*np.pi)        # remove auto-padding so ticks align
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()