import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-10,10)

signal = np.sin(20*np.pi*n)


plt.stem(n , signal , label = 'c)')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()