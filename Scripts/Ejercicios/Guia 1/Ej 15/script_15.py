import numpy as np
import matplotlib.pyplot as plt

def x(n):
    """Ejemplo de función x(n). Debe ser definida según el problema específico."""
    # Ejemplo de definición de x(n). Ajusta según tu señal específica.
    n = np.asarray(n)
    result = np.zeros_like(n, dtype=float)
    result[np.logical_or(n == -2, n == 3)] = 1
    result[n == 0] = 3
    result[np.logical_or(np.logical_or(n == -1, n == 1), n == 2)] = 2
    return result

def y1(n, N0):
    """Calcula y1(n) = x(N0 * n)"""
    n = np.asarray(n)
    return x(N0 * n)

def y2(n, N0):
    """Calcula y2(n) = x(n / N0) si n es múltiplo de N0, de lo contrario 0"""
    n = np.asarray(n)
    # Verificar si n es múltiplo de N0
    is_multiple = (n % N0 == 0)
    # Calcular valores de y2
    y2_values = np.where(is_multiple, x(n // N0), 0)
    return y2_values

# Ejemplo de uso
N0 = 2
n = np.arange(-10, 11)  # Rango de valores para n

# Calcular y1(n) y y2(n)
y1_values = y1(n, N0)
y2_values = y2(n, N0)

# Mostrar resultados
print("y1(n):", y1_values)
print("y2(n):", y2_values)


# Graficar la señal
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura para mejor visualización
plt.stem(n, y2_values, label='y2',markerfmt='g', basefmt='g-', use_line_collection=True)
plt.stem(n, y1_values, label='y1',markerfmt='r', basefmt='r-', use_line_collection=True)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Ej 12 item h')
plt.grid(True)
plt.legend()
plt.show()