import wave
import numpy as np
import matplotlib.pyplot as plt

# Ruta del archivo .wav
filename = 'do.wav'

# Abrir el archivo .wav
with wave.open(filename, 'r') as wf:
    # Obtener parámetros del archivo
    n_channels = wf.getnchannels()
    sampwidth = wf.getsampwidth()
    framerate = wf.getframerate()
    n_frames = wf.getnframes()
    
    # Leer los datos del archivo
    audio_data = wf.readframes(n_frames)

# Convertir los datos de bytes a un array de enteros
# Dependiendo del ancho de muestra, puede ser int16 o int8
if sampwidth == 2:
    audio_data = np.frombuffer(audio_data, dtype=np.int16)
elif sampwidth == 1:
    audio_data = np.frombuffer(audio_data, dtype=np.uint8) - 128  # Ajustar el rango de 0-255 a -128 a 127

# Crear un vector de tiempos
time = np.linspace(0, n_frames / framerate, num=n_frames)

# Graficar la forma de onda
plt.figure(figsize=(12, 6))

plt.plot(time, audio_data, color='green')
plt.title('Forma de onda del archivo de audio: ' + str(filename))
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()