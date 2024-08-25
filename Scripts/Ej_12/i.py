import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de n y k
n = np.arange(-100, 100)
k = np.arange(0, 50)

# Crear una matriz para almacenar las señales
signal_matrix = np.zeros((len(n), len(k)))

# Calcular la señal para cada valor de k y almacenar en la matriz
for i in range(len(k)):
    signal_matrix[:, i] = np.cos(np.pi *(10*np.tan(3*np.pi*k[i]/400)) * n /2)

# Sumar las señales a lo largo del eje de k
signal = np.sum(signal_matrix, axis=1)

# Graficar la señal
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura para mejor visualización
plt.stem(n, signal, label='item g) 0 < k < 50: ⅀ g(k,n)', basefmt=" ", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Ej 12 item i')
plt.grid(True)
plt.legend()
plt.show()