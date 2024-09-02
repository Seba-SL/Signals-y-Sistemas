import wave 
import sys
import numpy as np
import matplotlib.pyplot as plt

wav = wave.open("Zombie.wav","r")

raw = wav.readframes(-1)
raw = np.frombuffer(raw , "int16")

if wav.getnchannels() == 2:
    print("Archivos Estereo no soportados , use mono")
    sys.exit(0);

plt.title("Señal de onda del archivo : Zombie.wav")

plt.plot(raw , color = "green")


plt.ylabel("Amplitud")
plt.xlabel("tiempo")


plt.tight_layout()

plt.show()