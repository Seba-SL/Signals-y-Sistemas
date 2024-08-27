import numpy as np
import matplotlib.pyplot as plt


#a_ cos[(2π/12)*n]

duration = 20
sampling = 1000

time = np.linspace(-10,duration , int(sampling*duration) , endpoint = False)

plt.figure(figsize = (12,12) )

def heaviside(x):
    return np.where(x >= 0, 1, 0)


def signal(time):
    return 1/pow(np.e,5*time) *heaviside(time + 2 )

signal_par = (signal(time) + signal(-time))/2


signal_impar = (signal(time)  -signal(-time))/2


plt.plot(2,1,1)
plt.plot(time , signal(time),label = 'd)' , color =  'blue',linewidth = 3)
plt.plot(time , signal_par  ,label = 'par parte' , color =  'red',linewidth = 3)
plt.plot(time , signal_impar  ,label = 'impar parte' , color =  'orange',linewidth = 3)
plt.title('Ejercicio 9 , item d)')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


