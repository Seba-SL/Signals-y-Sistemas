import numpy as np
import matplotlib.pyplot as plt

# Definimos la función escalón unitario
def u(t):
    return np.where(t >= 0, 1, 0)

# Parámetros de la señal
duracion = 10  # Duración total de la señal en segundos
t = np.linspace(0, duracion, 1000)  # Vector de tiempo

# Inicializamos la señal
x = np.zeros_like(t)

# (u(t−2k)−u(t−2k−1))−2⋅(u(t−2k−1)−u(t−2k−2))]
# Calculamos la señal sumando los términos de la serie
for k in range(-10, 11):  # Usamos un rango finito para la suma infinita
    x += u(t - 2*k) - u(t - 1 - 2*k)

# Graficamos la señal
plt.figure(figsize=(12, 4))
plt.plot(t, x, label='$x(t) = \sum_{k=-\infty}^{\infty} [u(t - 2k) - u(t - 1 - 2k)]$', color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Gráfico de la función $x(t)$')
plt.grid(True)
plt.legend()
plt.show()
