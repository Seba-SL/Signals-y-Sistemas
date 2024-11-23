import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display

# Cargar el archivo de audio
audio_file = 'InASentimentalMood.wav'
ventana_size = 20480
y, sr = librosa.load(audio_file)

# Configuración del espectrograma
NFFT = int(ventana_size)
overlap = 0.9
noverlap = int(NFFT * overlap)

# Crear el espectrograma
Sxx, freqs, times, im = plt.specgram(y, Fs=sr, NFFT=NFFT, noverlap=noverlap, cmap='viridis', vmin=-110, vmax=-30)

# Configuración del gráfico
plt.ylim(0, 500)
plt.colorbar(label='Intensidad (dB)')
plt.title('Espectrograma: '+ str(audio_file) +', Ventana: ' + str(ventana_size))
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.tight_layout()

# Identificar las frecuencias de mayor intensidad
max_dB_indices = np.argmax(Sxx, axis=0)  # Índices de frecuencias máximas por tiempo
max_dB_values = np.max(Sxx, axis=0)      # Valores máximos en dB por tiempo

# Lista para guardar posiciones ya etiquetadas
etiquetas_posicionadas = []

# Etiquetar las frecuencias en el espectrograma
for t, freq_index in enumerate(max_dB_indices):
    freq_value = freqs[freq_index]
    # Evitar solapamientos
    if max_dB_values[t] > -10:  # Solo etiquetar si está por encima de -30 dB
        # Comprobar si ya hay una etiqueta cercana
        if not any(abs(freq_value - pos) < 10 for pos in etiquetas_posicionadas):
            plt.text(times[t], freq_value, f'{freq_value:.1f} Hz', fontsize=20, ha='center', color='white', verticalalignment='bottom')
            etiquetas_posicionadas.append(freq_value)  # Agregar la frecuencia etiquetada

# Mostrar el gráfico
plt.show()
