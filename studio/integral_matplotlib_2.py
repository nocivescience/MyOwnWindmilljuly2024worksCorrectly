import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

x_min, x_max = 0, 2 * np.pi
num_rectangles = 50

x=np.linspace(x_min, x_max, 1000)
y=f(x)

x_rectangles=np.linspace(x_min, x_max, num_rectangles + 1)
y_rectangles=f(x_rectangles[:-1]) # Altura de los rectángulos (evaluada en los puntos a la izquierda)

width=(x_max - x_min) / num_rectangles

plt.plot(x, y, label='sin(x)')

for i in range(num_rectangles):
    plt.bar(x_rectangles[i], y_rectangles[i], width=width, align='edge', alpha=0.3, edgecolor='black')

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Riemann Rectangles for sin(x)')
plt.legend()
plt.grid(True)

plt.show()