import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-2,10)

def escalon_unitario(n):
    return np.where(n >= 0, 1, 0)

signal = np.cos(np.pi*n/3)*escalon_unitario(n - 2)


plt.stem(n , signal , label = 'd)',use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()