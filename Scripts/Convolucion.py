import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definir las dos señales como funciones
def x(t):
    return np.sin(t)  # Ejemplo: seno

def h(t):
    return  np.cos(t + 2)*np.e # Ejemplo: exponencial decreciente

# Definir la función de convolución
def convolution(t):
    integral, _ = quad(lambda tau: x(tau) * h(t - tau), -np.inf, np.inf)
    return integral

# Definir el rango de tiempo para la evaluación
t = np.linspace(0, 10, 1000)

# Calcular la convolución
y = np.array([convolution(ti) for ti in t])

# Graficar las señales
plt.figure(figsize=(12, 8))

# Graficar la señal x
plt.subplot(3, 1, 1)
plt.plot(t, x(t), label='x(t)')
plt.title('Señal x(t)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

# Graficar la señal h
plt.subplot(3, 1, 2)
plt.plot(t, h(t), label='h(t)', color = 'yellow')
plt.title('Señal h(t)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

# Graficar la señal resultante de la convolución
plt.subplot(3, 1, 3)
plt.plot(t, y, label='y(t) = x(t) * h(t)', color = 'green')
plt.title('Convolución de x(t) y h(t)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()

# Ajustar el diseño
plt.tight_layout()
plt.show()
