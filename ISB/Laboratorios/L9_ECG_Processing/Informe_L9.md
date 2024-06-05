# **Laboratorio N°9: Caracterización de señal ECG**

***

# **Tabla de contenidos**
1. [Objetivos](#id1)
2. [Introducción](#id3)
3. [Metodología](#id4)
   - [Aplicación de filtro](#id3.1)
   - [Detección de picos](id3.2)
   - [Análisis de Threshold](#id3.3)
4. [Resultados](#id4)
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

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

## 3.2. Detección de picos<a name="id3.2"></a>

## 3.3. Análisis de Threshold<a name="id3.3"></a>


# 4.Resultados<a name="id4"></a>

# 5.Discusión<a name="id5"></a>


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

[4] A. R. Pérez-Riera, L. C. de Abreu, R. Barbosa-Barros, K. C. Nikus, y A. Baranchuk, «R-Peak Time: An Electrocardiographic Parameter with Multiple Clinical Applications», Ann Noninvasive Electrocardiol, vol. 21, n.º 1, pp. 10-19, ene. 2016, doi: 10.1111/anec.12323.
