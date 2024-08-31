import numpy as np
import matplotlib.pyplot as plt


# Definir el rango de n y k
n = np.arange(1, 100)


def escalon_unitario(n):
    return np.where(n >= 0, 1, 0)


# Sumar las señales a lo largo del eje de k
signal =  (1/pow(2,n)) * escalon_unitario(n)



# Graficar la señal
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura para mejor visualización
plt.stem(n, signal, label='item d) : 2^-n * u(n)', basefmt=" ", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Ej 11 item d)')
plt.grid(True)
plt.legend()
plt.show()
