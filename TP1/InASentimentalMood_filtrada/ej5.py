import matplotlib.pyplot as plt
import numpy as np
import librosa

# Cargar el archivo de audio
audio_file = 'filtered_500Hz.wav'  # Cambia esto por la ruta a tu archivo .wav
y, sr = librosa.load(audio_file, sr=None)

# Parámetros de tiempo para el espectrograma
start_time = 0  # Tiempo de inicio en segundos
end_time = 44   # Tiempo de fin en segundos

# Convertir los tiempos a índices
start_index = int(start_time * sr)
end_index = int(end_time * sr)

# Extraer el segmento de interés
y_segment = y[start_index:end_index]

# Parámetros del espectrograma
NFFT = 2048  # Tamaño de la ventana
overlap = 0.9  # Solapamiento
noverlap = int(NFFT * overlap)

# Graficar el espectrograma
figsize = (10, 6)
plt.figure(figsize=figsize)
plt.specgram(y_segment, Fs=sr, NFFT=NFFT, noverlap=noverlap, cmap='viridis', vmin=-110, vmax=-30)
plt.ylim(0, 800)  # Limitar el rango de frecuencia visualizada
plt.colorbar(label='Intensidad (dB)')
plt.title( str(audio_file) + f'Espectrograma con filtro 500Hz ({start_time} a {end_time} segundos)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.tight_layout()
plt.show()

# Análisis para encontrar la frecuencia fundamental en el rango seleccionado
Sxx, frequencies, times, im = plt.specgram(y_segment, Fs=sr, NFFT=NFFT, noverlap=noverlap)
Sxx_mean = np.mean(Sxx, axis=1)  # Promediar en el tiempo

# Encontrar la frecuencia fundamental
fundamental_freq = frequencies[np.argmax(Sxx_mean)]
print(f'Frecuencia fundamental en el rango {start_time}-{end_time}s: {fundamental_freq:.2f} Hz')
