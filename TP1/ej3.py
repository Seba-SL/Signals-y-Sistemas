import numpy as np #type: ignore
import soundfile as sf #type: ignore
import matplotlib.pyplot as plt #type: ignore

audio_file = 'InAsentimentalMood.wav'
data, samplerate = sf.read(audio_file)

window_start = 26  # en segundos
window_size = 4  # en segundos


window_end = window_start + window_size
start_sample = int(window_start * samplerate)
end_sample = int(window_end * samplerate)


windowed_signal = data[start_sample:end_sample]

if len(windowed_signal.shape) == 2:
    windowed_signal = np.mean(windowed_signal, axis=1)

time = np.linspace(0, len(data) / samplerate, num=len(data))

fig, ax = plt.subplots(2, 1, figsize=(12, 8))

if len(data.shape) == 2:
    data_mono = np.mean(data, axis=1)
else:
    data_mono = data

ax[0].plot(time, data_mono, color='lightblue', label='Señal completa')
ax[0].axvspan(window_start, window_end, color='orange', alpha=0.5, label='Ventana seleccionada')
ax[0].set_title('Señal de audio completa con ventana resaltada')
ax[0].set_xlabel('Tiempo (s)')
ax[0].set_ylabel('Amplitud')
ax[0].set_xlim((0,len(data)/samplerate))
ax[0].set_ylim((-2,2))
ax[0].legend()
ax[0].grid()

fft_result = np.fft.fft(windowed_signal)
frequencies = np.fft.fftfreq(n=len(windowed_signal), d=1/samplerate)

positive_frequencies = frequencies[:len(frequencies)//2]
positive_fft_result = np.abs(fft_result[:len(fft_result)//2])

ax[1].plot(positive_frequencies, positive_fft_result)
ax[1].set_title('FFT de la ventana temporal seleccionada')
ax[1].set_xlabel('Frecuencia (Hz)')
ax[1].set_ylabel('Magnitud')
ax[1].set_xlim((0, 2000))
ax[1].grid()

plt.tight_layout()
plt.show()