import numpy as np
import matplotlib.pyplot as plt

# Definir la función sinusoidal
def f(x):
    return np.sin(x)

# Definir el rango y la cantidad de rectángulos
x_min, x_max = 0, 2 * np.pi  # Rango completo
num_rectangles = 50  # Número de rectángulos

# Calcular los puntos para graficar la función
x = np.linspace(x_min, x_max, 1000)
y = f(x)

# Calcular los rectángulos de Riemann
x_rectangles = np.linspace(x_min, x_max, num_rectangles + 1)
y_rectangles = f(x_rectangles[:-1])  # Altura de los rectángulos (evaluada en los puntos a la izquierda)

# Definir el ancho de los rectángulos
width = (x_max - x_min) / num_rectangles

# Graficar la función sinusoidal
plt.plot(x, y, label='sin(x)')

# Graficar los rectángulos de Riemann
for i in range(num_rectangles):
    plt.bar(x_rectangles[i], y_rectangles[i], width=width, align='edge', alpha=0.3, edgecolor='black')

# Configurar la gráfica
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Riemann Rectangles for sin(x)')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
