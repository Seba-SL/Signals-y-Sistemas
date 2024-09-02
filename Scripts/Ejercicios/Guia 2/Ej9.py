# 9. Resolver en sus variantes discreta y continua los siguientes enunciados:
# (a) Dado un sistema LTI en tiempo discreto con una respuesta al impulso h(n) = αn u(n) con
# α < 1, encontrar la salida del sistema para cada una de las siguientes entradas:
# (i) x(n) = δ(n) − δ(n − 1)
# (ii) x(n) = u(n) − u(n − 5)

import numpy as np
import matplotlib.pyplot as plt

# Genero el rango de evaluación
n = np.arange(-10,11)

alfa = 0.5

def escalon(n):
    return np.where(n >= 0,1,0)


def h(n):
    return pow(alfa,n)*escalon(n)

def x(n):
    return escalon(n) - escalon(n - 5)


# Evaluar las funciones en el rango definido
h_vals = h(n)
x_vals = x(n)

# Realizar la convolución
y_vals = np.convolve(h_vals,x_vals, mode='full')

# Ajustar el rango para la salida de la convolución
n_y = np.arange(n[0] + n[0], n[-1] + n[-1] + 1)



plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura para mejor visualización



# Primer gráfico (subplot 1,1,1 es la posición 1 en una cuadrícula 1x1)
plt.subplot(3, 1, 1)
plt.stem(n, h(n), label='h(n) , α = ' + str(alfa), basefmt=" ", use_line_collection=True)
plt.title('h[n]  ,   α ='+ str(alfa))

# Segundo gráfico (subplot 1,1,2 es la posición 2 en una cuadrícula 1x1)
plt.subplot(3, 1, 2)
plt.stem(n, x(n), label='x(n)', basefmt=" ", linefmt = 'black', markerfmt = 'g', use_line_collection=True)
plt.title('x[n]')

# Tercer gráfico (subplot 1,1,3 es la posición 3 en una cuadrícula 1x1)
plt.subplot(3, 1, 3)

plt.stem(n_y, y_vals, label='x(n) * h(n)', basefmt=" ", linefmt='yellow', markerfmt='yo')
plt.title('y[n]')



plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Ej 9 ')
plt.grid(True)
plt.legend()

# Ajustar el diseño para evitar superposición de etiquetas
plt.tight_layout()

plt.show()





