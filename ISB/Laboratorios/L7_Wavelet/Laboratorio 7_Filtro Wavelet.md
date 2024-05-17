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

Para aplicar la transformada de wavelet con el objetivo de eliminar ruidos de la señal de ECG, se deben considerar varios aspectos clave. Entre ellos, la determinación del número de capas de descomposición de las ondas influye significativamente en la efectividad de la eliminación del ruido. A continuación, se describen los parámetros esenciales para este proceso: la selección de la onda madre, el nivel de descomposición y el método de umbralización.

- Onda Madre: La selección correcta de una función de base wavelet es crucial para el rendimiento en la eliminación de ruido. La Tabla 2 muestra la comparación de la relación señal-ruido (SNR) y el error cuadrático medio (MSE) de las señales de ECG sin ruido, procesadas mediante varias ondas típicas. Según esta tabla, la SNR de la wavelet db5 es relativamente alta y el MSE es relativamente bajo [2]. Por lo tanto, basándonos en esta evidencia, seleccionamos db5 como la base wavelet para el proceso de eliminación de ruido de la señal de ECG en este informe.

Tabla 2: Comparación de los resultados de eliminación de ruido según varias ondas típicas.
- Nivel de Descomposición: El número de capas de descomposición también es un factor crítico. Si el número de capas es demasiado pequeño, el efecto de eliminación de ruido será insatisfactorio. Generalmente, para eliminar el ruido de alta frecuencia y extraer componentes de baja frecuencia, el número de capas de descomposición se incrementa hasta cierto punto. Sin embargo, si el número de capas es demasiado alto, el error puede aumentar considerablemente. Esto se debe a que el proceso se centra más en las características de la base wavelet que en la señal que se está analizando, lo que puede resultar en frecuencias falsas y una pérdida significativa de información [2].

- Umbralización: La selección del método de umbralización adecuado es fundamental, independientemente de la función wavelet que se utilice. Existen varias técnicas de umbralización que presentan buenos resultados, como MINMAX, RIGOROUS SURE, UNIVERSAL y HEURISTIC SURE [5]. En este informe, se utilizará el umbral universal dado por `sqrt(2 * log(N)), donde N es la longitud de la señal.

## 3.3 Filtro EEG<a name="id4.3"></a>
# 4.Resultados<a name="id5"></a> 
### EMG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 2. Basal |  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETB1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETB2.png" alt="fotog" /> |
| Figura 3. Levantando Mochila |  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> |  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> | 
| Figura 4. Fuerza oponente |  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> | 

<div align="center">
<h2> Coeficientes de Detalle EMG </h2>
</div>

|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> |
### ECG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 2. Reposo| <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg_same_Axis.png" alt="fotog" /> | 
| Figura 3. Hiperventilación | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg_same_Axis.png" alt="fotog" /> |
| Figura 4. Despues de actividad fisica | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg_same_Axis.png" alt="fotog" /> |

<div align="center">
<h2> Coeficientes de Detalle ECG </h2>
</div>

|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg_same_Axis.png" alt="fotog" /> | 
### EEG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 2. Reposo | ![alt text](imagexx.png)|![alt text](imageXX.png)|
| Figura 3. Hiperventilación | ![alt text](imagexx.png)| ![alt text](imageXX.png)| 
| Figura 4. Despues de actividad fisica | ![alt text](image-xx.png)| ![alt text](imageXX.png)| 

<div align="center">
<h2> Coeficientes de Detalle EEG </h2>
</div>

|  ![alt text](imageXX.png) |
# 5.Discusión<a name="id6"></a>
### EMG
### ECG
### EEG
# 6.Referencias bibliográficas<a name="id7"></a>

