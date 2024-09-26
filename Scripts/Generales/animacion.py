import numpy as np
import matplotlib.pyplot as plt


# Definir el rango de frecuencias
frequencies = np.linspace(-10, 10, 1000)



# Definir la función compleja
def f(f):
    return  np.e**(1j*frequencies)/(-1-1j*frequencies)  -  np.e**(-1 - 1j*frequencies)/(-1-1j*frequencies)

values = f(frequencies)


#  -  exp(jw)    +   exp(-1-jw)       
#    (-1-jw)              (-1-jw)

# Graficar la parte real y la parte imaginaria
plt.figure(figsize=(50, 10))
#plt.plot(frequencies, values.real, label='Parte Real', color='blue')
#plt.plot(frequencies, values.imag, label='Parte Imaginaria', color='red')
plt.plot(frequencies, np.abs(values), label='Magnitud', color='green')
plt.title('|X(jw)|')
plt.xlabel('Frecuencia (f)')
plt.ylabel('Valor de la función')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.xlim(-4, 4)
plt.ylim(-0.8, 0.8)
plt.show()
