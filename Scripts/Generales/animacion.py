import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de omega
omega = np.linspace(-10, 10, 1000)

# Inicializar X(jω)
X = np.zeros_like(omega, dtype=complex)

# Evaluar la suma para k = -10 a 10 (puedes ajustar este rango)
for k in range(-10, 11):
    if k != 0:  # Evitar k = 0
        delta_w = k * (2 * np.pi / 6)
        X += (2 * np.sin(3 * delta_w) / k) * np.exp(-1j * omega * (3/2)) * (omega == delta_w)

# Graficar el módulo de X(jω)
plt.figure(figsize=(10, 5))
plt.plot(omega, np.abs(X), label='|X(jω)|')
plt.title('Espectro de frecuencia')
plt.xlabel('Frecuencia (ω)')
plt.ylabel('|X(jω)|')
plt.grid()
plt.legend()
plt.show()
