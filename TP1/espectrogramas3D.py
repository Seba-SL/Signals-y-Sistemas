import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.io import wavfile
from scipy.signal import spectrogram

# Cargar el archivo WAV
file = 'Zombie.wav'
sample_rate, data = wavfile.read(file)

# Asegurarse de que los datos son unidimensionales
if len(data.shape) > 1:
    data = data[:, 0]  # Usar solo un canal si es estéreo

# Definir un intervalo de tiempo
start_time = 0  # en segundos
end_time = 44   # en segundos

# Convertir el tiempo a índices
start_index = int(start_time * sample_rate)
end_index = int(end_time * sample_rate)

# Extraer el intervalo de la señal
interval_signal = data[start_index:end_index]

# Calcular el espectrograma
f, t, Sxx = spectrogram(interval_signal, sample_rate, nperseg=2048, noverlap=1024)

# Crear la figura 3D
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar el espectrograma en 3D
X, Y = np.meshgrid(t, f)
ax.plot_surface(X, Y, 10 * np.log10(Sxx + 1e-10), cmap='plasma', edgecolor='none')

# Etiquetas y título
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Frecuencia (Hz)')
ax.set_zlabel('Intensidad (dB)')
ax.set_title(f'Espectrograma 3D: {start_time} s a {end_time} s')
ax.view_init(elev=30, azim=150)  # Ajustar el ángulo de vista

plt.show()
