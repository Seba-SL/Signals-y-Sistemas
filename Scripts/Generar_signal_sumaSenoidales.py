import numpy as np
import matplotlib.pyplot as plt



# Parámetros de la señal
#frecuency_senal = 1/8     # frecuency en Hz
#amplitude_senal = 1         # amplitude de la señal

sampling = 1000            # Número de muestras por segundo
pi = 3.141592 # pi aproximacion
duration = 10               # Duración en segundos
# Crear un vector de time
time = np.linspace(0, duration, int(sampling * duration), endpoint=False)



# Funcion que generara Señal exponencial compleja
def signal_complex_generator(phase,amplitude,frecuency):
    return amplitude*np.sin((2*np.pi*frecuency*time ) + phase )
    
print('Ingrese el nombre se la señal a graficar')

nombre_signal = input()


print('Ingrese la cantidad de senoidales a sumar')

n = input()

# Inicializa la lista con un tamaño adecuado
signal_list = [None]*int(n)  # Asegúrate de que la lista tenga al menos n + 1 elementosPru

# Definir una lista de colores
colors = plt.cm.viridis(np.linspace(0, 1, int(n)))  # Usar el mapa de colores 'viridis'


for i in range(int(n)):
    
    print('Ingrese amplitud de señal ' +  str(i+1) )

    amplitude = input()

    print('Ingrese frecuencia de señal ' +  str(i+1) )

    frecuency = input()


    print('Ingrese fase de señal ' +  str(i+1) )

    phase = input()

    signal_list[i] = signal_complex_generator(float(phase),float(amplitude),float(frecuency) )





# Crear la gráfica
plt.figure(figsize=(10, 6))



# Graficar la señal senoidal
plt.plot(2, 1, 1)
plt.plot(time, sum(signal_list) , label='Señal: '+nombre_signal , color='green' ,linewidth=3 )
plt.title('Señal')
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.grid(True)
plt.legend()


for i in range(int(n)):
  
    # Graficar la señal senoidal
    plt.plot(2, 1, 1)
    plt.plot(time, signal_list[i] , label='señal'+str(i) , color=colors[i],linestyle=':' ,linewidth=1 )
    plt.title('Señales')
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    plt.grid(True)
    plt.legend()


# Mostrar las gráficas
plt.tight_layout()
plt.fill()
plt.show()


