# **Laboratorio N°6: Uso de filtros IIR y FIR**

***

# **Tabla de contenidos**
1. [Introducción](#id1)
2. [Tipos de filtros](#id2)
   - [Filtros IIR](#Filtros-IIR)
   - [Filtros FIR](#Filtros-FIR)
3. [Aplicación de filtros](#id3)
4. [Imágenes y análisis](#id4)
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

***

# 1.Introducción<a name="id1"></a>

<p align="justify">
</p>

## Objetivos:

<p align="justify">
Objetivo General: 
   
- El objetivo de este laboratorio es comprender y crear los filtros digitales necesarios para filtrar el ruido y otros artefactos comunes en las señales adquiridas del ECG, EMG Y EEG.

Objetivos Específicos para ECG: 
- Diseñar  filtros IIR y FIR óptimos, para filtrar las frecuencias altas de dichas
señales que corresponden a ruido.

Objetivos Específicos para EMG: 
- Diseñar un filtro FIR para eliminar frecuencias altas que correspondan a ruido eléctrico y artefactos de movimiento.
- Diseñar un filtro IIR para aislar la banda de frecuencia de interés que corresponde a la actividad muscular.

Objetivos Específicos para EEG: 
- Diseñar un filtro FIR para suprimir interferencias de  frecuencias altas que correspondan a ruido eléctrico y artefactos de movimientos como el parpadeo de ojos y la actividad muscular .
- Diseñar un filtro IIR para extraer bandas de frecuencia específicas (alfa, beta, etc.).

</p>

  
## Marco teórico:

<p align="justify">
Las señales biomédicas, tales como la cardiaca, la cerebral, la muscular, la respiratoria, la de saturación de oxígeno, entre otras, son de muy bajo potencial eléctrico, del orden de los mV, y están sometidas a muchos tipos de ruido, los que perjudican su observación y presentación en el análisis médico del paciente [1]. En ese sentido, es necesaria una técnica de procesamiento de señales biomédicas y una alternativa sería la aplicación de filtros digitales, que sean  adecuados para reprimir los distintos tipos de ruido, como la desviación de la línea base, la interferencia de la línea eléctrica, el ruido de alta frecuencia, los artefactos fisiológicos, etc. Los filtros digitales se pueden clasificar en dos categorías principales: filtros de respuesta finita al impulso (FIR) y filtros de respuesta infinita al impulso (IIR). Los filtros FIR se caracterizan por tener una respuesta de impulso finita, lo que significa que su salida depende únicamente de un número finito de entradas pasadas. Algunas técnicas de diseño de filtros FIR incluyen ventanas:  Rectangular, Hann, Blackman, Hamming y Kaiser Por otro lado, los filtros IIR tienen una respuesta de impulso infinita, lo que implica que su salida puede depender de un número infinito de entradas pasadas. Algunos ejemplos de filtros IIR incluyen Butterworth, Chebyshev I, Chebyshev II y filtros elípticos.[2].
   
Al diseñar un filtro para el procesamiento de señales biomédicas, es crucial considerar las características específicas de frecuencia y amplitud de la señal de interés. Esto se debe a que diferentes señales biomédicas pueden tener rangos de frecuencia y amplitudes distintas, como se muestra en la Tabla 1 para señales como el electrocardiograma (ECG), electroencefalograma (EEG) y electromiograma (EMG) [3]. Por lo tanto, seleccionar el tipo de filtro adecuado y ajustar sus parámetros en función de estas características es precisa para lograr una supresión efectiva del ruido y preservar la información relevante en las señales biomédicas

</p>

<p align="justify">
  
Tabla 1:  Amplitud y Rango de Frecuencias de algunas señales bioeléctricas típicas[3]

  
</p>


# 2. Tipos de filtros<a name="id2"></a>

## 2.1 Filtros IIR
<p align="justify">
   
- Los filtros IIR son útiles en aplicaciones donde se requiere una respuesta de frecuencia nítida y una implementación eficiente. [4]
   
- Requiere menos coeficientes y memoria que los filtros FIR para satisfacer un conjunto similar de especificaciones, es decir, frecuencia de corte y atenuación de banda de parada.[5]
  
- Menos estable numéricamente que sus homólogos FIR (respuesta de impulso finito), debido a las rutas de retroalimentación.[5]

Los filtros Butterworth son filtros IIR que tienen una respuesta en frecuencia plana en la banda de paso y una caída suave en la banda de parada. Se utilizan comúnmente en el filtrado de señales de ECG para eliminar ruido de baja frecuencia y de alta frecuencia, así como para enfatizar las componentes de frecuencia de interés en la señal. Con mayor énfasis en el pasa baja, pues crea más distorsión en la señal después de aplicarlo. [6]

Para el caso de señales EMG, dado que las señales pueden contener componentes de alta frecuencia, como los potenciales de acción musculares, así como componentes de baja frecuencia, como el ruido de línea de base y artefactos de movimiento. Se puede aplicar en dirección directa como inversa de las señales para evitar así distorsiones de fase. [7]

En el EEG, las señales de EEG pueden estar contaminadas con una variedad de artefactos, como ruido muscular, movimiento ocular y actividad eléctrica no cerebral[8]. Los filtros Butterworth de paso alto pueden ser útiles para atenuar el ruido de baja frecuencia y los artefactos musculares, mientras que los filtros Butterworth de paso bajo pueden ser utilizados para atenuar el ruido de alta frecuencia y los artefactos de movimiento ocular.[9]

</p>

## 2.2 Filtros FIR
<p align="justify">
   
- Los FIR se pueden diseñar fácilmente para que tengan fase lineal. Esto significa que no se introduce distorsión de fase en la señal que se va a filtrar, ya que todas las frecuencias se desplazan en el tiempo en la misma cantidad, manteniendo así sus relaciones armónicas relativas (es decir, retardo de grupo y fase constante).[5]

- Como los FIR no utilizan valores de salida anteriores para calcular su salida actual, es decir, no tienen retroalimentación, nunca pueden volverse inestables para ningún tipo de señal de entrada. [5]
  
- Altos requisitos computacionales y de memoria. [5]
  
La ventana rectangular, también conocida como ventana de caja, es la ventana más simple y básica que se puede utilizar en el diseño de filtros FIR[10]. Sin embargo, la ventana rectangular no proporciona una buena supresión de los lóbulos laterales en la respuesta en frecuencia del filtro, lo que puede provocar una mayor distorsión de la señal y una respuesta en frecuencia menos selectiva en comparación con otras ventanas. La ventana de Hamming es una ventana diseñada para reducir los lóbulos laterales en la respuesta en frecuencia de un filtro FIR, La ventana de Hamming es una opción popular para el diseño de filtros FIR pues se centra en los rangos de menor complejidad.[11]

</p>

# 3. Aplicación de filtros<a name="id3"></a>
## 3.1 Señal ECG
<table>
    <caption>Análisis</caption>
    <tr>
        <th scope="col">Situación </th>
        <th scope="col">Señal original</th>
        <th scope="col">Señal con el filtro FIR</th>
        <th scope="col">Señal con el filtro IIR</th>
    </tr>
    <tr>
        <th scope="row">ECG en reposo </th>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/01145c07daaa228965788686eb13672d88eddbdf/ISB/Laboratorios/Im%C3%A1genes/FIR/ECG/se%C3%B1al_original_ecg_reposo.png" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO1.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/aa2a50d5dd4b7c4feaef72327a62cf266b3dd863/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/filtrado_reposo_ecg.png" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">ECG hiperventilación</th>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/01145c07daaa228965788686eb13672d88eddbdf/ISB/Laboratorios/Im%C3%A1genes/FIR/ECG/se%C3%B1al_original_ecg_hiperventilacion.png" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO2.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/aa2a50d5dd4b7c4feaef72327a62cf266b3dd863/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/filtrado_hiperventilaci%C3%B3n_ecg.png" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">ECG después de actividad física</th>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/01145c07daaa228965788686eb13672d88eddbdf/ISB/Laboratorios/Im%C3%A1genes/FIR/ECG/se%C3%B1al_original_ecg_actividad.png" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO3.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/aa2a50d5dd4b7c4feaef72327a62cf266b3dd863/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/filtrado_despuesdeactividad_ecg.png" alt="Forest" style="width:90%"></td>
    </tr>
 
</table>

## 3.2 Señal EMG

<table>
    <caption>Análisis</caption>
    <tr>
        <th scope="col">Situación </th>
        <th scope="col">Señal original</th>
        <th scope="col">Señal con el filtro FIR</th>
        <th scope="col">Señal con el filtro IIR</th>
    </tr>
    <tr>
        <th scope="row">EMG en reposo </th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/reposo1.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO1.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/e7e7b106ab9d2ef83dfd2fb93792fc8e322b0704/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/filtrado_reposo_emg.png" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">EMG fuerza oponente - Contracción Leve</th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/norespirar.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO2.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/e7e7b106ab9d2ef83dfd2fb93792fc8e322b0704/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/filtrado_fuerza_oponente_emg.png" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">EMG levantando mochila - Contracción Fuerte</th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/reposo2.png" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO3.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/e7e7b106ab9d2ef83dfd2fb93792fc8e322b0704/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/filtrado_mochila_emg.png" alt="Forest" style="width:90%"></td>
    </tr>
 
</table>

## 3.3 Señal EEG

<table>
    <caption>Análisis</caption>
    <tr>
        <th scope="col">Situación </th>
        <th scope="col">Señal original</th>
        <th scope="col">Señal con el filtro FIR</th>
        <th scope="col">Señal con el filtro IIR</th>
    </tr>
    <tr>
        <th scope="row">EEG en reposo </th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/reposo1.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO1.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/7b4ce5b5-4547-4b6e-b46c-b5f99c3be0a9" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">EEG Ciclo ojo abierto - ojo cerrado</th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/norespirar.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO2.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/900dfe85-73dd-47de-85e5-3694ef7a3192" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">EEG Solución a preguntas - 100 peruanos dicen</th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/reposo2.png" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO3.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/41324086-cc68-490a-a91e-bb0b71c1842c" alt="Forest" style="width:90%"></td>
    </tr>
 
</table>

# 4. Imágenes y análisis<a name="id4"></a>

## 4.1 Señal ECG

|  **Señales originales - ploteadas por muestra**  | **Señales originales - ploteadas por tiempo** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg.png" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/f22c57572b6955f1543d1c9f5b41f9a6f89caac0/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/se%C3%B1ales_originales_ecg_same_Axis.png" alt="fotog" />|
</div>

<div align="center">
<h2>DFT de las señales </h2>
</div>

| En reposo | Hiperventilación | Después de actividad física |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/b69d2ae60ad0204982660fd56e9a182efcff241f/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/dft_se%C3%B1al_reposo_original.png) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/177af66f-6a87-448c-a8b2-b7b048d18ce0) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/c7b0a166-aefd-4334-aed1-4b175c0eae5c) |

<div align="center">
<h2> DFT de las señales después de haber aplicado filtro notch </h2>
</div>

| En reposo | Hiperventilación | Después de actividad física |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/2e276fb2-2a98-4072-b3d3-f53683f7f6c9) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/364911a1c914ce25a3a5b1a66d9296a9638e789f/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/dft_se%C3%B1al_hiperventilacion_notch.png) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/364911a1c914ce25a3a5b1a66d9296a9638e789f/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/dft_se%C3%B1al_despuesdeactividad_notch.png) |

<div align="center">
<h2> Diseño de filtro IIR - Butterworth </h2>
</div>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/02e6ce66-2ad5-4da9-8faa-e4146d26204d" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 1. Respuesta en frecuencia del filtro analógico (ECG)</i></p><br>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/99a5e8bffd54e1be043197fde6e694da83a9d4dd/ISB/Laboratorios/Im%C3%A1genes/IIR/ECG/transformada_bilineal_ecg.png" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 2. Transformada bilineal de H(s) a H(z) (ECG)</i></p><br>

<div align="center">
<h2> Señales filtradas - Filtro IIR  </h2>
</div>

| En reposo | Hiperventilación | Después de actividad física |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/3ae92175-1916-4743-b78c-18bcb763659b) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/8f8163cf-d47b-4020-ae2e-e922f1d455de) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/aec405e3-929e-41e8-8a2d-b0f6d1ec218d) |

<div align="center">
<h2> DFT de señales filtradas  - Filtro IIR </h2>
</div>

| En reposo | Hiperventilación | Después de actividad física |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/b4640b1b-9fde-422a-a5f3-e256c5a45aa4) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/149e2118-69b3-42ed-a6d8-2682c194a253) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/0dcebd94-735b-4a15-a71e-9c88af5aaaec) |



## 4.2 Señal EMG

|  **Señales originales - ploteadas por muestra**  | **Señales originales - ploteadas por tiempo** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5450c74e1c7dfc7b50c888294c4ca7917128c0ad/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/se%C3%B1ales_originales_emg.png" alt="fotog" />|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5450c74e1c7dfc7b50c888294c4ca7917128c0ad/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/se%C3%B1ales_originales_emg_same_Axis.png" alt="fotog" />|
</div>

<div align="center">
<h2>DFT de las señales </h2>
</div>

| En reposo | Fuerza oponente | Levantando mochila |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5450c74e1c7dfc7b50c888294c4ca7917128c0ad/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/dft_se%C3%B1al_reposo_original_emg.png) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/c1d1b27b-cd79-466d-bbdd-9c3fee18e0d0) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5450c74e1c7dfc7b50c888294c4ca7917128c0ad/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/dft_se%C3%B1al_mochila_original_emg.png) |


<div align="center">
<h2> Diseño de filtro IIR - Butterworth </h2>
</div>
<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/438d275c-b6d4-4811-ac0b-d3335183f6e6" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 3. Respuesta en frecuencia del filtro analógico (EMG)</i></p><br>


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5450c74e1c7dfc7b50c888294c4ca7917128c0ad/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/transformada_bilineal_emg.png" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 4. Transformada bilineal de H(s) a H(z) (EMG)</i></p><br>

<div align="center">
<h2> Señales filtradas - Filtro IIR  </h2>
</div>

| En reposo | Fuerza oponente | Levantando mochila |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/e73a8d6e-263d-438e-835f-fb27a0ba4acd) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/6b15b7b4-2411-4702-b082-f3132a93ccab) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/e9cb0ccf-c870-46a4-ad3d-9457ec10b2fc) |

<div align="center">
<h2> DFT de señales filtradas  - Filtro IIR </h2>
</div>

| En reposo | Fuerza oponente | Levantando mochila |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/015e85ed-2f66-4ec8-99dc-3416e22e65ed) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/3b119526-383f-4f0a-adcc-2d232f256c9b) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/986c9e47-00ad-4b82-9346-be4c368f3877) |




## 4.3 Señal EEG

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
<h2> DFT de las señales después de haber aplicado filtro notch </h2>
</div>

| En reposo | Ojos abiertos - Ojos cerrados | Ejercicio mental |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/9dfbbc15-c897-499a-9f22-dadd34046d57) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/e047337b-0983-4e84-aa88-88217b9e7934) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/4dc49e37-a6c3-4099-9a78-fd701d52dbca) |


<div align="center">
<h2> Diseño de filtro IIR - Butterworth </h2>
</div>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/16602be7-305d-450b-8cbe-75d8255465a2" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 1. Respuesta en frecuencia del filtro analógico (EEG)</i></p><br>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/377d9931-b713-4c63-a4f5-6838b8befc98" alt="fotog" width="460" height="400"/>
</p>
<p align="center"><i>Figura 2. Transformada bilineal de H(s) a H(z) (EEG)</i></p><br>


<div align="center">
<h2> Señales filtradas - Filtro IIR  </h2>
</div>

| En reposo | Ojos abiertos - Ojos cerrados | Ejercicio mental |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/26c96685-3ef5-4684-872b-714f4a9f81d6) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/7054d881-dc84-4ff7-a31d-0300a2f6ee56) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/ddee790b-b7a4-47b1-9536-205eb257d6a4) |



<div align="center">
<h2> DFT de señales filtradas  - Filtro IIR </h2>
</div>

| En reposo | Ojos abiertos - Ojos cerrados | Ejercicio mental |
|----------|----------|----------|
| ![Imagen 1](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/a563965c-a1e5-40c7-8dea-b944fd4f63df) | ![Imagen 2](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/90b4448d-30e0-4b7a-a56e-c94638ae5611) | ![Imagen 3](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/b31b21cd-d550-4ac5-9291-3cfc9c8f5be2) |





# 5. Discusión<a name="id5"></a>


# 6. Referencias bibliográficas<a name="id6"></a>
