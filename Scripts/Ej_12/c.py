import numpy as np
import matplotlib.pyplot as plt


def unit_step(x):
    return np.where(x >= 0, 1, 0)

n = np.arange(-10, 10)  # Ejemplo de valores de n

signal = (2.0 ** -n) * unit_step(2 - n)



# Crear la gráfica
plt.stem(n, signal,label = 'c)' , use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Ej 12  item c')
plt.grid(True)
plt.show()

