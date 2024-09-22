import numpy as np
import matplotlib.pyplot as plt


def unit_step(x):
    return np.where(x >= 0, 1, 0)

n = np.arange(-10, 10)  # Ejemplo de valores de n


float_value = float(-1)
power_value = float_value**n
entrada = (power_value)
signal = (power_value)*(1/(4-1j*np.pi)   + 1/(4+1j*np.pi ) )

#(1/7) *   exp(-3*j*π*k/7) * sen(4π*k/7)
#                             sen(π*k/7)

# Crear la gráfica
plt.stem(n, entrada,label = '' , use_line_collection=True , linefmt='g', markerfmt='g', basefmt='g')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('entrada del Sistema')
plt.grid(True)
plt.show()

