# **Laboratorio N°9: Caracterización de señal ECG**

***

# **Tabla de contenidos**
1. [Objetivos](#id1)
2. [Introducción](#id3)
3. [Metodología](#id4)
   - [Aplicación de filtro](#id3.1)
   - [Detección de picos](id3.2)
   - [Análisis de HRV](#id3.3)
4. [Resultados](#id4)
    - [Aplicación de filtro wavelet Sym5](#id4.1)
    - [Detección de picos R](#id4.2)
    - [Parámetros HRV](#id4.3)
   
6. [Discusión](#id5)
7. [Referencias bibliográficas](#id6) 

***

# 1.Objetivos<a name="id1"></a>
<p align="justify">
- Detectar los picos de la onda R que se encuentran en las señales ECG obtenidas previamente.
 </p>

 <p align="justify">
- Elaborar gráfica que permita visualizar todos los picos encontrados y hacer una discusión respecto la aparición de estos.
 </p>

 <p align="justify">
- Hallar la variabilidad del ritmo cardíaco (HRV) basandonos en un artículo base de nuestra elección.
 </p> 
 
# 2.Introducción<a name="id2"></a>

<div align="center">
<h2> Electrocardiograma  </h2>
</div>

<p align="justify">
El electrocardiograma (ECG) es una prueba médica que registra la actividad eléctrica del corazón a lo largo del tiempo. Utiliza electrodos colocados en la piel para captar las señales eléctricas generadas por el corazón. Estas señales se representan gráficamente, lo que permite a los profesionales de la salud evaluar el ritmo cardíaco, detectar irregularidades y diagnosticar diversas afecciones cardíacas. Es una herramienta crucial en cardiología y se utiliza tanto para diagnósticos rutinarios como en situaciones de emergencia.
</p> 

<div align="center">
<h2> Pico R  </h2>
</div>

<p align="justify">
El pico R en el electrocardiograma (ECG) es un punto clave en la evaluación de la actividad eléctrica del corazón, específicamente en la medición del tiempo de activación ventricular (TAV) o tiempo al pico R. Este intervalo se mide desde el inicio del complejo QRS hasta el pico máximo de la onda R o R', y refleja el tiempo necesario para la activación eléctrica desde el endocardio hasta el epicardio. En condiciones normales, el tiempo al pico R varía según la pared ventricular y el tipo de derivación utilizada: para el ventrículo derecho, se mide en las derivaciones V1 o V2 con un límite superior de 35 ms, mientras que para el ventrículo izquierdo, se mide en las derivaciones V5 o V6 con un límite de 45 ms. Esta medición es esencial para el diagnóstico de diversas condiciones cardíacas y proporciona información crítica sobre la conducción eléctrica del corazón.[1]
</p> 


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/8f3df861-76be-40f3-86c8-333396259770" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 1. Forma de un electrocardiograma (ECG) en un paciente normal[2]</i></p><br>

<div align="center">
<h2> HRV  </h2>
</div>

<p align="justify">
La variabilidad de la frecuencia cardíaca (HRV) es la variación fisiológica del intervalo entre latidos consecutivos del corazón, influenciada por la actividad del sistema nervioso autónomo. La HRV se ha convertido en una herramienta diagnóstica crucial en la última década, permitiendo la evaluación de diversas condiciones clínicas y funcionales. Tradicionalmente, el análisis de la HRV se realiza mediante los intervalos entre latidos obtenidos a partir de las ondas R en electrocardiogramas (ECG). Esta técnica proporciona información valiosa sobre el estado del sistema nervioso autónomo y la salud cardiovascular, siendo utilizada en la detección de arritmias, la evaluación del estrés y la predicción de eventos cardíacos adversos. La creciente precisión y accesibilidad de los sensores ha ampliado su aplicación, consolidándose como un componente esencial en la cardiología moderna.[3]
</p> 

# 3.Metodología<a name="id3"></a>

## 3.1. Aplicación de filtro<a name="id3.1"></a>

<p align="justify">
En la señal de electrocardiograma (ECG), la aplicación de filtros es una etapa crucial para la eliminación de ruido y la mejora de la calidad de la señal antes del análisis. Tradicionalmente, se utilizan filtros pasa banda como los filtros Chebyshev tipo I y Butterworth para este propósito. Sin embargo, en métodos más avanzados, la transformada wavelet discreta (DWT) se emplea para una compresión y reducción de ruido más efectiva.
</p> 

<p align="justify">
La DWT descompone la señal ECG en componentes de detalle y aproximación, aplicando un umbral suave para eliminar el ruido en los coeficientes de detalle y luego reconstruir la señal limpia. Este proceso no solo reduce el tamaño de la señal, sino que también mejora la precisión y eficiencia en la detección de picos R, fundamentales para el análisis de la variabilidad de la frecuencia cardíaca y otras características cardíacas.[4]
</p>


<p align="justify">
Nosotros nos basaremos en el paper titulado "R Peak Detection Method Using Wavelet Transform and Modified Shannon Energy Envelope", en el cual los autores proponen un método innovador para la detección de picos R en señales de ECG que se basa en la transformada wavelet (WT) y la envolvente de energía de Shannon modificada (SEE). Este método reemplaza los tradicionales filtros de paso de banda con la transformada wavelet discreta (DWT) para reducir el tamaño y el ruido de las señales de ECG, lo que resulta en una mejora en la precisión y la eficiencia del proceso de detección de picos R.[5]
</p>

<p align="justify">
El procedimiento comienza aplicando la DWT a la señal de ECG utilizando la wavelet Symlet 5 (sym5). Esta elección permite una descomposición efectiva de la señal en coeficientes de aproximación (AC) y coeficientes de detalle (DC). Luego, se aplica un umbral suave a los coeficientes de detalle para eliminar el ruido, utilizando un valor de umbral calculado según la fórmula t=σ*(√(2log(n))/n), donde σ es la desviación estándar del ruido y n es el número total de coeficientes wavelet.[5]
</p>

<p align="justify">
La Symlet 5 (sym5) es una wavelet perteneciente a la familia de las Symlets, que son una modificación de las wavelets Daubechies, diseñadas por Ingrid Daubechies para mejorar ciertas características de simetría. Las wavelets Symlets son conocidas por su capacidad para proporcionar una reconstrucción precisa de la señal y por su forma casi simétrica, lo que reduce los artefactos en el procesamiento de señales. La sym5, en particular, es ampliamente utilizada en la descomposición y reconstrucción de señales debido a su capacidad para capturar tanto las características de alta como de baja frecuencia en la señal original, lo que la hace ideal para aplicaciones como la eliminación de ruido en señales electrocardiográficas (ECG). Al equilibrar la complejidad computacional con la precisión en la representación de la señal, la sym5 se posiciona como una herramienta valiosa en el procesamiento avanzado de señales, permitiendo una análisis más claro y preciso de los datos adquiridos de forma natural.[6]
</p>



## 3.2. Detección de picos<a name="id3.2"></a>

<p align="justify">
En el paper seleccionado se explica que el proceso de detección de picos R comienza con la transformada wavelet para reducir el tamaño y el ruido de las señales de ECG. Luego, se aplica una diferenciación de primer orden y una normalización de amplitud para calcular la energía de Shannon (SE). Posteriormente, la envolvente de energía de Shannon (SEE) se extrae mediante un filtro de media móvil, lo que suaviza la señal y elimina los picos no deseados.[5]
</p>

<p align="justify">
Una vez obtenida la SEE, se realiza una diferenciación y normalización adicional, seguida de una operación de cuadratura para amplificar los picos verdaderos y atenuar los picos falsos. La señal resultante pasa nuevamente por un filtro de media móvil para obtener una envolvente de energía máxima (PEE) más clara.[5]
</p>

<p align="justify">
Los picos R se detectan mediante la identificación de los picos ascendentes en la PEE, sin necesidad de umbrales de amplitud específicos. Se aplica un algoritmo de búsqueda de picos para localizar los picos estimados y ajustar sus posiciones buscando la máxima amplitud dentro de un rango de ±25 muestras en la señal de ECG original.[5]
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/b4287e51-96ef-429a-90a7-8f2ad1cb9553" alt="fotog" width="180" height="80"/>
</p>
<p align="center"><i>Figura 2.Función de búsqueda de picos a partir de PEE [5]</i></p><br>

<p align="justify">
Finalmente, los picos R detectados se validan y actualizan en función de los intervalos RR entre picos vecinos. Este procedimiento asegura la detección precisa de los picos R verdaderos, equilibrando los intervalos RR y eliminando posibles falsos positivos o negativos. Este enfoque basado en la transformada wavelet y la envolvente de energía de Shannon modificada permite una detección robusta y precisa de los picos R en señales de ECG ruidosas.[5]
</p>

<p align="justify">
Para este laboratorio, decicidimos inicialmente guiarnos por el paper menconado pero tuvimos que adaptarlo al lenguaje python para poder seguir todos los pasos. Es por ello que no se usó la función findPeaks porque esta solo podía ser usada en MATLAB.Asimismo, decidimos complementar la detección de los picos usando como guía alterna el notebook "Event Detection - R Peaks (ECG)" de biosignals.[7]
</p>



## 3.3. Análisis de HRV<a name="id3.3"></a>

<p align="justify">
Para analizar la variabilidad de la frecuencia cardíaca (HRV) a partir de señales de ECG, se siguió un enfoque sistemático utilizando el paquete biosignalsnotebooks junto con otras bibliotecas científicas. El primer paso fue la importación de los paquetes necesarios para la manipulación y procesamiento de los datos de señal, tales como biosignalsnotebooks para la carga de datos y bibliotecas como numpy y scipy para operaciones matemáticas y estadísticas.
</p>

<p align="justify">
Una vez importados los paquetes, se procedió a cargar los datos de ECG adquiridos, obteniendo tanto la señal como el encabezado que contiene información crucial como la frecuencia de muestreo. Identificamos el canal utilizado durante la adquisición para asegurarnos de que los datos procesados sean los correctos.Luego, almacenamos la frecuencia de muestreo y los datos de la señal en variables específicas para facilitar su manipulación posterior. Se generó un tacograma, que constituye la estructura fundamental desde donde se extraerán todos los parámetros de HRV.[8]
</p>

<p align="justify">
Se realizó una limpieza de los datos removiendo los latidos ectópicos, que se definen como ciclos cardíacos cuya duración difiere en al menos un 20% del ciclo anterior. Esto garantiza la precisión de los análisis posteriores.Para la extracción de los parámetros de HRV, se calcularon primero los parámetros de tiempo, como los intervalos RR máximos, mínimos y promedio, así como la frecuencia cardíaca máxima, mínima y promedio. También se calculó la desviación estándar de los intervalos RR (SDNN), un indicador clave de la variabilidad de la frecuencia cardíaca.[8]
</p>

<p align="justify">
En cuanto a los parámetros de Poincaré, se calcularon SD1 y SD2, que se derivan de la desviación estándar de las diferencias entre intervalos RR consecutivos, proporcionando una visión más profunda de la variabilidad y complejidad de la frecuencia cardíaca.Para los parámetros de frecuencia, se utilizó el espectro de potencia para calcular la potencia en diferentes bandas de frecuencia (ULF, VLF, LF, y HF). Este análisis permite entender cómo se distribuye la energía de la variabilidad de la frecuencia cardíaca en diferentes rangos de frecuencia.[8]
</p>

<p align="justify">
Finalmente, se calcularon parámetros adicionales como NN20, pNN20, NN50 y pNN50, que representan la cantidad y porcentaje de intervalos RR que difieren del anterior en al menos 20 ms y 50 ms, respectivamente. Esto proporciona información adicional sobre la regularidad y estabilidad de los intervalos cardíacos.Para simplificar y automatizar el proceso, se utilizó la función hrv_parameters del módulo extract de biosignalsnotebooks, que realiza la extracción de todos estos parámetros de manera eficiente. Este enfoque metodológico nos permitió obtener una visión integral y detallada de la variabilidad de la frecuencia cardíaca a partir de señales de ECG, sentando las bases para análisis más profundos y aplicaciones clínicas.[8]
</p>

# 4.Resultados<a name="id4"></a>

## 4.1. Aplicación de filtro wavelet Sym5<a name="id4.1"></a>

<p align="justify">
Se aplicó el filtro wavelet Sym5 y se halló el umbral a partir de la siguiente ecuación:
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/48183e7a-319d-4ed1-b6f9-bd022b2c2124" alt="fotog" width="180" height="100"/>
</p>
<p align="center"><i>Figura 3.Método de selección de umbral universal [5]</i></p><br>


<p align="justify">
Donde N es el número total de coeficientes wavelet y σ se calcula como la mediana del valor absoluto de los coeficientes de detalle dividida por 0.6745, representando así la desviación estándar del ruido.
</p>

<div align="center">
<h2> ECG - Reposo </h2>
</div>

|  **Señal original - ploteada por tiempo**  | **Señal filtrada - ploteada por tiempo** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/1fb6ebae-bb4f-43aa-b60a-ff129f483141" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/b39a229b-149b-42e7-982f-a7ee9746bfd8" alt="fotog" />|

<div align="center">
<h2> ECG - Hiperventilación </h2>
</div>

|  **Señal original - ploteada por tiempo**  | **Señal filtrada - ploteada por tiempo** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/7e74de21-2581-4374-9c5f-a3591c34fe4a" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/fa1c7227-1a40-4a47-be4b-a076dbe7edb3" alt="fotog" />|


<div align="center">
<h2> ECG - Después de actividad física </h2>
</div>

|  **Señal original - ploteada por tiempo**  | **Señal filtrada - ploteada por tiempo** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/eef7f25f-f61a-4c1d-a881-0d25e2a4bfa5" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/4789fa85-cb57-45b9-b03e-131779ecb7f6" alt="fotog" />|

## 4.2. Detección de picos R<a name="id4.2"></a>

<p align="justify">
Al principio se propusó detectar los picos mediante la identificación de los picos ascendentes en la envolvente de energía máxima (PEE), en la cual los picos con menor amplitud representabn a los picos R falsos y los picos con una amplitud mucho mayor representarían los picos R verdaderos. No obstante, al aplicar todo el procedimiento que se realizó en el paper y adaptarlo al código en lenguaje Python; se obtuvieron resultados poco deseables que no detectaban los pico de nuestro interés(observar Figura 4). Debido a esto decidimos guiarnos por el notebook biosignals y usamos la función detect_r_peaks para hallar los picos R presentes en la señal ECG filtrada.

</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/d4c685f8-df46-4b3c-89a6-f205f21b770b" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 4. Detección de picos R usando mediante el PEE en la señal ECG durante hiperventilación</i></p><br>

<div align="center">
<h2> ECG - Reposo </h2>
</div>
 
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/bb4ab336-4d4f-4c88-93e7-57aff5d1ed18" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 5. Detección de picos R usando detect_r_peaks en la señal ECG durante reposo</i></p><br>

<div align="center">
<h2> ECG - Hiperventilación </h2>
</div>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/936c8145-52d9-4e83-8010-b7607925ac15" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 6. Detección de picos R usando detect_r_peaks en la señal ECG durante hiperventilación</i></p><br>


<div align="center">
<h2> ECG - Después de actividad física </h2>
</div>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/14de0865-275d-4155-9560-3853db794a6e" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 7. Detección de picos R usando detect_r_peaks en la señal ECG después de actividad física</i></p><br>

## 4.3. Parámetros HRV<a name="id4.3"></a>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/89539957/f9b349a8-c4d6-44fd-be9a-0525752e78aa" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 8. Tacograma con parámetros de calculados en la señal ECG durante reposo</i></p><br>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/89539957/676db3f3-03f2-4aef-977e-dd11c28faac3" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 9. Tacograma con parámetros de calculados en la señal ECG durante hiperventilación</i></p><br>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/89539957/7f34a1b2-63c4-4e70-8750-4fc954f46538" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 10. Tacograma con parámetros de calculados en la señal ECG después de actividad física</i></p><br>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/89539957/1a2d58d2-5eff-4c64-a9b7-12880b68e63b" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 11. BPM con parámetros de calculados en la señal ECG durante reposo</i></p><br>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/89539957/8058e5c6-c8c9-4dbc-aa5e-b7f111fab348" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 12. BPM con parámetros de calculados en la señal ECG durante hiperventilación</i></p><br>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/89539957/50dc1534-7373-4b32-97cc-4e5c774acbdb" alt="fotog" width="600" height="350"/>
</p>
<p align="center"><i>Figura 13. BPM con parámetros de calculados en la señal ECG después de actividad física</i></p><br>

# 5.Discusión<a name="id5"></a>


## Análisis de Filtrado Wavelet Sym5 /Gráficas de ECG Original y Filtrada:

- ECG en Reposo: La gráfica muestra una señal ECG en reposo con ruido base. Al aplicar el filtro wavelet Sym5, la señal resultante es más limpia, con los picos R (QRS) claramente definidos, lo que facilita su análisis.
<p > 
- ECG en Hiperventilación: En esta condición, la señal ECG presenta mayor ruido y variabilidad debido al ritmo respiratorio elevado. El filtro wavelet Sym5 sigue demostrando una eficiencia notable en la limpieza de la señal, permitiendo una mejor observación de los picos R.
</p>

<p > 
- ECG Después de Actividad Física: La señal ECG post-ejercicio es más ruidosa y muestra una mayor frecuencia de picos R. El filtrado wavelet Sym5 reduce significativamente el ruido, resaltando los picos R pese al aumento de la actividad.
</p>

# Discusión de las Gráficas

En base al informe actualizado, se ha agregado una serie de nuevas gráficas que amplían y detallan el análisis del procesamiento de señales ECG bajo diversas condiciones. A continuación se presenta una discusión de estos nuevos gráficos:

## Análisis de Filtrado Wavelet Sym5

### Gráficas de ECG Original y Filtrada:
- **ECG en Reposo:** La gráfica muestra una señal ECG en reposo con ruido base. Al aplicar el filtro wavelet Sym5, la señal resultante es más limpia, con los picos R (QRS) claramente definidos, lo que facilita su análisis.
- **ECG en Hiperventilación:** En esta condición, la señal ECG presenta mayor ruido y variabilidad debido al ritmo respiratorio elevado. El filtro  sigue demostrando una eficiencia notable en la limpieza de la señal, permitiendo una mejor observación de los picos R.
- **ECG Después de Actividad Física:** La señal ECG post-ejercicio es más ruidosa y muestra una mayor frecuencia de picos R. El filtrado wavelet Sym5 reduce significativamente el ruido, resaltando los picos R pese al aumento de la actividad.

## Detección de Picos R

### Gráficas de Detección de Picos R:
- **ECG en Reposo:** La detección de picos R se presenta con alta precisión, identificando correctamente los picos R y minimizando los falsos positivos.
- **ECG en Hiperventilación:** La gráfica de detección de picos R durante la hiperventilación muestra un aumento en la frecuencia cardíaca, con detecciones consistentes y precisas.
- **ECG Después de Actividad Física:** Tras la actividad física, la detección de picos R muestra un ritmo cardíaco acelerado. La metodología empleada sigue siendo eficaz, mostrando la capacidad del algoritmo para manejar condiciones de alta variabilidad y ruido.

## Análisis Espectral

### Análisis de Frecuencia:
- **Espectrograma en Reposo:** El espectrograma de la señal ECG en reposo muestra una distribución de frecuencia predominante en rangos bajos, correspondiente al ritmo cardíaco en reposo.
- **Espectrograma en Hiperventilación:** Durante la hiperventilación, el espectrograma muestra un incremento en las frecuencias debido al aumento en el ritmo respiratorio y cardíaco.
- **Espectrograma Post-Ejercicio:** La gráfica espectral post-ejercicio muestra una amplia distribución de frecuencias, reflejando la variabilidad y la alta frecuencia del ritmo cardíaco tras la actividad física.


## Conclusión

La combinación de filtrado wavelet Sym5 y el análisis espectral proporciona un enfoque comprensivo para la mejora y análisis de señales ECG, crucial para aplicaciones clínicas y de investigación en el monitoreo de la salud cardíaca.

# 6.Referencias bibliográficas<a name="id6"></a>
<p align="justify">
[1] A. R. Pérez-Riera, L. C. de Abreu, R. Barbosa-Barros, K. C. Nikus, y A. Baranchuk, «R-Peak Time: An Electrocardiographic Parameter with Multiple Clinical Applications», Ann Noninvasive Electrocardiol, vol. 21, n.º 1, pp. 10-19, ene. 2016, doi: 10.1111/anec.12323.
</p> 

<p align="justify">
[2] U. Zalabarria, E. Irigoyen, R. Martinez, y A. Lowe, «Online robust R-peaks detection in noisy electrocardiograms using a novel iterative smart processing algorithm», Applied Mathematics and Computation, vol. 369, p. 124839, mar. 2020, doi: 10.1016/j.amc.2019.124839.
</p> 
   
<p align="justify">
[3] S. Sieciński, P. S. Kostka, y E. J. Tkacz, «Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers», Sensors (Basel), vol. 20, n.º 16, p. 4522, ago. 2020, doi: 10.3390/s20164522.
</p> 

<p align="justify">
[4] A. R. Pérez-Riera, L. C. de Abreu, R. Barbosa-Barros, K. C. Nikus, y A. Baranchuk, «R-Peak Time: An Electrocardiographic Parameter with Multiple Clinical Applications», Ann Noninvasive Electrocardiol, vol. 21, n.º 1, pp. 10-19, ene. 2016, doi: 10.1111/anec.12323.
</p>

<p align="justify">
[5] J.-S. Park, S.-W. Lee, y U. Park, «R Peak Detection Method Using Wavelet Transform and Modified Shannon Energy Envelope», J Healthc Eng, vol. 2017, p. 4901017, 2017, doi: 10.1155/2017/4901017.
</p>


<p align="justify">
[6] A. S. S. Ahmad, M. S. Matti, O. A. M. ALhabib, y S. K. Shaikhow, «Denoising of Arrhythmia ECG Signals», International Journal of Medical Research and Health Sciences, 2018, Accedido: 5 de junio de 2024. [En línea]. Disponible en: https://www.semanticscholar.org/paper/Denoising-of-Arrhythmia-ECG-Signals-Ahmad-Matti/81bac4f91badd916d73f161eabbe8cf0eaf77a2a
</p>


[7] «r_peaks». Accedido: 7 de junio de 2024. [En línea]. Disponible en: http://notebooks.pluxbiosignals.com/notebooks/Categories/Detect/r_peaks_rev.html


[8] «hrv_parameters». Accedido: 7 de junio de 2024. [En línea]. Disponible en: http://notebooks.pluxbiosignals.com/notebooks/Categories/Extract/hrv_parameters_rev.html

