import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de tiempo
t = np.linspace(-2, 2, 1000)

# Definir la señal x(t)
x_t = -(1j / np.sqrt(2)) * np.exp(-np.pi * t*1j) + (1j / np.sqrt(2)) * np.exp(np.pi * t*1j)

# Obtener la parte real e imaginaria para graficar
real_part = np.real(x_t)
imag_part = np.imag(x_t)

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(t, real_part, label='Parte Real', color='blue')
plt.plot(t, imag_part, label='Parte Imaginaria', color='red')
plt.title('Señal x2(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('x(t)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()
