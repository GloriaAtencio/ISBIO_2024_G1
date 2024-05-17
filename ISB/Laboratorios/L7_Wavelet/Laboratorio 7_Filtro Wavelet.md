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
 
<p align="justify">
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/tabla1.jpeg" alt="fotog" width="520" height="300"/>
</p> 
<p align="center">
Tabla 1: Familia Wavelet [4]
</p> 

# 3.Metodología<a name="id4"></a>
## 3.1 Diseño del filtro para EMG<a name="id4.1"></a>
Onda Madre: Las wavelets Daubechies, como db2, db4, db6 y db8, son comúnmente utilizadas para el procesamiento de señales biomédicas debido a su capacidad para manejar señales no estacionarias y capturar características transitorias de la señal EMG. Estas wavelets tienen formas que son similares a las de los potenciales de acción de unidad motora (MUAP), lo que las hace especialmente adecuadas para este tipo de análisis. Asimismo, al ser ortogonales, lo facilitan la reconstrucción de la señal sin pérdida de información. Para este caso específico se utilizará db8, la mayor longitud de soporte permite a la db8 capturar características más detalladas de la señal EMG, lo cual es beneficioso para el análisis de señales con estructuras complejas y transitorias. Esto resulta en una mejor representación de las variaciones rápidas y detalles finos en la señal.
Nivel de Descomposición: Para señales EMG, que típicamente tienen frecuencias de muestreo en el rango de kHz, los niveles de descomposición usualmente varían entre 4 y 6. Esto permite capturar tanto los movimientos musculares generales (bajas frecuencias) como los picos de actividad muscular (altas frecuencias). Se trabaja con un nivel 5 estándar a las otras señales, un nivel demasiado bajo podría perder detalles importantes, mientras que un nivel demasiado alto podría introducir ruido [2].
Umbralización: El proceso descrito implica que los coeficientes cuya magnitud está por debajo del umbral se fijan en cero, lo cual es la característica distintiva de la umbralización dura. Se está tomando la forma universal, como tal se describe que este método está diseñado específicamente para manejar situaciones en las que la señal de interés está contaminada con ruido gaussiano, y su principal objetivo es minimizar el error de reconstrucción.

## 3.2 Diseño del filtro para ECG<a name="id4.2"></a>

Para aplicar la transformada de wavelet con el objetivo de eliminar ruidos de la señal de ECG, se deben considerar varios aspectos clave. Entre ellos, la determinación del número de capas de descomposición de las ondas influye significativamente en la efectividad de la eliminación del ruido. A continuación, se describen los parámetros esenciales para este proceso: la selección de la onda madre, el nivel de descomposición y el método de umbralización.

- Onda Madre: La selección correcta de una función de base wavelet es crucial para el rendimiento en la eliminación de ruido. La Tabla 2 muestra la comparación de la relación señal-ruido (SNR) y el error cuadrático medio (MSE) de las señales de ECG sin ruido, procesadas mediante varias ondas típicas. Según esta tabla, la SNR de la wavelet db5 es relativamente alta y el MSE es relativamente bajo [2]. Por lo tanto, basándonos en esta evidencia, seleccionamos db5 como la base wavelet para el proceso de eliminación de ruido de la señal de ECG en este informe.
  
<p align="justify">
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/tabla2.jpeg" alt="fotog" width="520" height="300"/>
</p> 
<p align="center">
Tabla 2: Comparación de los resultados de eliminación de ruido según varias ondas típicas.[2]
</p> 

- Nivel de Descomposición: El número de capas de descomposición también es un factor crítico. Si el número de capas es demasiado pequeño, el efecto de eliminación de ruido será insatisfactorio. Generalmente, para eliminar el ruido de alta frecuencia y extraer componentes de baja frecuencia, el número de capas de descomposición se incrementa hasta cierto punto. Sin embargo, si el número de capas es demasiado alto, el error puede aumentar considerablemente. Esto se debe a que el proceso se centra más en las características de la base wavelet que en la señal que se está analizando, lo que puede resultar en frecuencias falsas y una pérdida significativa de información [2].

- Umbralización: La selección del método de umbralización adecuado es fundamental, independientemente de la función wavelet que se utilice. Existen varias técnicas de umbralización que presentan buenos resultados, como MINMAX, RIGOROUS SURE, UNIVERSAL y HEURISTIC SURE [5]. En este informe, se utilizará el umbral universal dado por "sqrt(2 * log(N))", donde N es la longitud de la señal.

## 3.3 Diseño del filtro para EEG<a name="id4.3"></a>
# 4.Resultados<a name="id5"></a> 
### EMG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Basal| <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETB1.png" alt="fotog" width="350" height="270"/> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETB2.png" alt="fotog" width="350" height="270" /> | 
|Levantando mochila | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETM1.png" alt="fotog" width="350" height="270" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETM2.png" alt="fotog" width="350" height="270" /> |
| Fuerza oponente | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETO1.png" alt="fotog" width="350" height="270" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETO2.png" alt="fotog" width="350" height="270" /> |

<div align="center">
<h2> Coeficientes de Detalle EMG </h2>
</div>

|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" /> |
### ECG

Las señales de electrocardiograma (ECG) fueron adquiridas durante diferentes condiciones experimentales: en estado basal (reposo), en estado de hiperventilación y después de ejercicio. A continuación, se presenta la señal cruda para cada uno de estos estados y la señal filtrada para reducir el ruido, utilizando la transformada wavelet previamente parametrizada.

| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Reposo| <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/reposo1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/reposo2.png" alt="fotog" /> | 
| Hiperventilación | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/hiperventilacion1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/hiperventilacion2.png" alt="fotog" /> |
| Despues de actividad fisica | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/ejercicio1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/ejercicio2.png" alt="fotog" /> |

### EEG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Reposo | ![alt text](imagexx.png)|![alt text](imageXX.png)|
| Hiperventilación | ![alt text](imagexx.png)| ![alt text](imageXX.png)| 
| Despues de actividad fisica | ![alt text](image-xx.png)| ![alt text](imageXX.png)| 

# 5.Discusión<a name="id6"></a>

### EMG
### ECG
La transformada wavelet(WT) se ha demostrado como una herramienta eficaz debido a su capacidad de descomponer señales en diferentes escalas, lo que es particularmente útil para el análisis de señales no estacionarias como las de ECG.
Los resultados experimentales muestran que la aplicación de la transformada wavelet con la onda db5 y el umbral universal mejora significativamente la calidad de las señales de ECG. Las señales adquiridas en diferentes condiciones (reposo, hiperventilación, post-ejercicio) muestran una reducción notable del ruido después del procesamiento. Esto confirma la eficacia del método propuesto para mejorar la claridad y la utilidad de las señales de ECG para el análisis clínico. Además, la correcta elección del número de capas de descomposición es crucial, ya que un número demasiado bajo podría resultar en una insuficiente eliminación de ruido, mientras que un número demasiado alto podría introducir artefactos y pérdida de información. Este balance es esencial para preservar la integridad de la señal de ECG, un aspecto que ha sido resaltado en la literatura como fundamental para el análisis clínico preciso. Una señal de ECG más clara puede facilitar diagnósticos más precisos y confiables, lo que es crucial en contextos clínicos donde las decisiones deben ser rápidas y basadas en datos precisos.
### EEG
# 6.Referencias bibliográficas<a name="id7"></a>

[1] D. Vilimek et al., “Comparative analysis of wavelet transform filtering systems for noise reduction in ultrasound images”, PLOS ONE, vol. 17, n.º 7, julio de 2022, art. n.º e0270745. Accedido el 17 de mayo de 2024.[Online]. Available:  https://doi.org/10.1371/journal.pone.0270745 

[2]D. Zhang et al., "An ECG Signal De-Noising Approach Based on Wavelet Energy and Sub-Band Smoothing Filter," Appl. Sci., vol. 9, no. 22, p. 4968, 2019.Accedido el 17 de mayo de 2024 [Online]. Available: https://doi.org/10.3390/app9224968 

[3]S. Su et al., “An ECG Signal Acquisition and Analysis System Based on Machine Learning with Model Fusion”, Sensors, vol. 23, n.º 17, p. 7643, septiembre de 2023. Accedido el 17 de mayo de 2024. [Online]. Available:https://doi.org/10.3390/s23177643 

[4] D. M., A. E., and L. F., ‘Discrete Wavelet Transform in Compression and Filtering of Biomedical Signals’, Discrete Wavelet Transforms - Biomedical Applications. InTech, Sep. 12, 2011. doi: 10.5772/19529. 

[5] https://ieeexplore.ieee.org/document/5728090
