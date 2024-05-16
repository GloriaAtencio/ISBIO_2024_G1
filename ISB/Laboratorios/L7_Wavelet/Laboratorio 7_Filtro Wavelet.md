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

La transformada wavelet (WT) es un método ampliamente utilizado para la supresión de ruido y la extracción de características de señales biomédicas [1]. Esta técnica funciona descomponiendo las señales en una superposición de funciones wavelet, generando coeficientes para cada una. A través de ajustes de umbral, se distinguen los coeficientes de la señal de aquellos correspondientes al ruido, permitiendo que los coeficientes más grandes representen la señal y los más pequeños el ruido [2].

La esencia de la transformada wavelet es similar a la de la transformada de Fourier, ya que ambas utilizan una base para representar señales. Sin embargo, la transformada wavelet emplea un conjunto de bases específicas, denominadas 'wavelets', que son ondas con energía altamente concentrada en el dominio del tiempo y limitadas a un punto específico. Esto permite caracterizar características locales tanto en el dominio del tiempo como en el de la frecuencia. A diferencia de la transformada de Fourier, la transformada wavelet ofrece la ventaja de manejar señales abruptas o discontinuas, permitiendo un análisis más detallado de las señales mediante operaciones de estiramiento y desplazamiento [2].

# 3.Metodología<a name="id4"></a>
## 3.1 Filtro EMG<a name="id4.1"></a>
## 3.2 Filtro ECG<a name="id4.2"></a>
## 3.3 Filtro EEG<a name="id4.3"></a>
# 4.Resultados<a name="id5"></a>
# 5.Discusión<a name="id6"></a>
# 6.Referencias bibliográficas<a name="id7"></a>

