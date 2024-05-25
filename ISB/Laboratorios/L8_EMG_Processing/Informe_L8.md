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

## 3.3 Extracción de características <a name="id6"></a>

### Reposo

### Tensión

### Fuerza oponente

# 4. Discusiones <a name="id7"></a>

# 5. Bibliografía <a name="id8"></a>
