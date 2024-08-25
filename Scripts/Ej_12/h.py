import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de n y k
n = np.arange(1, 100)
k = np.arange(1, 50)

# Crear una matriz para almacenar las señales
signal_matrix = np.zeros((len(n), len(k)))

# Calcular la señal para cada valor de k y almacenar en la matriz
for i in range(len(k)):
    signal_matrix[:, i] = (1 / (np.pi * k[i])) * np.sin(np.pi * k[i] / 4) * np.cos(np.pi * k[i] * n / 32)

# Sumar las señales a lo largo del eje de k
signal = np.sum(signal_matrix, axis=1)

# Graficar la señal
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura para mejor visualización
plt.stem(n, signal, label='item g) 0 < k < 50: ⅀ Re(g(k,n))', basefmt=" ", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Ej 12 item h')
plt.grid(True)
plt.legend()
plt.show()
