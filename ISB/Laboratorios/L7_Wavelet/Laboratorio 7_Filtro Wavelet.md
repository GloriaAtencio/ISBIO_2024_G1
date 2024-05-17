# **Laboratorio N°7: TRANSFORMADA WAVELET**

***

# **Tabla de contenidos**
1. [Objetivos](#id1)
2. [Introducción](#id3)
3. [Metodología](#id4)
   - [Filtro EMG](#id4.1)
   - [Filtro ECG](id4.2)
   - [Filtro EEG](#id4.3)
4. [Resultados](#id5)
5. [Discusión](#id6)
6. [Referencias bibliográficas](#id7) 

***

# 1.Objetivos<a name="id1"></a>
   - Realizar busqueda de literatura sobre los coeficientes de wavelet aplicados a las señales de EMG, ECG y EEG.
   - Diseñar filtros adaptados para cada tipo de señal (EMG, ECG y EEG) con el objetivo de eliminar ruido y artefactos.
   - Analizar las señales filtradas para evaluar la efectividad de los filtros diseñados.
      
# 2.Introducción<a name="id3"></a>

La transformada wavelet (WT) es un método ampliamente utilizado para la supresión de ruido y la extracción de características de señales biomédicas [1]. A menudo se emplea para analizar señales instantáneas y variables en el tiempo. Aunque la transformada de Fourier clásica puede reflejar la connotación general de las señales, su expresión normalmente no es lo suficientemente intuitiva. Como alternativa, la transformada wavelet puede descomponer señales en diferentes escalas, permitiendo seleccionar diferentes niveles de descomposición según los objetivos de procesamiento. Además, permite la localización simultánea en los dominios del tiempo y la frecuencia, lo cual es particularmente ventajoso para el análisis de señales no estacionarias [2].

La metodología de eliminación de ruido mediante la transformada wavelet se basa en la descomposición de señales en una superposición de funciones wavelet. Tras esta descomposición, se generan coeficientes wavelet para cada señal. La distinción entre señal y ruido se realiza mediante ajustes de umbral, donde un umbral adecuado permite conservar los coeficientes de la señal, que son más grandes, y reducir los coeficientes del ruido, que son más pequeños [3].

Actualmente, se han desarrollado muchas bases wavelet, como Haar, Daubechies (Db), Symlet, entre otras, para el análisis y la síntesis de señales. La correcta selección de una función de base wavelet juega un papel crucial en el rendimiento de la eliminación de ruido [2].

Tabla 1: Familia Wavelet [4]


# 3.Metodología<a name="id4"></a>
## 3.1 Filtro EMG<a name="id4.1"></a>
## 3.2 Filtro ECG<a name="id4.2"></a>
## 3.3 Filtro EEG<a name="id4.3"></a>
# 4.Resultados<a name="id5"></a>
### EMG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 2. Basal | ![alt text](imagexx.png)|![alt text](imageXX.png)|
| Figura 3. Levantando Mochila | ![alt text](imagexx.png)| ![alt text](imageXX.png)| 
| Figura 4. Fuerza oponente | ![alt text](image-xx.png)| ![alt text](imageXX.png)| 

<div align="center">
<h2> Coeficientes de Detalle EMG </h2>
</div>

|  ![alt text](imageXX.png) |
### ECG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 2. Reposo | ![alt text](imagexx.png)|![alt text](imageXX.png)|
| Figura 3. Hiperventilación | ![alt text](imagexx.png)| ![alt text](imageXX.png)| 
| Figura 4. Despues de actividad fisica | ![alt text](image-xx.png)| ![alt text](imageXX.png)| 

<div align="center">
<h2> Coeficientes de Detalle EMG </h2>
</div>

|  ![alt text](imageXX.png) |
### EEG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 2. Reposo | ![alt text](imagexx.png)|![alt text](imageXX.png)|
| Figura 3. Hiperventilación | ![alt text](imagexx.png)| ![alt text](imageXX.png)| 
| Figura 4. Despues de actividad fisica | ![alt text](image-xx.png)| ![alt text](imageXX.png)| 

<div align="center">
<h2> Coeficientes de Detalle EMG </h2>
</div>

|  ![alt text](imageXX.png) |
# 5.Discusión<a name="id6"></a>
# 6.Referencias bibliográficas<a name="id7"></a>

