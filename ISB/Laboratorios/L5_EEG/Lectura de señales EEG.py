
#Lectura de Señales EEG


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re


f = open(r"C:\Users\Usuario\Downloads\EEG\EEG30sreposo.txt","r")
g = open(r"C:\Users\Usuario\Downloads\EEG\EEGparpadeo.txt","r")
h= open(r"C:\Users\Usuario\Downloads\EEG\EEG30sreposo_repeticion.txt","r")
i = open(r"C:\Users\Usuario\Downloads\EEG\ejercicio1.txt","r")
j= open(r"C:\Users\Usuario\Downloads\EEG\ejercicio2.txt","r")
raw_data = f.read()  # con f.read() leemos todo el contenido
raw_data2= h.read()
raw_data3= i.read()
raw_data4= g.read()
f.close()
h.close()
i.close()
g.close()

#raw_data

Fs = 1000
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")


array_1 = np.genfromtxt(r"C:\Users\Usuario\Downloads\EEG\EEG30sreposo.txt", delimiter="\t",skip_header = 4)
array_2=  np.genfromtxt(r"C:\Users\Usuario\Downloads\EEG\EEGparpadeo.txt", delimiter="\t",skip_header = 4)
array_3= np.genfromtxt(r"C:\Users\Usuario\Downloads\EEG\EEG30sreposo_repeticion.txt", delimiter="\t",skip_header = 4)
array_4= np.genfromtxt(r"C:\Users\Usuario\Downloads\EEG\ejercicio1.txt", delimiter="\t",skip_header = 4)
array_5= np.genfromtxt(r"C:\Users\Usuario\Downloads\EEG\ejercicio2.txt", delimiter="\t",skip_header = 4)


muestras=array_5[:,6].shape


#Momento de reposo inicial
plt.plot(array_5[:,6], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("N° de muestras (n)")
plt.ylabel("Amplitud")
plt.title("EEG en el que el sujeto responde preguntas de 100 peruanos dicen")
plt.legend(loc="upper right")
plt.xlim([5000,6000])

plt.show()

N = 2**10                                     # 10 bits, 0-1023

signal1 = array_5[:,6]

signal_fft = np.fft.fft(signal1, N)           # fft magtinud
signal_fft = np.round(np.abs(signal_fft),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
signal_aux = signal_fft/signal_fft.max()     # hallamos el maximo para pasar la magnitud a escala db

with np.errstate(divide='ignore'):
    signal_fft_db = 10*np.log10(signal_aux)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

F_list = np.linspace(0,Fs/2, N//2)
F = np.round(F_list[np.argmax(signal_fft_db)], 1)   # argmax, encuentra el argumento max en un array

plt.plot(F_list, signal_fft_db)  #10 * np.log10(P / Pref) , decibelios
plt.text(F,0, f"{F}Hz")
plt.grid(linestyle=":")
plt.ylabel("Magnitud (db)")
plt.xlabel("Frecuencias (Hz)")
plt.title("FFT en el decibelios de EEG sujeto responde preguntas de 100 peruanos dicen")
plt.xlim([0,200])
plt.xticks(np.arange(0,200,10))
plt.show()
