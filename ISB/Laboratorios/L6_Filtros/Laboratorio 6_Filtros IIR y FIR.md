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
El electroencefalograma (EEG) es una técnica neurofisiológica que registra la actividad eléctrica del cerebro.  La señal EEG se genera por la despolarización e hiperpolarización de las neuronas corticales.  La actividad EEG se puede analizar en términos de frecuencia, amplitud y forma de onda.
</p>

<p align="justify">
  
- Frecuencia: La frecuencia de la señal EEG se mide en hercios (Hz). Las diferentes frecuencias de EEG se asocian con diferentes estados de actividad cerebral. Por ejemplo, las ondas delta (0,5-4 Hz) se asocian con el sueño profundo, mientras que las ondas beta (12-30 Hz) se asocian con la vigilia y la atención. [1]

- Amplitud: La amplitud de la señal EEG se mide en microvoltios (µV). La amplitud de la señal EEG puede variar dependiendo del estado de actividad cerebral y de otros factores, como la edad y el sexo.[1]

- Forma de onda: La forma de onda de la señal EEG se refiere al patrón de la señal a lo largo del tiempo. La forma de onda de la señal EEG puede variar dependiendo del tipo de actividad cerebral que se esté registrando.[1]
  
</p>


# 2. Tipos de filtros<a name="id2"></a>

## 2.1 Filtros IIR
<p align="justify">
Los filtros IIR son sistemas de procesamiento de señales que utilizan retroalimentación (realimentación) en su estructura, lo que les permite tener una respuesta de impulso infinita. Esto significa que su respuesta al impulso no se extingue completamente con el tiempo, lo que les permite alcanzar una alta selectividad en la respuesta en frecuencia con un número relativamente pequeño de coeficientes. Los filtros IIR son útiles en aplicaciones donde se requiere una respuesta de frecuencia nítida y una implementación eficiente.z
</p>

## 2.2 Filtros FIR
<p align="justify">
Los filtros FIR son sistemas de procesamiento de señales que tienen una respuesta de impulso finita, lo que significa que su respuesta al impulso se extingue completamente con el tiempo. Los filtros FIR no utilizan retroalimentación en su estructura y son conocidos por tener una respuesta de fase lineal, lo que los hace ideales para aplicaciones donde se necesita preservar la precisión temporal de la señal. Los filtros FIR son útiles cuando se requiere una alta flexibilidad en el diseño de la respuesta en frecuencia y una buena supresión de los lóbulos laterales.
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
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/e7e7b106ab9d2ef83dfd2fb93792fc8e322b0704/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/filtrado_reposo_emg.png" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">EEG Ciclo ojo abierto - ojo cerrado</th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/norespirar.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO2.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/e7e7b106ab9d2ef83dfd2fb93792fc8e322b0704/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/filtrado_fuerza_oponente_emg.png" alt="Forest" style="width:90%"></td>
    </tr>
    <tr>
        <th scope="row">EEG Solución a preguntas - 100 peruanos dicen</th>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/reposo2.png" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/Harold01082001/Proyecto_IntroSe-ales/blob/main/Fotos/FILTRO3.jpeg" alt="Forest" style="width:90%"></td>
        <td><img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/e7e7b106ab9d2ef83dfd2fb93792fc8e322b0704/ISB/Laboratorios/Im%C3%A1genes/IIR/EMG/filtrado_mochila_emg.png" alt="Forest" style="width:90%"></td>
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


## 4.2 Señal EMG

## 4.3 Señal EEG

# 5. Discusión<a name="id5"></a>


# 6. Referencias bibliográficas<a name="id6"></a>
