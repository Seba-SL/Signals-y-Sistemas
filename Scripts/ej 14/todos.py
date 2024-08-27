import numpy as np
import matplotlib.pyplot as plt


#
duration = 20
sampling = 1000

time = np.linspace(-10,duration , int(sampling*duration) , endpoint = False)

n = np.array([-6,-5,-4,-3,-2,-1,0,1, 2, 3, 4, 5])  # Puedes ajustar el rango según sea necesario


plt.figure(figsize = (12,12) )

vector_x = [0,0,0,0,1,2,3,2,2,1,0,0]


def signal_x(x):
    return x;

def heaviside(x):
    return np.where(x >= 0, 1, 0)

def delta_approx(n, index):
    """
    Genera un impulso unitario (delta de Dirac) en la posición dada.
    
    :param n: Array de índices donde evaluar la señal.
    :param index: Posición del impulso unitario (donde será 1).
    :return: Array de la señal delta de Dirac.
    """
    return np.where(n == index, 1, 0)

def signal_c(n):
    if(n > 0):
        return signal_x(n)/2 + (np.power(-1, n)*signal_x(n))/2
    else : return 0

plt.plot(2,1,1)

plt.stem(n , vector_x,label = 'x(n)' ,use_line_collection=True)
#plt.stem(n , vector_x*heaviside(2-n),label = 'a)' ,use_line_collection=True ,  linefmt='-', markerfmt='ro', basefmt='r-')
#plt.stem(n , signal_x(n-1)*delta_approx(n - 3, 0),label = 'b)' ,use_line_collection=True ,  linefmt='-', markerfmt='ro', basefmt='r-')
plt.stem(n , signal_c(n) ,label = 'c)' ,use_line_collection=True ,  linefmt='-', markerfmt='ro', basefmt='r-')
#plt.stem(n , vector_x(3*n+1),label = 'd)' ,use_line_collection=True ,  linefmt='-', markerfmt='ro', basefmt='r-')

plt.title('Ejercicio 14')
plt.xlabel('time [s]')
plt.ylabel('amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


