import numpy as np
import matplotlib.pyplot as plt
import wave


#Obtener señal
wav = wave.open("do.wav","r")
#señal
raw_señal = wav.readframes(-1)
raw_señal = np.frombuffer(raw_señal , "int16")

# Supongamos que tienes una señal muestreada a 44.1 kHz
fs = 44100  # Tasa de muestreo en Hz (ejemplo)

# Crear una señal de ejemplo de 3.33 segundos
t = np.linspace(0, 3.33, int(fs * 3.33), endpoint=False)
signal = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)  # Ejemplo con componentes a 440 Hz y 880 Hz

# Realizar la FFT
n = len(raw_señal)
yf = np.fft.fft(raw_señal)
xf = np.fft.fftfreq(n, 1/fs)

# Encontrar la frecuencia fundamental
magnitude = np.abs(yf)
fundamental_freq = xf[np.argmax(magnitude[:n//2])]  # Solo considerar la mitad positiva del espectro

print(f"La frecuencia fundamental es: {fundamental_freq:.2f} Hz")

# Graficar el espectro de frecuencias
plt.figure(figsize=(12, 6))
plt.plot(xf[:n//2], magnitude[:n//2])
plt.title('Espectro de Frecuencias')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
plt.show()