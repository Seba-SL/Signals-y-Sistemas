import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-100,100)

signal = np.cos(n/6)


plt.stem(n , signal , label = 'c)',use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()