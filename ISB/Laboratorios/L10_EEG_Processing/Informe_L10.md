# **Laboratorio N°10:**

***

# **Tabla de contenidos**
1. [Objetivos](#id1)
2. [Introducción](#id3)
3. [Metodología](#id4)
 
   
4. [Resultados](#id4)
    
    
   
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

***

# 1.Objetivos<a name="id1"></a>
   - Descargar bases de datos de PhysioNet que contengan señales EEG.
   - Filtrar y limpiar las señales EEG para eliminar artefactos y ruido.
   - Aplicar filtros ICA para separar fuentes de actividad cerebral y eliminar interferencias.
   - Extraer características relevantes de las señales EEG preprocesadas
# 2.Introducción<a name="id2"></a>

<p align="justify">
La actividad neuronal en el cerebro humano se manifiesta entre las semanas 17 y 23 del desarrollo prenatal. Desde esta etapa temprana y a lo largo de toda la vida, las señales eléctricas generadas por el cerebro no solo reflejan su función, sino también el estado del cuerpo en su conjunto. Esta premisa impulsa la aplicación de métodos avanzados de procesamiento de señales digitales a los electroencefalogramas (EEG) obtenidos del cerebro humano [1].
 </p>

<p align="justify">
El camino que va desde las neuronas, actuando como fuentes de señal, hasta los electrodos, que son los sensores donde se registran diversas formas de actividad neuronal, se establece a través del medio. Sin embargo, comprender las funciones neuronales y las propiedades neurofisiológicas del cerebro, así como los mecanismos subyacentes a la generación y registro de señales, resulta fundamental para quienes trabajan con estas señales en la detección, diagnóstico y tratamiento de trastornos cerebrales y enfermedades relacionadas.
 </p>

<p align="justify">
La cabeza humana consta de diferentes capas, que incluyen el cuero cabelludo, el cráneo, el cerebro y numerosas capas delgadas entre ellos. El cráneo atenúa las señales aproximadamente cien veces más que el tejido blando, mientras que la mayor parte del ruido se genera dentro del cerebro (ruido interno) o sobre el cuero cabelludo (ruido del sistema o ruido externo)[1].
</p>

<p align="justify">
La descomposición de datos de EEG mediante ICA (Análisis de Componentes Independientes) transforma los registros de canales de cuero cabelludo en canales virtuales espacialmente transformados, produciendo señales temporalmente independientes. Este método aplica filtros espaciales a los datos multicanal para revelar fuentes de información subyacentes, que pueden ser actividades corticales sincrónicas o no corticales, como movimientos oculares y ruido de línea. ICA separa estas fuentes de las mezclas registradas, permitiendo un análisis más claro y detallado de las distintas actividades cerebrales y extracerebrales presentes en los datos de EEG.[2].
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/EEG/ICA.jpeg" alt="fotog" width="600" height="500"/>
</p>
<p align="center"><i> Figura1: Descomposición de EEG mediante ICA para Identificar Fuentes Independientes [2]</i></p>


# 3.Metodologia<a name="id3"></a>

## 3.1. Base de datos Physionet<a name="id3.1"></a>
<p align="justify">
Para este informe, se utilizará el conjunto de datos "Auditory evoked potential EEG-Biometric dataset" proporcionado por PhysioNet [3]. Este conjunto de datos incluye más de 240 grabaciones de EEG de dos minutos obtenidas de 20 voluntarios, con experimentos de estado de reposo y estímulos auditivos.
 </p>
<p align="justify">
En este laboratorio, nos centraremos únicamente en la data de una persona al que corresponde "s01_ex01_s01.csv"  que contiene los datos segmentados de EEG obtenidos durante el estado de reposo con los ojos abiertos de un sujeto. Estos datos segmentados fueron seleccionados debido a su idoneidad para el análisis y procesamiento de señales EEG. El archivo contiene información registrada mediante cuatro canales: T7, F8, Cz y P4.
</p>
<p align="justify">
A continuación, se muestra una vista previa de las señales segmentadas:
</p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/main/ISB/Laboratorios/Im%C3%A1genes/EEG/tablalab10.png" alt="fotog" width="400" height="200"/>
</p>
<p align="center"><i> Tabla 1:  Vista previa de las datos segmentadas (4 canales) </i></p>

## 3.2. Filtro Butterworth <a name="id3.2"></a>
## 3.3. Filtro por Análisis de Componentes Independientes (ICA) <a name="id3.3"></a>
## 3.4. Normalización y Alinemamiento <a name="id3.4"></a>
## 3.5. Extracción de Características <a name="id3.5"></a>

<p align="justify">

 </p>


# 4.Resultados<a name="id4"></a>

## 4.1. Obtencion de la data segmentada
|  **Señales Segmentadas**  |
|:------------:|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/6a697a00-504c-424a-a119-f5cd8bbd62c9)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/1190cfd0-7285-4b18-ab2a-21e8eb33f686)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/16be61b0-c4d2-44a8-a9a7-5f622e3d3c11)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/56bb6390-9167-4acf-8e27-389208e99a0d)|

## 4.2. Aplicación de Filtro Butterworth e ICA

|  **EEG Filtrada      -       EEG Filtrada + ICA**  |
|:------------:|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/fe90f1e3-df4f-4fd0-8090-39e4b67d7dcd)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/b5bd8ecc-8389-47af-9e52-885eedaaacd6)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/1c8b5fad-8a54-4abc-8545-08983251e673)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/3cc76a0f-be2a-4d95-b6dd-7d20779a6daa)|


## 4.3. PSD de la señal cruda y la señal filtrada + ICA

|  Power Spectral Density(PSD) del canal (F8)|
|:------------:|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/c1251884-cf4d-4b06-a1b5-0967e0f51a89)|

## 4.4. Wavelet - Extracción de Caraterísticas

|  **Extracción de Caraterísticas - Daubechies wavelet de orden 4**  |
|:------------:|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/1e4f2fec-4100-4128-a4ed-6738576da799)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/43c57ab4-bb37-447b-bac1-fffb7ea25dc6)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/09bbc5e0-62d0-4632-8733-a03e9942c298)|
|![image](https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164552077/6eed3db4-17b9-4413-bc8f-ff208e6bb6c0)|
# 5.Discusión<a name="id5"></a>

# 6.Referencias bibliográficas<a name="id6"></a>
[1]	S. Sanei y J. Chambers, «EEG Signal Processing».

[2]	«Indep. Comp. Analysis», EEGLAB Wiki. Accedido: 19 de junio de 2024. [En línea]. Disponible en: https://just-the-docs.github.io/tutorials/ConceptsGuide/ICA_background.html

[3]A. Goldberger et al., "PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals," Circulation [Online], vol. 101, no. 23, pp. e215–e220, 2000. 
