import numpy as np
import matplotlib.pyplot as plt

# Definimos el tiempo
t = np.linspace(-2, 5, 1000)

# Definimos la señal u(t) (escalón unitario)
u = np.heaviside(t, 1)

# Definimos h(t) = (1/t) * u(t-1)
h = (1/t) * np.heaviside(t-1, 1)

# Manejo del valor en t=0 para h(t)
h[t == 0] = 0  # Asignamos 0 cuando t=0 para evitar indefinición

# Calculamos la convolución
# Usamos 'same' para que la salida tenga la misma longitud que la entrada
convolution = np.convolve(u, h, mode='same') * (t[1] - t[0])  # Escalar por el paso de tiempo

# Graficamos las señales y su convolución
plt.figure(figsize=(15, 10))

# Grafica u(t)
plt.subplot(3, 1, 1)
plt.plot(t, u, label='$u(t)$ (escalón unitario)', color='blue')
plt.title('Señal u(t)')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()

# Grafica h(t)
plt.subplot(3, 1, 2)
plt.plot(t, h, label='$h(t) = \\frac{1}{t}u(t-1)$', color='red')
plt.title('Señal h(t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.ylim(-1, 1)  # Ajustamos el límite del eje y para una mejor visualización
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()

# Grafica la convolución
plt.subplot(3, 1, 3)
plt.plot(t, convolution, label='Convolución $u(t) * h(t)$', color='green')
plt.title('Convolución de $u(t)$ y $h(t)$')
plt.xlabel('t')
plt.ylabel('Convolución')
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()

# Mostramos las gráficas
plt.tight_layout()
plt.show()
