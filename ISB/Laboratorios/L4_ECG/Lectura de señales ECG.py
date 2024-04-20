
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
plt.xlim([5000,1000])

plt.show()

