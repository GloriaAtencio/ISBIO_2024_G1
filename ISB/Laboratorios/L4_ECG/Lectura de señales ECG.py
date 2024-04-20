
#Lectura de Señales EMG

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re


reposo = open(r'C:\Users\Usuario\Downloads\Lab_EKG\ECG_reposo.txt', 'r')
despues_acti= open(r'C:\Users\Usuario\Downloads\Lab_EKG\ECG_despuesdeactividad.txt', 'r')
sentadillas= open(r'C:\Users\Usuario\Downloads\Lab_EKG\ECG_Sentadillas.txt', 'r')
hiperventilacion= open(r'C:\Users\Usuario\Downloads\Lab_EKG\ECG_hiperventilación.txt', 'r')
raw_data = reposo.read()  #  f.read() leemos todo el contenido
raw_data2= despues_acti.read()
raw_data3= sentadillas.read()
raw_data4= hiperventilacion.read()
reposo.close()
despues_acti.close()
sentadillas.close()
hiperventilacion.close()



#------------------------------------------------------------------------------------
Fs = 1000
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")

array_1 = np.genfromtxt(r"C:\Users\Usuario\Downloads\Lab_EKG\ECG_reposo.txt", delimiter="\t",skip_header = 4)
array_2=  np.genfromtxt(r"C:\Users\Usuario\Downloads\Lab_EKG\ECG_despuesdeactividad.txt", delimiter="\t",skip_header = 4)
array_3= np.genfromtxt(r"C:\Users\Usuario\Downloads\Lab_EKG\ECG_Sentadillas.txt", delimiter="\t",skip_header = 4)
array_4= np.genfromtxt(r"C:\Users\Usuario\Downloads\Lab_EKG\ECG_hiperventilación.txt", delimiter="\t",skip_header = 4)




#Momento de reposo inicial
plt.plot(array_1[:,6], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("N° de muestras (n)")
plt.ylabel("Amplitud")
plt.title("ECG_reposo")
plt.legend(loc="upper right")
plt.xlim([5000,7000])

#plt.show()


#ECG del usuario despues de hacer ejercicio
plt.plot(array_2[:,6], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("N° de muestras (n)")
plt.ylabel("Amplitud")
plt.title("ECG después de actividad Física")

plt.legend(loc="upper right")
plt.xlim([5000,7000])

plt.show()

#ECG del usuario sentadillas
plt.plot(array_3[:,6], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("N° de muestras (n)")
plt.ylabel("Amplitud")
plt.title("ECG sentadillas")

plt.legend(loc="upper right")
plt.xlim([5000,7000])

plt.show()

#ECG hiperventilacion
plt.plot(array_4[:,6], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("N° de muestras (n)")
plt.ylabel("Amplitud")
plt.title("ECG hiperventilación")

plt.legend(loc="upper right")
plt.xlim([5000,7000])

plt.show()



N = 2**10                                     # 10 bits, 0-1023

signal1 = array_4[:,6]

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
plt.title("FFT en el decibelios de ECG Hiperventilación")
plt.xlim([0,200])
plt.xticks(np.arange(0,200,10))
plt.show()





