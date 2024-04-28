# **Laboratorio N°5: Uso de BiTalino para EEG**

***

# **Tabla de contenidos**
1. [Introducción](#id1)
2. [Procedimiento](#id2)
3. [Videos](#id3)
4. [Ploteos y análisis](#id4)
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

***

# 1.Introducción<a name="id1"></a>

<p align="justify">

## Objetivo:

El objetivo de este laboratorio es registrar y analizar la señal electroencefalográfica (EEG) de un sujeto durante diferentes estados de actividad cerebral.  específicamente, se busca:

- Registrar una línea base de señal con poco ruido y sin movimientos durante 30 segundos.
- Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos.
- Registrar otra fase de referencia de 30 segundos.
- Registrar la señal mientras el sujeto realiza ejercicios matemáticos mentales.
</p>

  
## Marco teórico:

<p align="justify">
El electroencefalograma (EEG) es una técnica neurofisiológica que registra la actividad eléctrica del cerebro.  La señal EEG se genera por la despolarización e hiperpolarización de las neuronas corticales.  La actividad EEG se puede analizar en términos de frecuencia, amplitud y forma de onda.
</p>

<p align="justify">
  
- Frecuencia: La frecuencia de la señal EEG se mide en hercios (Hz). Las diferentes frecuencias de EEG se asocian con diferentes estados de actividad cerebral. Por ejemplo, las ondas delta (0,5-4 Hz) se asocian con el sueño profundo, mientras que las ondas beta (12-30 Hz) se asocian con la vigilia y la atención. [1]

- Amplitud: La amplitud de la señal EEG se mide en microvoltios (µV). La amplitud de la señal EEG puede variar dependiendo del estado de actividad cerebral y de otros factores, como la edad y el sexo.[1]

- Forma de onda: La forma de onda de la señal EEG se refiere al patrón de la señal a lo largo del tiempo. La forma de onda de la señal EEG puede variar dependiendo del tipo de actividad cerebral que se esté registrando.[1]
  
</p>


# 2.Procedimiento<a name="id2"></a>

## Conexión del BiTalino 



<div align="center">

### Materiales y equipos 

|     Modelo       |                  Descripción                  |   Cantidad    |
|  :-------------: |:--------------------------------------------: |:-------------:|
| (R)EVOLUTION     | Kit BITalino                                  | 1             |
| -                | Laptop                                        | 1             |
| -                | Electrodos                                    | 3             |
</div>

<p align="center">
 <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f2a73e9eb7b9cc528b56bf9261b093b2c905f8e3/ISB/Laboratorios/Im%C3%A1genes/EEG/bitalino_eeg.png" alt="fotog" width="500" height="300"/>
</p>
<p align="center"><i>Figura 1. Tarjeta BiTalino</i></p>

<p align="justify">

El procedimiento inicial consistió en conectar la batería a la tarjeta y activar el interruptor de apagado a encendido. Luego, se procedió a emparejar la tarjeta BiTalino con la laptop a través de Bluetooth. Una vez establecida la conexión, se inició el programa Open Signals y se localizó la tarjeta dentro de la interfaz del programa.
</p>

## Posicionamiento de electrodos

<p align="justify">
Tras leer el manual de usuario de la tarjeta, confirmamos que para este laboratorio era necesario el uso de 3 electrodos para obtener la señal EEEG. Para determinar la colocación adecuada de los electrodos, seguimos las instrucciones detalladas en el manual tipo guía proporcionado por BiTalino.
</p>

<p align="center">
 <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/8a6d4f4c3a2a639e7e6bb67bd623d400adca8478/ISB/Laboratorios/Im%C3%A1genes/EEG/electrodos_bitalino.png" alt="fotog" width="600" height="200"/>
</p>
<p align="center"><i>Figura 2. Cantidad de electrodos necesarios según el tipo de señal [2]</i></p>

## Protocolo
<p align="justify">

</p>

| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/c7c651d3689e8628b29ea806629639e14f2c6c82/ISB/Laboratorios/Im%C3%A1genes/EEG/electrodos_1.jpeg) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/c7c651d3689e8628b29ea806629639e14f2c6c82/ISB/Laboratorios/Im%C3%A1genes/EEG/electrodos_2.jpeg) |
|:-------------------------:|:-------------------------:|
|        **Vista frontal**      |        **Vista lateral**      |


# 3.Videos<a name="id3"></a>
<p align="justify">
Cabe resaltar que todos los registros de las señales fueron realizados a una frecuencia de 100 Hz, esto se debe a que la tarjeta BiTalino solo utiliza las siguientes frecuencias: 100, 10 y 10 Hz e incluso hasta 1000 Hz (según su manual de usuario en Especificaciones técnicas).[2]
</p>
<p align="center">
 <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/8a6d4f4c3a2a639e7e6bb67bd623d400adca8478/ISB/Laboratorios/Im%C3%A1genes/EEG/especificaciones_tecnicas_bitalino.png" alt="fotog" width="500" height="300"/>
</p>
<p align="center"><i>Figura 3. Especificaciones técnicas de la tarjeta BiTalino[2]</i></p>

## Caso 1: Respiración normal, sin movimientos oculares/ojos cerrados durante 30 segundos

<p align="justify">
Se procedió a registrar una línea base de señal con mínima interferencia y ausencia de movimientos (respiración en su ritmo normal, sin movimiento ocular ni ojos abiertos) durante un período de 30 segundos. Esta condición, denominada como "caso 1", fue utilizada para capturar la señal EEG en el software Open Signals. Para verificar que el tiempo fuera el correcto se utilizó un cronómetro.
</p>


<div align="center">
<h2>¿Por qué se considera una línea base en EEG y su importancia?</h2>
</div>

<p align="justify">
Una línea base en EEG se refiere a la actividad cerebral registrada en condiciones de reposo y calma, sin interferencias externas ni movimientos fisiológicos significativos. Esta condición es crucial en la investigación y análisis de señales cerebrales, ya que proporciona un punto de referencia estable y consistente para comparar con otras actividades cerebrales o intervenciones.[3]
</p>
<p align="justify">
La importancia de establecer una línea base radica en que permite identificar patrones normales de actividad cerebral de un individuo en un estado de reposo, lo que facilita la detección de cambios significativos que puedan indicar alteraciones o respuestas a estímulos específicos. Además, la línea base sirve como punto de partida para evaluar la eficacia de tratamientos, intervenciones o tareas cognitivas al compararlas con la actividad cerebral en reposo.[3]
</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/3f7e35cf2eb9920438122a8e60794ad830b08fe0/ISB/Laboratorios/Im%C3%A1genes/EEG/reposo_eeg_1_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/3a96023b-0b57-4392-9a56-2c838ebdad0f" width="300" height="300"></video>|
</div>



## Caso 2: Ciclo de ojos abiertos - ojos cerrados cinco veces

<p align="justify">
Se llevó a cabo la repetición de un ciclo consistente en alternar entre los estados de ojos abiertos y ojos cerrados, cada uno mantenido durante cinco segundos, y se repitió este ciclo en cinco ocasiones. Adquirir la señal EEG en situaciones específicas, como en el caso mencionado de alternar entre ojos abiertos y cerrados, sirve para estudiar y entender cómo el cerebro responde a diferentes estímulos y condiciones. Este tipo de adquisición de señal proporciona información valiosa sobre la actividad eléctrica cerebral y puede utilizarse en diversas aplicaciones, como en la investigación de trastornos neurológicos, la evaluación de la atención y la concentración, el monitoreo del estado de alerta, entre otros. 
</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/3f7e35cf2eb9920438122a8e60794ad830b08fe0/ISB/Laboratorios/Im%C3%A1genes/EEG/parpadeo_eeg_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/dfcd0bb7-95a5-4aaa-b080-cdadaefcc273" width="300" height="300"></video>|
</div>


## Caso 3: Fase de referencia de 30 segundos

<p align="justify">
Se procedió a registrar otra fase de referencia de 30 segundos, manteniendo las condiciones de calma y reposo sin movimientos significativos, similar al caso anteriormente mencionado como "caso 1".
</p>

<div align="center">
<h2>Importancia de obtener otra fase de referencia</h2>
</div>

<p align="justify">
Volver a registrar otra fase de referencia, en este caso "caso 3", es fundamental en el proceso de adquisición de señales EEG por varias razones:
</p>

<p align="justify">
1. Verificación de la consistencia: Obtener una segunda fase de referencia permite verificar la estabilidad y consistencia de la señal EEG registrada. Al repetir el proceso, se puede confirmar si los resultados obtenidos son reproducibles y confiables.[4]
</p>

<p align="justify">
2. Control de posibles interferencias: Al realizar múltiples fases de referencia, se puede identificar y controlar posibles interferencias o artefactos que puedan afectar la calidad de la señal EEG. Esto ayuda a garantizar que la señal capturada sea lo más pura y precisa posible.
</p>

<p align="justify">
3. Comparación y análisis: Contar con múltiples fases de referencia facilita la comparación entre diferentes momentos de actividad cerebral en reposo, lo que puede revelar patrones o cambios significativos en la actividad cerebral que de otra manera podrían pasar desapercibidos.[4]
   
</p>
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/3f7e35cf2eb9920438122a8e60794ad830b08fe0/ISB/Laboratorios/Im%C3%A1genes/EEG/reposo_eeg_2_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/4f032e7f-0600-4a20-a24c-c89d2e37f389" width="300" height="300"></video>|
</div>



## Caso 4: Solución de acertijos

<p align="justify">
Bajo la premisa de obtener una mayor variación en la señal EEG, se planteó el "caso 4". En este escenario, se solicitó a uno de nuestros compañeros que leyera en voz alta una serie de ejercicios matemáticos, mientras el usuario resolvía cada uno de ellos mentalmente. Se instruyó al usuario a enfocar su mirada en un punto específico para minimizar la generación de artefactos. Sin embargo, los resultados no fueron los esperados, ya que el tiempo de respuesta del usuario oscilaba entre 5 y 6 segundos, y al observar la señal en Open Signals, no se evidenciaba una variación significativa en comparación con la línea base. Ante esta situación, se optó por realizar una lectura de acertijos con la esperanza de generar picos más notorios en la señal.
  
</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/3f7e35cf2eb9920438122a8e60794ad830b08fe0/ISB/Laboratorios/Im%C3%A1genes/EEG/acertijos_eeg_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/7ffcb595-1aad-423c-bacc-27f90f1a04fb" width="300" height="300"></video>|
</div>



## Caso 5: Solución de preguntas de 100 peruanos dicen

<p align="justify">
En el "caso 5", se decidió cambiar el enfoque de los acertijos a la resolución de preguntas al estilo del programa "100 Peruanos Dicen". Este programa implica que cinco miembros en cada grupo intenten adivinar las respuestas proporcionadas por 100 personas en una encuesta previa, acumulando puntos según la popularidad de las respuestas. Se procuró que las preguntas fueran cortas y generales para facilitar las respuestas del usuario. Este cambio se realizó con la intención de generar una mayor variación en la señal EEG y obtener picos más notorios que permitieran un análisis más claro de la actividad cerebral.
</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/3f7e35cf2eb9920438122a8e60794ad830b08fe0/ISB/Laboratorios/Im%C3%A1genes/EEG/preguntas100_eeg_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/950e223c-d6b6-46f5-9407-4257fd673218" width="300" height="300"></video>|
</div>



# 4.Ploteos y análisis<a name="id4"></a>

## Caso 1: Respiración normal, sin movimientos oculares/ojos cerrados durante 30 segundos

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 4. Reconstrucción de la señal EEG (línea base) obtenida a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 5. Ploteo de la Señal EEG (línea base) obtenida en python</i></p>


<p align="justify">

</p>

## Caso 2: Ciclo de ojos abiertos - ojos cerrados cinco veces

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/c_a_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 6. Reconstrucción de la señal EEG obtenida durante los 5 ciclos de ojos abiertos-cerrados a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/c_a_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 7. Ploteo de la Señal EEG obtenida durante los 5 ciclos de ojos abiertos-cerrados en python</i></p>

<p align="justify">

</p>

## Caso 3: Fase de referencia de 30 segundos

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo2_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 8. Reconstrucción de la señal EEG obtenida durante el registro de la segunda línea base a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo2_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 9. Ploteo de la Señal EEG obtenida durante el registro de la segunda línea base en python</i></p>

<p align="justify">

</p>

## Caso 4: Solución de acertijos

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/acertijo_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal EEG obtenida durante la solución de acertijos a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/acertijos_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal EEG obtenida durante la solución de acertijos en python</i></p>

<p align="justify">

</p>

## Caso 5: Solución de preguntas de 100 peruanos dicen


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/100preruanosdicen_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 12. Reconstrucción de la señal EEG obtenida durante la solución de las preguntas (100 peruanos dicen) a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/100peruanosdicen_fft.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 13. Ploteo de la Señal EEG obtenida durante la solución de las preguntas (100 peruanos dicen) en python</i></p>

<p align="justify">

</p>

## Código empleado - Python

```python

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

```

# 5.Discusión<a name="id5"></a>

<p align="justify">

</p>

# 6.Referencias bibliográficas<a name="id6"></a>

<p align="justify">
1. A. Rayi y N. Murr, «Electroencephalogram», en StatPearls, Treasure Island (FL): StatPearls Publishing, 2024. Accedido: 27 de abril de 2024. [En línea]. Disponible en: http://www.ncbi.nlm.nih.gov/books/NBK563295/
</p>

<p align="justify">
2. “BITalino (r)evolution User Manual.” Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2021/11/bitalino-revolution-user-manual.pdf
</p>
<p align="justify">
3. M. S. R. Campos, J. P. H. Corvacho, L. D. S. Andrade, y J. M. L. López, «ANÁLISIS DE LAS CARACTERÍSTICAS DE EEG EN UN CONTEXTO DE EMOCIONES INDUCIDAS», EIEI ACOFI, sep. 2021, doi: 10.26507/ponencia.1765.
</p>
<p align="justify">
4. «Líneas base, anotaciones enfocadas al diseño experimental fNIRS y EEG», BuscaEU. Accedido: 27 de abril de 2024. [En línea]. Disponible en: https://brainlatam.com/blog/lineas-base-anotaciones-enfocadas-al-diseno-experimental-fnirs-y-eeg-1836
</p>
