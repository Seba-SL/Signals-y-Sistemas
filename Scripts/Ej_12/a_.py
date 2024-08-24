import numpy as np
import matplotlib.pyplot as plt


#a_ cos[(2π/12)*n]

pi = 3.131592

duration = 20
sampling = 1000

time = np.linspace(0,duration , int(sampling*duration) , endpoint = False)

plt.figure(figsize = (12,12) )

plt.plot(2,1,1)
plt.plot(time , np.cos((2*np.pi/12*time)),label = 'a)' , color =  'blue',linewidth = 3)
plt.title('Ejercicio 12 , item a)')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

