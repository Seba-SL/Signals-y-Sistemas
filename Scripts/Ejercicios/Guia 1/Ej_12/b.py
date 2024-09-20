import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Definir el rango de n
k = np.arange(-2, 4)  # Puedes ajustar el rango según sea necesario

# Generar la función escalón unitario
u_n = unit_step(k)

# Generar la señal 2n * u(n
signal = (1/7)*np.exp(-1j*6*np.pi*k/7)*np.sin(8*np.pi*k/7)/ np.sin(2*np.pi*k/7) 


# Crear la gráfica
plt.stem(k, signal, use_line_collection=True)
plt.xlabel('k')
plt.ylabel('a(k)')
plt.title('Coeficientes de Fourier')
plt.grid(True)
plt.show()

