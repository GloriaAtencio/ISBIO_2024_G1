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

## 2.2.Procesamiento de la Señal
<p align="justify">
Como se mencionó anteriormente  ruido que afectan la señal sEMG, por lo que requiere adecuación antes de ser tratada. Por lo que primero la señal debe pasar por una etapa de amplificación Después de esta amplificación, se siguen los siguientes pasos[4]:
</p> 

## 2.2.1 Pre-procesamiento de la Señal:

## Filtro
<p align="justify">
Es esencial comenzar con una etapa de filtrado para reducir los artefactos en las señales EMG. Usualmente, se emplea un filtro pasa alto para disminuir los efectos de movimiento y la inestabilidad entre los electrodos de superficie y la piel. También se utilizan filtros pasa bajo para registrar datos de estimulación muscular y eliminar interferencias de alta frecuencia. Incluso se puede emplear un filtro pasa banda para optimizar el proceso [4].
</p> 

## Segmentación

<p align="justify">
La segmentación de una señal EMG implica dividir la señal en segmentos más pequeños y manejables para su análisis detallado. Este proceso es esencial para identificar los puntos de inicio y fin de la actividad muscular, y para distinguir entre diferentes estados musculares como contracciones y relajaciones. Los métodos de segmentación pueden variar, utilizando técnicas basadas en el tiempo (como ventanas deslizantes de longitud fija) o en la frecuencia (como transformadas de Fourier) para asegurar que las características importantes de la señal se capturen con precisión​ [5].
</p> 

# 3. Metodología <a name="id3"></a>

## 3.1 Materiales y Equipos <a name="id4"></a>


|     Modelo       |                  Descripción                  |   Cantidad    |
|  :-------------: |:--------------------------------------------: |:-------------:|
| (R)EVOLUTION     | Kit BITalino                                  | 1             |
| -                | Laptop                                        | 1             |


## 3.2 Procedimiento <a name="id4"></a>
## Señales Adquiridas:
<p align="justify">
En este laboratorio, se emplearán datos de señales EMG recolectados en sesiones previas. La adquisición de estos datos se realizó siguiendo un protocolo estándar utilizando el dispositivo BITalino y el software OpenSignal. Primero, se estableció la conexión entre BITalino y OpenSignal vía Bluetooth para permitir la visualización en tiempo real de las señales. Posteriormente, se conectó el sensor EMG de tres electrodos al BITalino para iniciar la recolección de las señales.
</p> 

<p align="justify">
Estos datos fueron capturados de la señal proveniente de la contracción del músculo  biceps , se evaluaron 3 casos : 
</p> 

- Caso 1: Brazo en reposo
- Caso 2:Levantando una mochila
- Caso 3:Soportando una fuerza oponente

## Pre-procesamiento de la Señal:
## Elección de filtrado de la señal EMG:

<p align="justify">
El filtrado es esencial para reducir los artefactos en las señales de sEMG. En el curso, se han compararán filtros FIR, IIR y se ha demostrado la efectividad del filtro Wavelet. Sin embargo usando de base el trabajo de, se recomienda el uso de filtros butterworth(n=4) en conjunto a un notch. El filtro pasa-banda de 5-500 Hz y el filtro de Notch de 60 Hz, la combinación de un filtro pasa-banda Butterworth y un filtro notch es altamente efectiva para el procesamiento de señales EMG, centrandonos en eliminar las fuentes de ruido más comunes (artefactos de movimiento, interferencia de línea eléctrica y ruido de alta frecuencia) mientras preservan las características importantes de la señal EMG.
</p> 

## Segmentación:

<p align="justify">
En el estudio se especifica que el tamaño de la ventana se estableció en 200 ms con un solapamiento del 50%. Esto significa que si la ventana inicial cubre desde el tiempo t0 hasta t0+200 ms, la siguiente ventana comenzará en t0+100 ms y terminará en t0​+300 ms, y así sucesivamente.
</p> 



### Reposo

### Tensión

### Fuerza oponente

<p align="justify">
Basándonos en los Notebooks de Biosignals, seguimos la guía denominada Parámetros de EMG  y obtuvimos lo siguiente:
</p> 

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/d4c04c08-effd-4eec-a06f-6fd4b4f42bdd" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 1. Detección y contabilidad de activaciones musculares</i></p><br>

<p align="justify">
En la gráfica podemos observar que el número de activaciones musculares fue de 3 veces.
</p>

## 3.3 Extracción de características <a name="id6"></a>

### Reposo

### Tensión

### Fuerza oponente

# 4. Discusiones <a name="id7"></a>

# 5. Bibliografía <a name="id8"></a>

<p align="justify">
1. N. Sobahi, «Denoising of EMG Signals Based on Wavelet Transform», 2011. Accedido: 25 de mayo de 2024. [En línea]. Disponible en: https://www.semanticscholar.org/paper/Denoising-of-EMG-Signals-Based-on-Wavelet-Transform-Sobahi/8cb86bc29345a607cbef72460464b86f26d4868a
2. M. Boyer, L. Bouyer, J.-S. Roy, and A. Campeau-Lecours, “Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review,” Sensors, vol. 23, no. 6, p. 2927, Jan. 2023, doi: https://doi.org/10.3390/s23062927.

3. M. Prabhashankar, “Impact of Yoga and Meditation on Health,” International Journal of Advanced Research in Science, Communication and Technology (IJARSCT), vol. 11, no. 1, p. 2581, 2020, doi: https://doi.org/10.48175/568.

4. A. Moreno Sanz, “Procesado Avanzado De Señal EMG,” thesis, Universidad Carlos III De Madrid, Escuela Politécnica superior, Madrid, 2017.” https://e-archivo.uc3m.es/rest/api/core/bitstreams/73de4212-e068-4610-9dca-4cf450e3fd9e/content (accessed Sep. 2017).

5. F. D. Farfán, J. C. Politti, and C. J. Felice, “Evaluation of EMG processing techniques using Information Theory,” BioMedical Engineering OnLine, vol. 9, no. 1, p. 72, 2010, doi: https://doi.org/10.1186/1475-925x-9-72.
</p> 
