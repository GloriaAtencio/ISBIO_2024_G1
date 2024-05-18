# **Laboratorio N°7: TRANSFORMADA WAVELET**

***

# **Tabla de contenidos**
1. [Objetivos](#id1)
2. [Introducción](#id3)
3. [Metodología](#id4)
   - [Filtro Wavelet - EMG](#id4.1)
   - [Filtro Wavelet - ECG](id4.2)
   - [Filtro Wavelet - EEG](#id4.3)
4. [Resultados](#id5)
5. [Discusión](#id6)
6. [Referencias bibliográficas](#id7) 

***

# 1.Objetivos<a name="id1"></a>
   - Realizar busqueda de literatura sobre los coeficientes de wavelet aplicados a las señales de EMG, ECG y EEG.
   - Diseñar filtros adaptados para cada tipo de señal (EMG, ECG y EEG) con el objetivo de eliminar ruido y artefactos.
   - Analizar las señales filtradas para evaluar la efectividad de los filtros diseñados.
      
# 2.Introducción<a name="id3"></a>
<p align="justify">
La transformada wavelet (WT) es un método ampliamente utilizado para la supresión de ruido y la extracción de características de señales biomédicas [1]. A menudo se emplea para analizar señales instantáneas y variables en el tiempo. Aunque la transformada de Fourier clásica puede reflejar la connotación general de las señales, su expresión normalmente no es lo suficientemente intuitiva. Como alternativa, la transformada wavelet puede descomponer señales en diferentes escalas, permitiendo seleccionar diferentes niveles de descomposición según los objetivos de procesamiento. Además, permite la localización simultánea en los dominios del tiempo y la frecuencia, lo cual es particularmente ventajoso para el análisis de señales no estacionarias [2].
 </p>    
<p align="justify">
La metodología de eliminación de ruido mediante la transformada wavelet se basa en la descomposición de señales en una superposición de funciones wavelet. Tras esta descomposición, se generan coeficientes wavelet para cada señal. La distinción entre señal y ruido se realiza mediante ajustes de umbral, donde un umbral adecuado permite conservar los coeficientes de la señal, que son más grandes, y reducir los coeficientes del ruido, que son más pequeños [3].
   </p>  
<p align="justify">
Actualmente, se han desarrollado muchas bases wavelet, como Haar, Daubechies (Db), Symlet, entre otras, para el análisis y la síntesis de señales. La correcta selección de una función de base wavelet juega un papel crucial en el rendimiento de la eliminación de ruido [2].
</p>  
<p align="justify">
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/tabla1.jpeg" alt="fotog" width="520" height="300"/>
</p> 
<p align="center">
Tabla 1: Familia Wavelet [4]
</p> 

# 3.Metodología<a name="id4"></a>
## 3.1 Diseño del filtro para EMG<a name="id4.1"></a>
<p align="justify">
Onda Madre: Las wavelets Daubechies, como db2, db4, db6 y db8, son comúnmente utilizadas para el procesamiento de señales biomédicas debido a su capacidad para manejar señales no estacionarias y capturar características transitorias de la señal EMG. Estas wavelets tienen formas que son similares a las de los potenciales de acción de unidad motora (MUAP), lo que las hace especialmente adecuadas para este tipo de análisis [6]. Asimismo, al ser ortogonales, lo facilitan la reconstrucción de la señal sin pérdida de información. Para este caso específico se utilizará db8, la mayor longitud de soporte permite a la db8 capturar características más detalladas de la señal EMG, lo cual es beneficioso para el análisis de señales con estructuras complejas y transitorias. Esto resulta en una mejor representación de las variaciones rápidas y detalles finos en la señal.
   </p> 
<p align="justify">
Nivel de Descomposición: Para señales EMG, que típicamente tienen frecuencias de muestreo en el rango de kHz, los niveles de descomposición usualmente varían entre 4 y 6. Esto permite capturar tanto los movimientos musculares generales (bajas frecuencias) como los picos de actividad muscular (altas frecuencias). Se trabaja con un nivel 5 estándar a las otras señales, un nivel demasiado bajo podría perder detalles importantes, mientras que un nivel demasiado alto podría introducir ruido [2].
</p> 
<p align="justify">
Umbralización: El proceso descrito implica que los coeficientes cuya magnitud está por debajo del umbral se fijan en cero, lo cual es la característica distintiva de la umbralización dura. Se está tomando la forma universal, como tal se describe que este método está diseñado específicamente para manejar situaciones en las que la señal de interés está contaminada con ruido gaussiano, y su principal objetivo es minimizar el error de reconstrucción [6].
</p> 

## 3.2 Diseño del filtro para ECG<a name="id4.2"></a>
<p align="justify">
Para aplicar la transformada de wavelet con el objetivo de eliminar ruidos de la señal de ECG, se deben considerar varios aspectos clave. Entre ellos, la determinación del número de capas de descomposición de las ondas influye significativamente en la efectividad de la eliminación del ruido. A continuación, se describen los parámetros esenciales para este proceso: la selección de la onda madre, el nivel de descomposición y el método de umbralización.
</p> 
<p align="justify">
- Onda Madre: La selección correcta de una función de base wavelet es crucial para el rendimiento en la eliminación de ruido. La Tabla 2 muestra la comparación de la relación señal-ruido (SNR) y el error cuadrático medio (MSE) de las señales de ECG sin ruido, procesadas mediante varias ondas típicas. Según esta tabla, la SNR de la wavelet db5 es relativamente alta y el MSE es relativamente bajo [2]. Por lo tanto, basándonos en esta evidencia, seleccionamos db5 como la base wavelet para el proceso de eliminación de ruido de la señal de ECG en este informe.
</p> 
<p align="justify">
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/tabla2.jpeg" alt="fotog" width="520" height="300"/>
</p> 
<p align="center">
Tabla 2: Comparación de los resultados de eliminación de ruido según varias ondas típicas.[2]
</p> 
<p align="justify">
- Nivel de Descomposición: El número de capas de descomposición también es un factor crítico. Si el número de capas es demasiado pequeño, el efecto de eliminación de ruido será insatisfactorio. Generalmente, para eliminar el ruido de alta frecuencia y extraer componentes de baja frecuencia, el número de capas de descomposición se incrementa hasta cierto punto. Sin embargo, si el número de capas es demasiado alto, el error puede aumentar considerablemente. Esto se debe a que el proceso se centra más en las características de la base wavelet que en la señal que se está analizando, lo que puede resultar en frecuencias falsas y una pérdida significativa de información [2].
</p> 
<p align="justify">
- Umbralización: La selección del método de umbralización adecuado es fundamental, independientemente de la función wavelet que se utilice. Existen varias técnicas de umbralización que presentan buenos resultados, como MINMAX, RIGOROUS SURE, UNIVERSAL y HEURISTIC SURE [5]. En este informe, se utilizará el umbral universal dado por "sqrt(2 * log(N))", donde N es la longitud de la señal.
</p> 

## 3.3 Diseño del filtro para EEG<a name="id4.3"></a>

<p align="justify">
Al hacer el diseño del código en lenguaje python de la transformada wavelet como filtro nos basamos en el paper "EEG De-noising using Wavelet Transform and Fast ICA" el cual aborda el uso de la transformada wavelet y el análisis de componentes independientes (ICA) para la eliminación de ruido en señales EEG mediante un método de umbralización de coeficientes de descomposición. La técnica se verifica con señales simuladas y se aplica a señales biomédicas EEG, también útil para imágenes por resonancia magnética con ruido aleatorio adicional.
</p> 

<p align="justify">
El diseño de filtro mediante la transformada wavelet (WT) permite el análisis multiresolución de señales no estacionarias, extrayendo información global a bajas frecuencias (altas escalas) mediante la convolución de la señal con una función wavelet escalada. Los coeficientes de wavelet muestran la similitud en el contenido de frecuencia y se interpretan como aproximaciones del filtro pasa banda dilatado.
</p> 

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/55bbe7da-bba5-4cdc-a8d8-8e3d8f393090" alt="fotog" width="960" height="400"/>
</p>
<p align="center"><i>Figura 1. La filtración de síntesis consiste en el sobremuestreo por 2 y la filtración.</i></p><br>

<p align="justify">
Cabe resaltar que en el artículo se utilizó la función sym4 de wavelet y  se utiliza la umbralización de los coeficientes de la DWT hasta el nivel 3 para eliminar el ruido aleatorio. También usaron un umbral del tipo suave. Y nos basamos en el siguiente código proporcionado  en el artículo:
 </p>
 
```
eeg=load('EEG01.TXT'); 
eeg=detrend(eeg); % Remove a linear trend 
eeg=eeg(100:611);
 L=length(eeg); 
eegN=eeg+160*randn(L,1);
 [THR,SORH,KEEPAPP]=ddencmp('den','wv',eegN); 
level=3; 
[eegC,CeegC,LeegC,PERF0,PERFL2]=wdencmp('gbl',eeg N,'sym4',level,THR,SORH,KEEPAPP);
```

<p align="justify">
Como el código proporcionado fue aplicado en matlab , tuvimos que adaptarlo al lenguaje python:
 </p>
 
```
def apply_wavelet_filter(signal, wavelet='db4', level=3):
    # Eliminar la tendencia lineal
    signal_detrended = detrend(signal)

    # Calcular el umbral global
    sigma = np.median(np.abs(signal_detrended - np.median(signal_detrended))) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(signal_detrended)))

    # Descomposición wavelet
    coeffs = pywt.wavedec(signal_detrended, wavelet, level=level)

    # Aplicar umbralización suave
    coeffs_thresh = [pywt.threshold(c, threshold, mode='soft') if i > 0 else c for i, c in enumerate(coeffs)]

    # Reconstrucción de la señal
    filtered_signal = pywt.waverec(coeffs_thresh, wavelet)
    # Asegurarse de que la señal reconstruida tenga la misma longitud que la original
    filtered_signal = filtered_signal[:len(signal)]
    return filtered_signal, coeffs, coeffs_thresh
```


# 4.Resultados<a name="id5"></a> 
## 4.1 Señal EMG
| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Basal| <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETB1.png" alt="fotog" width="350" height="270"/> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETB2.png" alt="fotog" width="350" height="270" /> | 
|Levantando mochila | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETM1.png" alt="fotog" width="350" height="270" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETM2.png" alt="fotog" width="350" height="270" /> |
| Fuerza oponente | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETO1.png" alt="fotog" width="350" height="270" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/EMGWAVELETO2.png" alt="fotog" width="350" height="270" /> |

| Coeficientes de Detalle EMG BASAL| 
|----------|
|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/emg11.png" alt="fotog" width="750" height="370" /> |
|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/emg12.png" alt="fotog" width="750" height="370" /> |

| Coeficientes de Detalle EMG LEVANTANDO MOCHILA| 
|----------|
|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/emg21.png" alt="fotog" width="750" height="370" /> |
|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/emg22.png" alt="fotog" width="750" height="370" /> |

| Coeficientes de Detalle EMG FUERZA OPONENTE| 
|----------|
|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/emg31.png" alt="fotog" width="750" height="370" /> |
|  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/emg32.png" alt="fotog" width="750" height="370" /> |
## 4.1 Señal ECG

Las señales de electrocardiograma (ECG) fueron adquiridas durante diferentes condiciones experimentales: en estado basal (reposo), en estado de hiperventilación y después de ejercicio. A continuación, se presenta la señal cruda para cada uno de estos estados y la señal filtrada para reducir el ruido, utilizando la transformada wavelet previamente parametrizada.

| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Reposo| <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/reposo1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/reposo2.png" alt="fotog" /> | 
| Hiperventilación | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/hiperventilacion1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/hiperventilacion2.png" alt="fotog" /> |
| Despues de actividad fisica | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/ejercicio1.png" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/WAVELET/ejercicio2.png" alt="fotog" /> |

## 4.1 Señal EEG

<p align="justify">
Las señales EEG que serán procesadas fueron adquiridos en el laboratorio pasado , durante diferentes actividades : Estado basal , ciclo de ojos cerrados y abiertos y finalmente ejercicio mental.Estas señales se almacenaron en formato de texto y se uso una frecuencia de muestreo de 100 Hz
</p> 

| Tipo de señal | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Reposo |<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/2201f2a6-53d8-4e27-8ce8-b6250f588474" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/0ae19515-09c0-479b-b161-3b1d63a717dd" alt="fotog" /> | 
| Ciclo cerrando y abriendo ojos |<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/fd6c11e9-7f5c-45c6-8cc6-757a48c61383" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/fca204fb-8439-4de1-bd96-da87c1def46b" alt="fotog" /> | 
| Ejercicio mental |<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/bb322eb1-0292-4996-b478-223809a69348" alt="fotog" /> | <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/ad00c575-4345-416f-bb8d-aac6e587bf12" alt="fotog" /> | 

# 5.Discusión<a name="id6"></a>

### EMG
En la condición basal, se observó que el filtro wavelet fue efectivo para eliminar el ruido presente en la señal, lo que permitió una mejor visualización de los potenciales de acción muscular asociados con el reposo o la actividad mínima. Se pudo apreciar una reducción significativa en la amplitud de las señales de alta frecuencia, lo que sugiere una disminución del ruido electromagnético y artefactos indeseados. Durante la actividad de oponerse a una fuerza, el filtro wavelet demostró el poder preservar los potenciales de acción musculares relevantes mientras atenuaba el ruido generado por movimientos involuntarios o interferencias externas, inherentes a la EMG superficial. Asimismo, se evidenció la mejora de la relación señal-ruido, donde los picos de actividad muscular se destacaron más sobre el fondo de ruido residual. Al levantar una mochila, las señales EMG se vieron con mayor nivel de interferencias debido a la actividad muscular intensificada y la influencia de la carga adicional. Sin embargo, el filtro wavelet logró mitigar gran parte de estos efectos no deseados al eliminar el ruido de fondo, permitiendo una identificación más precisa de los potenciales de acción muscular asociados con el esfuerzo por la carga.

### ECG
La transformada wavelet(WT) se ha demostrado como una herramienta eficaz debido a su capacidad de descomponer señales en diferentes escalas, lo que es particularmente útil para el análisis de señales no estacionarias como las de ECG.
Los resultados experimentales muestran que la aplicación de la transformada wavelet con la onda db5 y el umbral universal mejora significativamente la calidad de las señales de ECG. Las señales adquiridas en diferentes condiciones (reposo, hiperventilación, post-ejercicio) muestran una reducción notable del ruido después del procesamiento. Esto confirma la eficacia del método propuesto para mejorar la claridad y la utilidad de las señales de ECG para el análisis clínico. Además, la correcta elección del número de capas de descomposición es crucial, ya que un número demasiado bajo podría resultar en una insuficiente eliminación de ruido, mientras que un número demasiado alto podría introducir artefactos y pérdida de información. Este balance es esencial para preservar la integridad de la señal de ECG, un aspecto que ha sido resaltado en la literatura como fundamental para el análisis clínico preciso. Una señal de ECG más clara puede facilitar diagnósticos más precisos y confiables, lo que es crucial en contextos clínicos donde las decisiones deben ser rápidas y basadas en datos precisos.

## 5.1 Señal EEG

|  **Señales originales - ploteadas por muestra**  | **Señales originales - ploteadas por tiempo** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/e8656ae1-165e-4820-a40c-f10b47a7c094" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/e5b34c56-d485-468c-ac64-274756b2deea" alt="fotog" />|
</div>

<div align="center">
<h2>DFT de las señales </h2>
</div>

| En reposo | Ojos abiertos - Ojos cerrados | Ejercicio mental |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/cd918295-9092-4b68-b1a8-195049803148) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/d543a01d-9943-4e6b-a3a0-63042d90d0e7) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/955af287-7d5b-4ca1-91c2-cc8fc5020f5c) |

<div align="center">
<h2>Comparación de las señales sin filtro y con filtro</h2>
</div>

<div align="center">
   
| En reposo |
|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/1364ba08-2a48-4239-81d3-62a1952d1d55) |
</div>

<div align="center">
   
 | Ojos abiertos - Ojos cerrados |
 |----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/3bd058e1-1853-4959-9dd9-0fa2974c387c) |
</div>

<div align="center">
   
| Ejercicio mental |
 |----------|
 | ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/66a48a98-7c4b-4d29-8f0f-66197f55207e) |
 </div>

 <div align="center">
<h2>Coeficientes de aproximación y detalle</h2>
</div>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/447e3b8d-863a-40c8-ace1-15de63c16585" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 1. Coeficiente de aproximación - Reposo (EEG)</i></p><br>

<div align="center">
   
| Coeficientes de detalle - En reposo |
|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/7b8e45f3-a784-4bb3-bae8-59e99e0ae297) |
</div>


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/dd14fae8-2da5-4cf5-8620-5c2a10e545a0" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 2. Coeficiente de aproximación - Ojos abiertos - Ojos cerrados (EEG)</i></p><br>

<div align="center">
   
 |  Coeficientes de detalle - Ojos abiertos - Ojos cerrados |
 |----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/8001fd0d-76cf-4215-a86b-3774dab930ae) |
</div>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/cb05a47e-189c-49a0-b804-9df28762c623" alt="fotog" width="900" height="200"/>
</p>
<p align="center"><i>Figura 3. Coeficiente de aproximación - Ejercicio mental (EEG)</i></p><br>



<div align="center">
   
| Ejercicio mental |
 |----------|
 | ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/a870eba7-13c5-4b59-ad54-7385bb907e27) |
 </div>

<div align="center">
<h2>DFT de las señales filtradas - Wavelet </h2>
</div>

| En reposo | Ojos abiertos - Ojos cerrados | Ejercicio mental |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/f52e872f-d9f4-4c7a-b486-9a1f49962d72) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/0989e51e-0dd5-4736-8576-ac67d0012420) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/342e1807-a5f7-4f06-8a9b-d9ea9b8a6a18) |

<div align="center">
<h2>DFT de las señales filtradas - Wavelet y Notch </h2>
</div>

| En reposo | Ojos abiertos - Ojos cerrados | Ejercicio mental |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/0b21bb7e-d561-42ea-8084-251638158406) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/5ea2ff99-1264-4a52-ba5f-45b2fa16e700) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/43a3d92b-296a-4c5c-9469-5b95cad0ac8a) |


# 6.Referencias bibliográficas<a name="id7"></a>

[1] D. Vilimek et al., “Comparative analysis of wavelet transform filtering systems for noise reduction in ultrasound images”, PLOS ONE, vol. 17, n.º 7, julio de 2022, art. n.º e0270745. Accedido el 17 de mayo de 2024.[Online]. Available:  https://doi.org/10.1371/journal.pone.0270745 

[2]D. Zhang et al., "An ECG Signal De-Noising Approach Based on Wavelet Energy and Sub-Band Smoothing Filter," Appl. Sci., vol. 9, no. 22, p. 4968, 2019.Accedido el 17 de mayo de 2024 [Online]. Available: https://doi.org/10.3390/app9224968 

[3]S. Su et al., “An ECG Signal Acquisition and Analysis System Based on Machine Learning with Model Fusion”, Sensors, vol. 23, n.º 17, p. 7643, septiembre de 2023. Accedido el 17 de mayo de 2024. [Online]. Available:https://doi.org/10.3390/s23177643 

[4] D. M., A. E., and L. F., ‘Discrete Wavelet Transform in Compression and Filtering of Biomedical Signals’, Discrete Wavelet Transforms - Biomedical Applications. InTech, Sep. 12, 2011. doi: 10.5772/19529. 

[5] https://ieeexplore.ieee.org/document/5728090

[6] N. Sobahi, “Denoising of EMG Signals Based on Wavelet Transform,” Asian Transactions on Engineering, vol. 01, no. 05, Jan. 2011, [Online]. Available: https://www.researchgate.net/publication/267957236_Denoising_of_EMG_Signals_Based_on_Wavelet_Transform
