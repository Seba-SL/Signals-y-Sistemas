import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
duracion = 10  # Duración total de la señal en segundos
t = np.linspace(-10, duracion, 1000)  # Vector de tiempo

# Función escalón unitario u(t + 3)
u_t_plus_3 = np.heaviside(t + 2, 1)

# Señal x(t)
x_t = np.exp(-5 * t) * u_t_plus_3

# Graficar la señal
plt.figure(figsize=(12, 4))
plt.plot(t, x_t, label='$x(t) = e^{-5t} \cdot u(t + 2)$', color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Gráfico de la señal $x(t) = e^{-5t} \cdot u(t + 2)$')
plt.grid(True)
plt.legend()
plt.show()
