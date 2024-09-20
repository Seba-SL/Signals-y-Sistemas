import numpy as np
import matplotlib.pyplot as plt


def unit_step(x):
    return np.where(x >= 0, 1, 0)

n = np.arange(-10, 10)  # Ejemplo de valores de n

signal = (1/7)*np.exp(-3j*np.pi*n/7)*(    np.sin(4*np.pi*n/7)/ np.sin(np.pi*n/7) )

#(1/7) *   exp(-3*j*π*k/7) * sen(4π*k/7)
#                             sen(π*k/7)

# Crear la gráfica
plt.stem(n, signal,label = 'c)' , use_line_collection=True)
plt.xlabel('k')
plt.ylabel('a[k]')
plt.title('Coeficientes de Fourier')
plt.grid(True)
plt.show()

