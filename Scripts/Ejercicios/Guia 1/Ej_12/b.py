import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Definir el rango de n
n = np.arange(-10, 11)  # Puedes ajustar el rango según sea necesario

# Generar la función escalón unitario
u_n = unit_step(n)

# Generar la señal 2n * u(n)
signal = 2 * n * u_n

# Crear la gráfica
plt.stem(n, signal, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Señal 2n * u(n)')
plt.grid(True)
plt.show()

