import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Parámetros
duration = 10
sampling = 100
time = np.linspace(-duration, duration, int(sampling * duration), endpoint=False)

# Funciones
def escalon(t):
    return np.where(t > 0, 1, 0)

def x(t):
    return escalon(t - 1) * np.sin(t)

def h(t):
    return escalon(t) - 2 * escalon(t - 2) + escalon(t - 5)

# Define la función de convolución
def convolution_integrand(tau, t):
    return x(tau) * h(t - tau)

# Define la convolución usando integración numérica
def convolution(t):
    result, _ = quad(convolution_integrand, -duration, duration, args=(t,))
    return result

# Vectoriza la función de convolución para todo el rango de tiempo
convolution_vectorized = np.vectorize(convolution)

# Crear la figura
plt.figure(figsize=(8, 12))

# Graficar la primera señal
plt.subplot(3, 1, 1)
plt.plot(time, x(time), 'r', label='x(t)')
plt.title('x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

# Graficar la segunda señal
plt.subplot(3, 1, 2)
plt.plot(time, h(time), 'g', label='h(t)')
plt.title('h(t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.legend()

# Graficar la tercera señal
plt.subplot(3, 1, 3)
plt.plot(time, convolution_vectorized(time), 'b', label='x(t)⋆h(t)')
plt.title('x(t)⋆h(t)')
plt.xlabel('t')
plt.ylabel('x(t)⋆h(t)')
plt.legend()





# Ajustar el layout para que no se solapen los gráficos
plt.tight_layout()

# Mostrar los gráficos
plt.show()
