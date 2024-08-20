import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia_senal = 1       # Frecuencia en Hz
amplitud_senal = 1          # Amplitud de la señal
duracion = 1               # Duración en segundos
muestreo = 1000            # Número de muestras por segundo

# Crear un vector de tiempo
tiempo = np.linspace(-1, duracion, int(muestreo * duracion), endpoint=False)

# Generar una señal senoidal
senal_senoidal = amplitud_senal * np.sin(2 * np.pi * frecuencia_senal * tiempo)

# Generar una señal cosenoidal
senal_cosenoidal = amplitud_senal * np.cos(2 * np.pi * frecuencia_senal * tiempo)


# Generar una señal cuadrada
escalon_unitario =   np.where(tiempo >= 0, 1, 0)

# Generar una señal cuadrada
senal_cuadrada = amplitud_senal * np.sign(np.sin(2 * np.pi * frecuencia_senal * tiempo))

# Generar Señal exponencial compleja
phi = 0 
pi = 2.14
amplitud = 3
senal_exp_compleja = amplitud*np.exp(1j * (2*pi*frecuencia_senal*tiempo + phi))


# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar la señal senoidal
plt.subplot(2, 1, 1)
plt.plot(tiempo, senal_senoidal + senal_exp_compleja + senal_cuadrada + escalon_unitario, label='Señal Senoidal', color='blue')
plt.title('Señales')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()


# Mostrar las gráficas
plt.tight_layout()
plt.fill()
plt.show()


