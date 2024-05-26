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
La electromiografía (EMG) necesita un procesamiento de señal previo a su análisis.Debido a que durante su recorrido a través de diversos tejidos, la señal EMG  adquiere ruido.[2] Además, si la EMG se toma desde la superficie de la piel, puede captar señales de diferentes unidades motoras simultáneamente. Por tanto, un adecuado procesamiento de la señal EMG es crucial para su análisis preciso.
</p> 

# 3. Metodología <a name="id3"></a>

## 3.1 Filtrado <a name="id4"></a>

## Elección de filtrado de la señal EMG:

<p align="justify">
En nuestro caso decidimos utilizar el filtro Wavelet que se encarga de darnos una versión menos ruidosa de la señal , en este caso el filtro wavelet aplicado fue el db8.
</p> 

<div align="center">
<h2>Filtro Wavelet db8</h2>
</div>

<p align="justify">
Conocida como db8 , la wavelet Daubechies 8 (db8), forma parte de una de las tantas wavelets que normalmente son aplicadas para quitar ruido en señales biomédicas entre ellas se encuentran : db2,db8 y db6.
</p> 

<p align="justify">
La denoising de señales electromiográficas de superficie (sEMG) es crucial para mejorar la precisión y la interpretación de los datos recogidos. Uno de los métodos más eficaces para este propósito es el uso de la Transformada de Wavelet Discreta (DWT) junto con un método de umbral..
</p> 

<p align="justify">
En el paper “Denoising of EMG Signals Based on Wavelet Transform” , La función wavelet utilizada actúa como un filtro, determinando la resolución y la escala de los componentes descompuestos mediante operaciones de submuestreo y sobremuestreo.. Asimismo, se usa el método del umbral que es aplicado a la transformada de la señal. Los valores de la transformada de la señal original, cuya magnitud es mayor que un umbral ( Ts) , capturan efectivamente la energía de la señal. En contraste, los valores de la transformada del ruido, cuya magnitud es inferior a un umbral de ruido (Tn) , se reducen a cero. Esto permite eliminar el ruido de la señal transformada al aplicar el umbral adecuado.[1]
</p> 


## 3.2 Segmentación <a name="id5"></a>

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
</p> 
