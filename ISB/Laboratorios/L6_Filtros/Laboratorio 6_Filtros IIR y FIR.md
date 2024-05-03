# **Laboratorio N°6: Uso de filtros IIR y FIR**

***

# **Tabla de contenidos**
1. [Introducción](#id1)
2. [Procesamiento de data](#id2)
3. [Señales](#id3)
4. [Ploteos de señales filtradas y análisis](#id4)
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

***

# 1.Introducción<a name="id1"></a>

<p align="justify">
</p>

## Objetivo:

El objetivo de este laboratorio es registrar y analizar la señal electroencefalográfica (EEG) de un sujeto durante diferentes estados de actividad cerebral.  específicamente, se busca:

-  filtrar las frecuencias altas, que corresponden a ruido, del dataset de  ECG creado en el laboratorio anterior.  
- diseñar 2 filtros uno IIR y uno FIR, para realizar el filtrado.
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
