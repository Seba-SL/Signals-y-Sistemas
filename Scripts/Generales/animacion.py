import numpy as np
import matplotlib.pyplot as plt

# Definimos la función u(t) y x(t)
def u(t):
    return np.where(t >= 0, 1, 0)

def x(t):
    return u(t) - t

# Generamos el rango de t
t = np.linspace(-2, 2, 400)  # Rango de -2 a 2

# Calculamos x(t)
xt = x(t)

# Graficamos
plt.figure(figsize=(8, 4))
plt.plot(t, xt, label='$x(t) = u(t) - t$', color='blue')
plt.title('Gráfica de $x(t) = u(t) - t$')
plt.xlabel('t')
plt.ylabel('$x(t)$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.ylim(-2, 2)
plt.xlim(-2, 2)
plt.legend()
plt.show()
