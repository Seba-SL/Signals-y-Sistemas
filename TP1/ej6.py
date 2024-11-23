import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import librosa
import librosa.display

def butterworth_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y


name_file = 'InASentimentalMood.wav'

# Cargar el archivo de audio
fs, data = wavfile.read(name_file)

# Si el archivo tiene más de un canal, seleccionamos uno
if len(data.shape) > 1:
    data = data[:, 0]  # Usa el primer canal

# Aplicar el filtro
cutoff = 500  # Frecuencia de corte en Hz
order = 5  # Orden del filtro
filtered_data = butterworth_filter(data, cutoff, fs, order)

# Guardar el audio filtrado
wavfile.write('audio_filtrado.wav', fs, filtered_data.astype(np.int16))

# Visualizar la señal original y filtrada
plt.figure(figsize=(12, 6))

# Gráfico del audio original
plt.subplot(2, 1, 1)
plt.title('Audio Original')
plt.plot(data)
plt.xlim(0, len(data))

# Gráfico del audio filtrado
plt.subplot(2, 1, 2)
plt.title('Audio Filtrado')
plt.plot(filtered_data)
plt.xlim(0, len(filtered_data))

plt.tight_layout()
plt.show()

# Comparación de espectrogramas
plt.figure(figsize=(12, 8))

# Espectrograma del audio original
plt.subplot(2, 1, 1)
D = librosa.amplitude_to_db(np.abs(librosa.stft(data)), ref=np.max)
librosa.display.specshow(D, sr=fs, x_axis='time', y_axis='log', cmap='coolwarm')
plt.colorbar(format='%+0.0f dB')
plt.title('Espectrograma del Audio Original')

# Espectrograma del audio filtrado
plt.subplot(2, 1, 2)
D_filtered = librosa.amplitude_to_db(np.abs(librosa.stft(filtered_data)), ref=np.max)
librosa.display.spec
