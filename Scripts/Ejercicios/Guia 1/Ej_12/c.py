import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq


def unit_step(x):
    return np.where(x >= 0, 1, 0)

n = np.arange(-10, 10)  # Ejemplo de valores de n


float_value = float(-1)
power_value = float_value**n
entrada = (power_value)
coef = np.sin(np.pi*n/6)*(3/2)/(12*np.sin(np.pi*n/12) )
signal =  1 + np.cos(np.pi*n) 

transformada_Fourier = fft(signal)

#     a[k] = sen(π*k/6)(3/2)
#             12sen(π*k/12)

#Profe: ak = (1/12) * (1 + 2 * np.cos((np.pi/6) * k))


#(1/7) *   exp(-3*j*π*k/7) * sen(4π*k/7)
#                             sen(π*k/7)

# Crear la gráfica
plt.stem(n, transformada_Fourier,label = 'añ' , use_line_collection=True , linefmt='g', markerfmt='g', basefmt='g')

plt.xlabel('k')
plt.ylabel('ak')
plt.title('Coeficientes de Fourier')
plt.grid(True)
plt.show()

