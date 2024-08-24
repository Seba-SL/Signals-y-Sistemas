import numpy as np
import matplotlib.pyplot as plt

# Definir la función escalón de Heaviside
def heaviside(x):
    return np.where(x >= 0, 1, 0)

def delta_approx(x, epsilon=0.01):
    return np.exp(-x**2 / (2 * epsilon**2)) / (epsilon * np.sqrt(2 * np.pi))


# Crear un rango de valores para x
x = np.linspace(-5, 5, 1000)

# Calcular los valores de la función escalón y la aproximación de delta de Dirac
heaviside_values = heaviside(-2*x+3) - heaviside(-2*x -3)
delta_values = delta_approx(x)


# Crear la gráfica
plt.figure(figsize=(12 , 12))

# Graficar la función escalón
plt.plot(1, 2, 1)
plt.plot(x, 3*delta_values , label='Función Escalón de Heaviside')
plt.title('Función Escalón de Heaviside')
plt.xlabel('x')
plt.ylabel('Heaviside(x)')
plt.grid(True)
plt.legend()



# Mostrar las gráficas
plt.tight_layout()
plt.show()
