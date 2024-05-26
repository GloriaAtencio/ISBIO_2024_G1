# LABORATORIO 8 - PROCESAMIENTO DE EMG

## TABLA DE CONTENIDO

1. [Objetivos](#id1)
2. [Introducción](#id2)
3. [Metodología](#id3)
   - [Filtrado](#id4)
   - [Segmentación](#id5)
   - [Extracción de características](#id6)
4. [Discusiones](#id7)
5. [Bibliografía](#id8)

# 1. Objetivos <a name="id1"></a>
   - Investigar y recopilar literatura científica sobre técnicas y métodos utilizados en el procesamiento de señales electromiográficas (EMG).
   - Aplicar técnicas de filtrado para limpiar y preparar las señales EMG obtenidas en el laboratorio.
   - Implementar un proceso de segmentación de las señales EMG en diferentes estados musculares: reposo, tensión y Fuerza oponente.
   - Extraer y analizar características relevantes de las señales EMG
     
# 2. Introducción<a name="id2"></a>

## 2.1.Contexto

<p align="justify">
La electromiografía (EMG) es una técnica  que permite captar las señales eléctricas que son obtenidas de las actividades neuromusculares..Estas se pueden recolectar a en la superficie de la piel , debajo de la piel y dentro del músculo [1].
En la actualidad , el EMG se utiliza para diagnóstico  y  monitoreo de lesiones musculares, daños a los nervios y disfunciones musculares que se pueden producir a trastornos neurológicos y musculares, con fines de investigación, para el análisis de la biomecánica de diversos movimientos y el análisis de la marcha, entre otros. [1]
</p> 

<p align="justify">
La electromiografía (EMG) necesita un procesamiento de señal previo a su análisis.Debido a que durante su recorrido a través de diversos tejidos, la señal EMG  adquiere ruido[2]. Además, si la EMG se toma desde la superficie de la piel, puede captar señales de diferentes unidades motoras simultáneamente. Por tanto, un adecuado procesamiento de la señal EMG es crucial para su análisis preciso.
</p> 

<p align="justify">
Es importante conocer las fuentes de ruido que afectan la señal sEMG, las cuales se pueden categorizar en cuatro tipos: ruido inherente, ruido ambiental, artefacto de movimiento, interferencia y ruido interno. [3]   
</p>

1. Ruido Inherente: Este ruido proviene del equipo electrónico, ya que cada equipo electrónico produce ruido.
1. Ruido Ambiental: Este ruido es generado por radiación electromagnética, como la transmisión de televisión, los cables de energía eléctrica y la radio.
1. Artefacto de Movimiento: Este ruido es causado por el movimiento del cable que conecta los electrodos con el circuito amplificador.
1. Interferencia (Cross Talk): Señal no deseada generada por un músculo activo que está cerca del músculo esquelético deseado (músculo objetivo).
1. Ruido Interno: Está relacionado principalmente con la estructura del cuerpo humano, que involucra la profundidad y ubicación de la fibra muscular entre los electrodos de superficie y el músculo activo, así como la cantidad de grasa corporal que aumenta la distancia o separación entre los electrodos de superficie y la fibra muscular activa.

## 2.2.Tratamiento de la Señal
<p align="justify">
Como se mencionó anteriormente  ruido que afectan la señal sEMG, por lo que requiere adecuación antes de ser tratada. Por lo que primero la señal debe pasar por una etapa de amplificación Después de esta amplificación, se siguen los siguientes pasos[4]:
</p> 

## 2.2.1 Pre-procesamiento de la Señal:

### Filtro
<p align="justify">
Es esencial comenzar con una etapa de filtrado para reducir los artefactos en las señales EMG. Usualmente, se emplea un filtro pasa alto para disminuir los efectos de movimiento y la inestabilidad entre los electrodos de superficie y la piel. También se utilizan filtros pasa bajo para registrar datos de estimulación muscular y eliminar interferencias de alta frecuencia. Incluso se puede emplear un filtro pasa banda para optimizar el proceso [4].
</p> 

### Segmentación

<p align="justify">
La segmentación de una señal EMG implica dividir la señal en segmentos más pequeños y manejables para su análisis detallado. Este proceso es esencial para identificar los puntos de inicio y fin de la actividad muscular, y para distinguir entre diferentes estados musculares como contracciones y relajaciones. Los métodos de segmentación pueden variar, utilizando técnicas basadas en el tiempo (como ventanas deslizantes de longitud fija) o en la frecuencia (como transformadas de Fourier) para asegurar que las características importantes de la señal se capturen con precisión​ [5].
</p> 

## 2.2.2 Procesamiento de la Señal:
### Extracción de características:
<p align="justify">
Durante la extracción, el objetivo es obtener información significativa de la señal EMG para su análisis mediante la modificación de los datos originales, lo que resulta en la generación de un vector de características. Este proceso no solo mejora el desempeño del clasificador, sino que también puede disminuir la dimensionalidad, lo que facilita el procesamiento y la clasificación. [6]
</p> 

## 3.Metodología <a name="id3"></a>

<p align="justify">
Para en el proceso de procesamiento de señales EMG, se uso el paper 'Comparison of machine learning algorithms and feature extraction techniques for the automatic detection of surface EMG activation timing'[7].
</p> 

## 3.1 Materiales y Equipos <a name="id4"></a>


|     Modelo       |                  Descripción                  |   Cantidad    |
|  :-------------: |:--------------------------------------------: |:-------------:|
| (R)EVOLUTION     | Kit BITalino                                  | 1             |
| -                | Laptop                                        | 1             |


## 3.2 Procedimiento <a name="id4"></a>
### Señales Adquiridas:
<p align="justify">
En este laboratorio, se emplearán datos de señales EMG recolectados en sesiones previas. La adquisición de estos datos se realizó siguiendo un protocolo estándar utilizando el dispositivo BITalino y el software OpenSignal. Primero, se estableció la conexión entre BITalino y OpenSignal vía Bluetooth para permitir la visualización en tiempo real de las señales. Posteriormente, se conectó el sensor EMG de tres electrodos al BITalino para iniciar la recolección de las señales.
</p> 

<p align="justify">
Estos datos fueron capturados de la señal proveniente de la contracción del músculo  biceps , se evaluaron 3 casos : 
</p> 

- Caso 1: Brazo en reposo
- Caso 2: Levantando una mochila
- Caso 3: Soportando una fuerza oponente

### Pre-procesamiento de la Señal:
#### Elección de filtrado de la señal EMG:

<p align="justify">
El filtrado es esencial para reducir los artefactos en las señales de sEMG. En el curso, se han compararán filtros FIR, IIR y se ha demostrado la efectividad del filtro Wavelet. Sin embargo usando de base el trabajo de, se recomienda el uso de filtros butterworth(n=4) en conjunto a un notch. El filtro pasa-banda de 5-500 Hz y el filtro de Notch de 60 Hz, la combinación de un filtro pasa-banda Butterworth y un filtro notch es altamente efectiva para el procesamiento de señales EMG, centrandonos en eliminar las fuentes de ruido más comunes (artefactos de movimiento, interferencia de línea eléctrica y ruido de alta frecuencia) mientras preservan las características importantes de la señal EMG.
</p> 

#### Segmentación:

<p align="justify">
En el estudio se especifica que el tamaño de la ventana se estableció en 200 ms con un solapamiento del 50%. Esto significa que si la ventana inicial cubre desde el tiempo t0 hasta t0+200 ms, la siguiente ventana comenzará en t0+100 ms y terminará en t0​+300 ms, y así sucesivamente.
</p> 

### Procesamiento de la Señal:
#### Extracción de características:
<p align="justify">
Identificar el mejor conjunto de características puede mejorar el rendimiento de la clasificación y reducir el tiempo necesario para la extracción y clasificación de características. Entre las técnicas comúnmente utilizadas, las que se centran en capturar las principales características de la señal EMG se pueden clasificar en tres tipos: dominio del tiempo, dominio de la frecuencia y una combinación de ambos [7]
En este informe se extraerán parámetros de EMG, tanto del dominio del tiempo como de la frecuencia.

</p> 

### Reposo

<div align="center">
<h2>Señal sin filtro </h2>
</div>

<p align="justify">
Basándonos en los Notebooks de Biosignals, seguimos la guía denominada Parámetros de EMG  y obtuvimos lo siguiente:
</p> 

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/00042809-7b14-4520-af41-9aaf494c4a59" alt="fotog" width="700" height="300"/>
</p>
<p align="center"><i>Figura 1. Detección y contabilidad de activaciones musculares - Reposo</i></p><br>


<p align="justify">
En la gráfica podemos observar que el número de activaciones musculares fue de 3 veces.
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/360929db-2f1f-4a8b-815d-f3e77c2570fa" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 2. Duración Máxima, Mínima y Media de los periodos de activación muscular - Reposo</i></p><br>


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/56f65996-f970-4c06-ae72-378b59fef6d8" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 3. Desviación máxima, mínima, media y estándar de los valores de muestra de EMG - Reposo</i></p><br>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/f46e90c5-a16e-400f-b1e1-169020e30661" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 4. Potencia total y algunos puntos de referencia en el dominio de la frecuencia - Reposo</i></p><br>

### Tensión

### Fuerza oponente

<div align="center">
<h2>Señal sin filtro </h2>
</div>

<p align="justify">
Basándonos en los Notebooks de Biosignals, seguimos la guía denominada Parámetros de EMG  y obtuvimos lo siguiente:
</p> 

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/d4c04c08-effd-4eec-a06f-6fd4b4f42bdd" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 9. Detección y contabilidad de activaciones musculares</i></p><br>

<p align="justify">
En la gráfica podemos observar que el número de activaciones musculares fue de 3 veces.
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/d69964a8-cafb-49ca-832c-1148ac2a48f2" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 10. Duración Máxima, Mínima y Media de los periodos de activación muscular</i></p><br>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/f929ba65-e541-43cd-a485-09e694122e92" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 11. Desviación máxima, mínima, media y estándar de los valores de muestra de EMG</i></p><br>


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/5a9ce3de-81ad-4aa2-9fb0-bd535d8e0438" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 12. Potencia total y algunos puntos de referencia en el dominio de la frecuencia</i></p><br>


## 3.3 Extracción de características <a name="id6"></a>

### Reposo

### Tensión

### Fuerza oponente

# 4. Discusiones <a name="id7"></a>

# 5. Bibliografía <a name="id8"></a>

<p align="justify">
1. N. Sobahi, «Denoising of EMG Signals Based on Wavelet Transform», 2011. Accedido: 25 de mayo de 2024. [En línea]. Disponible en: https://www.semanticscholar.org/paper/Denoising-of-EMG-Signals-Based-on-Wavelet-Transform-Sobahi/8cb86bc29345a607cbef72460464b86f26d4868a.
</p> 
<p align="justify">
2. M. Boyer, L. Bouyer, J.-S. Roy, and A. Campeau-Lecours, “Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review,” Sensors, vol. 23, no. 6, p. 2927, Jan. 2023, doi: https://doi.org/10.3390/s23062927.
</p> 

<p align="justify">
3. M. Prabhashankar, “Impact of Yoga and Meditation on Health,” International Journal of Advanced Research in Science, Communication and Technology (IJARSCT), vol. 11, no. 1, p. 2581, 2020, doi: https://doi.org/10.48175/568.
</p> 

<p align="justify">
4. A. Moreno Sanz, “Procesado Avanzado De Señal EMG,” thesis, Universidad Carlos III De Madrid, Escuela Politécnica superior, Madrid, 2017.” https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content (accessed Sep. 2017).

</p> 

<p align="justify">
5. F. D. Farfán, J. C. Politti, and C. J. Felice, “Evaluation of EMG processing techniques using Information Theory,” BioMedical Engineering OnLine, vol. 9, no. 1, p. 72, 2010, doi: https://doi.org/10.1186/1475-925x-9-72.
</p> 

<p align="justify">
6. A. M. Moslhi, H. H. Aly, and M. ElMessiery, “The Impact of Feature Extraction on Classification Accuracy Examined by Employing a Signal Transformer to Classify Hand Gestures Using Surface Electromyography Signals,” Sensors, vol. 24, no. 4, p. 1259, Jan. 2024, doi: https://doi.org/10.3390/s24041259.
</p> 


<p align="justify">
7. Valentina Mejía Gallón, Stirley Madrid Vélez, J. Ramírez, and F. Bolaños, “Comparison of machine learning algorithms and feature extraction techniques for the automatic detection of surface EMG activation timing,” Biomedical signal processing and control, vol. 94, pp. 106266–106266, Aug. 2024, doi: https://doi.org/10.1016/j.bspc.2024.106266.
</p> 


<p align="justify">
8.«emg_parameters». Accedido: 25 de mayo de 2024. [En línea]. Disponible en: http://notebooks.pluxbiosignals.com/notebooks/Categories/Extract/emg_parameters_rev.html 
</p> 


