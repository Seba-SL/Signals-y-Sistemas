import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Cargar el archivo WAV
filename = 'filtered_2000Hz.wav'  # Reemplaza con el nombre de tu archivo WAV
sample_rate, data = wavfile.read(filename)

# Si el archivo tiene más de un canal, seleccionamos uno
if len(data.shape) > 1:
    data = data[:, 0]  # Usar solo el primer canal

# Crear un eje de tiempo en segundos
duration = len(data) / sample_rate
time = np.linspace(0, duration, len(data))

# Graficar la señal de audio
plt.figure(figsize=(12, 6))
plt.plot(time, data,color="green")
plt.title('Señal de Audio:'+str(filename))
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0, duration)
plt.grid()
plt.show()
