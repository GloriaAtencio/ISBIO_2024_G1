# **Laboratorio N°4: Uso de BiTalino para ECG**

***

# **Tabla de contenidos**
1. [Contexto](#id1)
2. [Procedimiento](#id2)
3. [Videos](#id3)
4. [Ploteos y análisis](#id4)

***

# 1.Contexto<a name="id1"></a>

<p align="justify">
Para el laboratorio N°4 se nos pidió adquirir la señal ECG usando la tarjeta BiTalino, es por eso que el objetivo principal para este laboratorio es realizzar mediciones de la señal haciendo de dos a tres tipos de pruebas que nos permitan conocer más acerca de la variación de la señal y así poder plantear la respectiva discusión al final.
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

<p align="justify">
Ya dentro del Open Signals, se nos dió el ProSim 4. con el cual obtuvimos el ejemplo una señal ecg en distintas fases de una parada cardíaca. Se grabó la variación de la señal durante las 5 etapas y se obtuvo lo siguiente:
</p>

### Videos e imágenes de señales obtenidas con el ProSim 4

#### Etapa 1 

#### Etapa 2

#### Etapa 3

#### Etapa 4

#### Etapa 5

### Posicionamiento de electrodos

<p align="justify">
Con respecto el posicionamiento de los electrodos, nos guiamos del protocolo de la guía del BiTalino.
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5884e90568d787a64e4d173875539c3cefb68913/ISB/Laboratorios/Im%C3%A1genes/ECG/bita_ecg_pos.jpeg" alt="fotog" width="300" height="300"/>
</p>
<p align="center"><i>Figura 3. Posicionamiento de los electrodos en el usuario</i></p>

# 3.Videos<a name="id3"></a>

## Caso 1: Reposo

<p align="justify">
Se colocaron los electrodos respectivamente y se pidió al usuario mantener su cuerpo en estado de reposo para así poder adquirir la señal y hacer la grabación de dicho momento. Asimismo, nos aseguramos que el usuario no portara ningún tipo de objeto que fuera de metal.
</p>

<div align="center">
  <video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>
</div>


## Caso 2: Ejercicio
<div align="center">
  <video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/45419d9b-965e-47d3-9d13-16ecac872f61" width="300" height="300"></video>
</div>


## Caso 3: Sentadillas rápidas 

<div align="center">
  <video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/de98dfbb-ffa4-4979-869f-52692feec2f9" alt="video/mp4" width="300" height="300"></video>
</div>

## Caso 4: Hiperventilación

<div align="center">
  <video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/03ea0920-e83d-4704-b5d9-c194ae37dadb" width="300" height="300"></video>
</div>




# 4.Ploteos y análisis<a name="id2"></a>

## Caso 1: Reposo

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_reposo.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 4. Señal ECG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_reposo.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 5. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

## Caso 2: Ejercicio

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_despues_de_actividad.PNG" alt="fotog" width="560" height="300"/>
</p>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_Actividad.PNG" alt="fotog" width="560" height="300"/>
</p>

## Caso 3: Sentadillas rápidas 
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_sentadillas.PNG" alt="fotog" width="560" height="300"/>
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_Sentadillas.PNG" alt="fotog" width="560" height="300"/>
</p>

## Caso 4: Hiperventilación

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/ECG_hiperventilaci%C3%B3n.PNG" alt="fotog" width="560" height="300"/>
</p>


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/ECG/plot_ecg/FFT_Hiperventilaci%C3%B3n.PNG" alt="fotog" width="560" height="300"/>
</p>



# Referencias bibliográficas
