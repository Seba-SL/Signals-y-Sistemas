import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Definir el rango de n
k = np.arange(-10, 10)  # Puedes ajustar el rango según sea necesario

# Generar la función escalón unitario
u_n = unit_step(k)

# Generar la señal 2n * u(n
signal = (1/6)*np.exp(-1j*np.pi*k/2)*(    np.sin(2*np.pi*k/3)/ np.sin(np.pi*k/6) )

#  exp(-j*π*k/2) * sen(2π*k/3)
   #                      sen(π*k/6)
# Crear la gráfica
plt.stem(k, signal, use_line_collection=True)
plt.xlabel('k')
plt.ylabel('a(k)')
plt.title('Coeficientes de Fourier')
plt.grid(True)
plt.show()

