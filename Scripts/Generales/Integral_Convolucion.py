import numpy as np
import matplotlib.pyplot as plt


def escalon(x):
    return np.where(x >= 0, 1, 0)


# Definir las señales
t = np.linspace(-500   , 500, 1000)  # Tiempo
x = np.sin(np.pi*t/3)          # Señal 1: función gaussiana
h = escalon(t) - escalon(t-6) + 3*escalon(t-12) # Señal 2: seno

# Convolución
y = np.convolve(x, h, mode='same') * (t[1] - t[0])

# Graficar señales
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Señal x(t)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, h)
plt.title('Señal h(t)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, y)
plt.title('Convolución y(t)')
plt.grid(True)

plt.tight_layout()
plt.show()



