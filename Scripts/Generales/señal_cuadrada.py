import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia = 44  # Frecuencia de la nota La en Hz
duracion = 2.0    # Duración de la señal en segundos
muestra_por_segundo = 1000  # Número de muestras por segundo (frecuencia de muestreo)

# Generar el vector de tiempo
t = np.linspace(0, duracion, int(duracion * muestra_por_segundo), endpoint=False)

# Generar la señal de la nota musical
senal = 0.5 * np.sin(2 * np.pi * frecuencia * t)

# Graficar la señal
plt.figure(figsize=(10, 4))
plt.plot(t, senal)
plt.title(f'Señal de una nota musical de {frecuencia} Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
