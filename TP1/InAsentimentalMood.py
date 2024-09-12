import wave 
import sys
import numpy as np
import matplotlib.pyplot as plt


#Obtener señal
wav = wave.open("InASentimentalMood.wav","r")

#Obtener Do
nota_do = wave.open("do.wav","r")
#Obtener Re
nota_re = wave.open("RE.wav","r")
#obtener Mi
nota_mi = wave.open("mi.wav","r")

#obtener Fa
nota_fa = wave.open("fa.wav","r")

#Obtener sol
nota_sol = wave.open("sol.wav","r")

#Obtener la
nota_la = wave.open("la.wav","r")

#Obtener si
nota_si = wave.open("si.wav","r")

#Raws
#señal
raw_señal = wav.readframes(-1)
raw_señal = np.frombuffer(raw_señal , "int16")

#do
raw_nota_do = nota_do.readframes(-1)
raw_nota_do =  np.frombuffer(raw_nota_do , "int16")

#Re
raw_nota_re = nota_re.readframes(-1)
raw_nota_re =  np.frombuffer(raw_nota_re , "int16")

#Mi
raw_nota_mi = nota_mi.readframes(-1)
raw_nota_mi =  np.frombuffer(raw_nota_mi , "int16")

#Fa
raw_nota_fa = nota_fa.readframes(-1)
raw_nota_fa =  np.frombuffer(raw_nota_fa , "int16")


#sol
raw_nota_sol = nota_sol.readframes(-1)
raw_nota_sol =  np.frombuffer(raw_nota_sol , "int16")

#la
raw_nota_la = nota_la.readframes(-1)
raw_nota_la =  np.frombuffer(raw_nota_la , "int16")


#si
raw_nota_si = nota_si.readframes(-1)
raw_nota_si =  np.frombuffer(raw_nota_si , "int16")



if wav.getnchannels() == 2 :
    print("Archivos Estereo no soportados , use mono")
    sys.exit(0)


# Crear una figura y dos subplots (uno para cada gráfico)
fig, ( ax_do , ax_re ,  ax_mi  ) = plt.subplots(3, 1, figsize=(20, 5))

fig3, ( ax_fa ,  ax_sol ,  ax_la , ax_si ) = plt.subplots(4, 1, figsize=(20, 5))

fig2, (ax_señal ) = plt.subplots(1, 1, figsize=(20, 5))

# Graficar musica
ax_señal.plot(raw_señal, color='green',label ="InASentimentalMood")
ax_señal.set_title('InASentimentalMood')
ax_señal.set_xlabel('t')
ax_señal.set_ylabel('Amplitud')

# Graficar Do
ax_do.plot(raw_nota_do, color='blue',label ="Do")
ax_do.set_title('DO')
ax_do.set_xlabel('t')
ax_do.set_ylabel('Amplitud')

#Grafico Re
ax_re.plot(raw_nota_re, color='red',label ="Re")
ax_re.set_title('RE')
ax_re.set_xlabel('t')
ax_re.set_ylabel('Amplitud')

#Grafico Mi
ax_mi.plot(raw_nota_mi, color='orange',label ="Mi")
ax_mi.set_title('MI')
ax_mi.set_xlabel('t')
ax_mi.set_ylabel('Amplitud')


#Grafico Fa
ax_fa.plot(raw_nota_fa, color='lightblue',label ="Fa")
ax_fa.set_title('FA')
ax_fa.set_xlabel('t')
ax_fa.set_ylabel('Amplitud')

# Graficar sol
ax_sol.plot(raw_nota_sol, color='purple',label ="Sol")
ax_sol.set_title('SOL')
ax_sol.set_xlabel('t')
ax_sol.set_ylabel('Amplitud')


#Grafico La
ax_la.plot(raw_nota_la, color='pink',label ="La")
ax_la.set_title('LA')
ax_la.set_xlabel('t')
ax_la.set_ylabel('Amplitud')



#Grafico Si
ax_si.plot(raw_nota_si, color='brown',label ="Si")
ax_si.set_title('SI')
ax_si.set_xlabel('t')
ax_si.set_ylabel('Amplitud')

fig.subplots_adjust(hspace = 1)

# Ajustar el espacio entre subplots
plt.tight_layout()

# Mostrar la figura con los subplots
plt.show()