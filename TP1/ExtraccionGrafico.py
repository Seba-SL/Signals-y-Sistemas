import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Ruta del archivo .wav
archivo_wav = 'mi.wav'

# Leer el archivo .wav
frecuencia_muestreo, datos = wavfile.read(archivo_wav)

# Crear un array de tiempos en segundos
tiempo = np.arange(len(datos)) / frecuencia_muestreo

# Crear la gráfica
plt.figure(figsize=(12, 6))
plt.plot(tiempo, datos, label='Amplitud', color = 'yellow')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Forma de onda del archivo de audio: ' + str(archivo_wav) )
plt.legend()
plt.grid(True)
plt.show()
