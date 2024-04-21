# **Laboratorio N°4: Uso de BiTalino para ECG**

***

# **Tabla de contenidos**
1. [Contexto](#id1)
2. [Procedimiento](#id2)
3. [Videos](#id3)
4. [Ploteos y análisis](#id4)
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

***

# 1.Contexto<a name="id1"></a>

<p align="justify">
En el Laboratorio N°4, se ha encomendado la tarea de adquirir la señal ECG utilizando la tarjeta BiTalino. El objetivo principal de esta actividad es realizar mediciones de la señal ECG a través de dos a tres tipos de pruebas específicas. Estas pruebas están diseñadas para proporcionar un mayor entendimiento sobre la variación de la señal, permitiendo así plantear una discusión fundamentada al concluir el laboratorio.
</p>

<p align="justify">
Al finalizar las pruebas y recopilar los datos necesarios, se podrá realizar una discusión fundamentada y detallada sobre los resultados obtenidos. Esta discusión no solo implicará la interpretación de los datos medidos, sino también la comparación con teorías previas, la identificación de posibles patrones o anomalías en la señal, y la formulación de conclusiones relevantes.
</p>

# 2.Procedimiento<a name="id2"></a>

## Conexión del BiTalino 

### Materiales y equipos 


|     Modelo       |                  Descripción                  |   Cantidad    |
|  :-------------: |:--------------------------------------------: |:-------------:|
| (R)EVOLUTION     | Kit BITalino                                  | 1             |
| -                | Laptop                                        | 1             |
| Fluke            | Prosim 4                                      | 1             |


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/9a7420da071748b34dc40f665ea7b1db2cfc3242/ISB/Laboratorios/Im%C3%A1genes/ECG/mat_bitalino_ecg.jpeg" alt="fotog" width="500" height="300"/>
</p>
<p align="center"><i>Figura 1. Tarjeta BiTalino</i></p>

<p align="justify">
Como primer paso, hay que conectar la batería a la tarjeta y cambiar el switch de off a on. Después de ello , se tuvo que emparejar mediante bluetooth la tarjeta (BiTalino 4F-CD) y la laptop. Ya una vez hecha la conexión se abrió el programa Open Signals, se ubicó la tarjeta dentro del programa.
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/9a7420da071748b34dc40f665ea7b1db2cfc3242/ISB/Laboratorios/Im%C3%A1genes/ECG/ops_sg_ecg.jpeg" alt="fotog" width="500" height="300"/>
</p>
<p align="center"><i>Figura 2. Conexión de la tarjeta con el programa Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/b41ba03a0c28263c082ba419738f025b52fae340/ISB/Laboratorios/Im%C3%A1genes/ECG/prosim.jpeg" alt="fotog" width="300" height="380"/>
</p>
<p align="center"><i>Figura 3. Secuencia de parada cardiaca en el ProSim 4</i></p>

<p align="justify">
Ya dentro del Open Signals, se nos dió el ProSim 4. con el cual obtuvimos el ejemplo una señal ecg en distintas fases de una parada cardíaca. Se grabó la variación de la señal durante las 5 etapas y se obtuvo lo siguiente:
</p>

### Imágenes de las señales obtenidas con el ProSim 4

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/941e688e122232804b8e87dc74393373679f659a/ISB/Laboratorios/Im%C3%A1genes/ECG/etapa1_prosim.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 4. Señal obtenida en la primera etapa simulada en el ProSim en el programa Open Signals</i></p>



<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/941e688e122232804b8e87dc74393373679f659a/ISB/Laboratorios/Im%C3%A1genes/ECG/etapa2_prosim.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 5. Señal obtenida en la segunda etapa simulada en el ProSim en el programa Open Signals</i></p>



<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/941e688e122232804b8e87dc74393373679f659a/ISB/Laboratorios/Im%C3%A1genes/ECG/etapa3_prosim.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 6. Señal obtenida en la tercera etapa simulada en el ProSim en el programa Open Signals</i></p>



<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/941e688e122232804b8e87dc74393373679f659a/ISB/Laboratorios/Im%C3%A1genes/ECG/etapa4_prosim.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 7. Señal obtenida en la cuarta etapa simulada en el ProSim en el programa Open Signals</i></p>



<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/941e688e122232804b8e87dc74393373679f659a/ISB/Laboratorios/Im%C3%A1genes/ECG/etapa5_prosim.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 8. Señal obtenida en la quinta etapa simulada en el ProSim en el programa Open Signals</i></p>

<p align="justify">
En la primera etapa, se puede visualizar un ritmo cardíaco normal, con una actividad eléctrica cardíaca regular y un patrón típico de ondas P, QRS y T en el ECG. Seguido se observa como la morfología entre Py T empieza a demostrar cambios notorios, muy propios de una taquicardia por lo aberrante de su morfología. Asimismo la desorganización de la señal a posterior indicaría una fibrilación ventricular oscilante; por lo general se puede observar una desaceleración gradual del ritmo cardíaco y la aparición de ritmos irregulares. Por lo ultimo se reconoce asistolia, se reconoce una línea isoeléctrica, sin la presencia de complejos QRS ni de ondas P o T, indicando asi la ausencia total de actividad eléctrica en el corazón.[1]
  
</p>

| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/7305731af22fcf05c313b37e133810dc5eb14936/ISB/Laboratorios/Im%C3%A1genes/ECG/plot1_op_prosim.jpeg) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/7305731af22fcf05c313b37e133810dc5eb14936/ISB/Laboratorios/Im%C3%A1genes/ECG/plot2_py_prosim.jpeg) |
|:-------------------------:|:-------------------------:|
|        **Señal construida a partir del archivo txt obtenido del OpenSignals**      |        **Ploteo de la señal obtenida del OpenSignals usando python**      |


### Posicionamiento de electrodos

<p align="justify">
Con respecto el posicionamiento de los electrodos, nos guiamos del protocolo de la guía del BiTalino.
</p>

### Protocolo: 
<p align="justify">
Para realizar las pruebas del sensor ECG BITalino hemos usado la configuración de la derivación I de Einthoven, posicionando los electrodos en las muñecas y la cresta ilíaca. El electrodo positivo (rojo) se ubicó en la muñeca izquierda (LA) y el electrodo negativo (negro) en la muñeca derecha (RA). La referencia (REF) en blanco se situó en la cresta ilíaca.[2] Por otro lado, para la toma de la data planteamos 3 casos, en estado basal, en actividad física e hiperventilación.
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5884e90568d787a64e4d173875539c3cefb68913/ISB/Laboratorios/Im%C3%A1genes/ECG/bita_ecg_pos.jpeg" alt="fotog" width="300" height="300"/>
</p>
<p align="center"><i>Figura 9. Posicionamiento de los electrodos en el usuario</i></p>

# 3.Videos<a name="id3"></a>

## Caso 1: Reposo

<p align="justify">
Se colocaron los electrodos respectivamente y se pidió al usuario mantener su cuerpo en estado de reposo para así poder adquirir la señal y hacer la grabación de dicho momento. Asimismo, nos aseguramos que el usuario no portara ningún tipo de objeto que fuera de metal.
</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/reposo_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>|
</div>


## Caso 2: Actividad física
<p align="justify">
Para este caso, se le pidió al usuario que realizara ejercicio por unos 5 minutos para así adquirir data cuando la frecuencia cardíaca aumenta. Una vez que el usuario terminó la actividad física se le volvió a colocar los electrodos y se inició la medición de la señal en el programa Open Signals.
</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/ejercicio_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/45419d9b-965e-47d3-9d13-16ecac872f61" width="300" height="300"></video>|
</div>


## Caso 3: Sentadillas rápidas 
<p align="justify">
En realidad, este caso lo utilizamos como una forma de medición que no permitió ver cómo es que la señal variaba dependiendo el esfuerzo físico del usuario. Si bien se le pisió al usuario hacer sentadillas en periodos cortos de tiempo , la data obtenida no se tomó en cuenta finalmente porque esta presentó mucho ruido en el programa Open Signals.
</p>
<div align="center">

|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/4c45903a2bed9d5834583624d6b6f98c12b42dc4/ISB/Laboratorios/Im%C3%A1genes/ECG/sentadilla_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/de98dfbb-ffa4-4979-869f-52692feec2f9" alt="video/mp4" width="300" height="300"></video>|
</div>

## Caso 4: Hiperventilación
<p align="justify">
Por último, se le pidió al usuario intentar imitar una hiperventilación para poder ver el impacto de la respiración en la señal ECG. Es por ello, que se propusimos esta actividad como tercer caso de prueba y tomamos los datos respectivos de la señal adquirida en el Open Signals.
</p>
<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/hiperventilaci%C3%B3n_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/03ea0920-e83d-4704-b5d9-c194ae37dadb" width="300" height="300"></video>|
</div>




# 4.Ploteos y análisis<a name="id4"></a>

## Caso 1: Reposo

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_reposo.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal ECG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_reposo.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

<p align="justify">
Análisis: En estado basal, en la derivación I del electrocardiograma (ECG), la onda P representa la despolarización auricular, siendo generalmente positiva y de duración aproximada de 0.08 a 0.10 segundos. El intervalo PR, que va desde el inicio de la onda P hasta el inicio del complejo QRS, normalmente oscila entre 0.12 y 0.20 segundos. El complejo QRS, reflejando la despolarización ventricular, exhibe una morfología positiva inicial seguida de una onda negativa, con una duración de alrededor de 0.06 a 0.10 segundos. La onda T, representativa de la repolarización ventricular, es positiva y simétrica, con una duración similar a la onda P. El segmento ST, que precede a la onda T, generalmente se mantiene isoeléctrico en condiciones normales.[3]   
</p>
  
## Caso 2: Actividad física

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_despues_de_actividad.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 12. Reconstrucción de la señal ECG obtenida después de que el usuario realizó ejercicio a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_Actividad.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 13. Ploteo de la Señal ECG obtenida después de que el usuario realizó ejercicio en python</i></p>

<p align="justify">
Análisis: Después de hacer ejercicio moderado, se logra ver una frecuencia cardíaca más rápida, un aumento en la amplitud y la frecuencia de las ondas P, posiblemente por un acortamiento del intervalo PR, un complejo QRS ligeramente más amplio y cambios en el segmento ST, con elevación reducida debido a los cambios en repolarización ventricular.[3] 
</p>


## Caso 3: Sentadillas rápidas 

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_sentadillas.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 14. Reconstrucción de la señal ECG obtenida cuando el usuario realizó sentallidas cortas a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_Sentadillas.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 15. Ploteo de la Señal ECG obtenida cuando el usuario realizó sentallidas cortas en python</i></p>

## Caso 4: Hiperventilación

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_hiperventilaci%C3%B3n.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 16. Reconstrucción de la señal ECG obtenida durante el periodo de hiperventilación forzada del usuario a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_Hiperventilaci%C3%B3n.PNG" alt="fotog" width="560" height="300"/>
</p>

<p align="center"><i>Figura 17. Ploteo de la Señal ECG obtenida durante el periodo de hiperventilación forzada del usuario en python</i></p>

<p align="justify">
Análisis: La hiperventilación puede provocar cambios transitorios en el electrocardiograma (ECG), se ve un aumento en la frecuencia cardíaca debido a la estimulación del sistema nervioso autónomo, así como posibles alteraciones en el acortamiento de QT. Además, pueden observarse cambios en el segmento ST y la onda T, como ligeras elevaciones, reflejando la influencia de la hiperventilación en la repolarización ventricular. Estos cambios pueden variar en intensidad y duración, extrapolando a un caso real de hiperventilación según la gravedad y la duración de la hiperventilación, la alcalosis respiratoria derivaría en signos mas evidentes de los mencionados.[3][4]
</p>

## Código empleado - Python

```

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




```

# 5.Discusión<a name="id5"></a>


# 6.Referencias bibliográficas<a name="id6"></a>
<p align="justify">

[1] P. E. Nodal Leyva, J. G. López Héctor, and G. de La Llera Domínguez, "Paro cardiorrespiratorio (PCR): Etiología. Diagnóstico. Tratamiento," Revista Cubana de Cirugía, vol. 45, no. 3-4, Dec. 2006. [Online]. Available: http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S0034-74932006000300019&lng=es. [Accessed: Apr. 20, 2024]

[2] L. Y. Biosignals, “BITalino (r)evolution Lab Guide,” Pluxbiosignals.com. [Online]. Available: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf. [Accessed: Apr. 19, 2024].

[3] A. L. Goldberger, Z. D. Goldberger, and A. Shvilkin, _Goldberger’s Clinical Electrocardiography: A Simplified Approach_, 8th ed., Philadelphia, PA: Elsevier Saunders, 2013.

[4] S. Dash y A. Kumar, “Hyperventilation Leading to Transient T-wave Inversion Mimicking Unstable Angina,” Cureus, vol. 13, no. 1, e12980, enero 29, 2021. DOI: 10.7759/cureus.12980
</p>
