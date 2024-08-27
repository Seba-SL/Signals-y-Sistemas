import numpy as np
import matplotlib.pyplot as plt

def signal_x(n):
    # Convertir n a un array si no lo es
    n = np.asarray(n)
    
    # Inicializar un array de ceros
    result = np.zeros_like(n, dtype=float)
    
    # Aplicar las condiciones de la función
    result[np.logical_or(n == -2, n == 3)] = 1
    result[n == 0] = 3
    result[np.logical_or(np.logical_or(n == -1, n == 1), n == 2)] = 2
    
    return result

def signal_c(n):
    n = np.asarray(n, dtype=float)  # Convertir n a tipo float
    return signal_x(n)/2 + (np.power(-1, n) * signal_x(n))/2


# Crear un rango de valores para n
n = np.arange(-5, 6)  # Incluye 5 en el rango

vector_x = signal_x(n)
vector_c = signal_c(n)

plt.figure()
#plt.stem(n, vector_x, label='x(n)', linefmt='-', markerfmt='ro', basefmt='r-', use_line_collection=True)
#plt.stem(n, vector_c, label='c)', linefmt='--', markerfmt='g', basefmt='g-', use_line_collection=True)
plt.stem(n, signal_x(3*n + 1 ), label='d)', linefmt='-', markerfmt='g', basefmt='g-', use_line_collection=True)
plt.legend()
plt.show()
