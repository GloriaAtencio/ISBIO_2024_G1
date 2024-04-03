# Planteamiento del problema y solución
**Contexto:**

Las enfermedades cardíacas son la principal causa de muerte a nivel mundial, con millones de personas afectadas cada año. 
Las enfermedades cardíacas son un problema de salud pública importante en Perú. Según el Ministerio de Salud, las enfermedades cardiovasculares son la principal causa de muerte en el país, con una tasa de mortalidad de 148 por cada 100.000 habitantes.

El doctor Ángel Cueva Parra, especialista en electrofisiología cardíaca, señaló que alrededor de 1 millón de personas en Perú sufren de arritmia, con una incidencia más alta en hombres mayores de 40 años. Durante la pandemia, estos pacientes han sido tratados en el servicio de Cardiología del Hospital Almenara, que es el principal centro de referencia para el tratamiento de esta condición.[1]

**Problemática:**
- Análisis manual del ECG: El análisis tradicional del electrocardiograma (ECG) requiere de personal médico altamente calificado y puede ser susceptible a errores humanos.
- Falta de detección de arritmias esporádicas: Los equipos de ECG estándar no siempre capturan arritmias que ocurren fuera del período de registro.
- Acceso limitado a la atención médica: En muchas regiones, el acceso a especialistas en cardiología es limitado, lo que dificulta el diagnóstico oportuno de enfermedades cardíacas. [2]

**Estado del Arte:**
1. Algoritmo para identificar y cuantificar cuadros arrítmicos utilizando Matlab.
   
  Se propone un algoritmo simple para identificar arritmias cardíacas a partir de la localización de los picos de las ondas P, Q, R y S de un electrocardiograma (ECG). El estudio se basa   en la importancia del ECG como herramienta para detectar arritmias, utilizando la derivación V5 del ECG debido a su característica de tener una onda P con amplitud positiva.
  La metodología del proyecto se basa en dos fases principales: la localización de los puntos máximos de las ondas P, Q, R y S del ECG, y la identificación de arritmias de acuerdo a los    criterios y  características de las ondas . Se utilizan señales de ECG obtenidas de la Arrhythmia DataBase del MIT-BIH, con la derivación V5 y una velocidad de muestreo de 360 Hz. [3]

2. Discrete wavelet transform-based ECG features detection and extraction using low-cost ADS1293EVM

  Se presenta técnicas automáticas de detección y extracción de características en señales de ECG reales utilizando plataformas de bajo costo y algoritmos basados en la transformada        discreta de wavelet
  La plataforma utilizada para adquirir las señales de ECG es la tarjeta de adquisición ADS1293EVM y se utiliza el software MATLAB para calcular estas señales. El programa desarrollado     se evalúa con 30 registros de ECG de 6 segundos de duración, obteniendo resultados en la detección de características de interés superiores al 90%.
  Los resultados obtenidos muestran una alta precisión en la detección de características relevantes en las señales de ECG, lo que sugiere la viabilidad y efectividad de esta metodología   para aplicaciones clínicas y de diagnóstico.[4]

**Propuesta de Solución:**

Desarrollar un sistema integral para el diagnóstico de enfermedades cardíacas que combine las siguientes tecnologías:
 - Dispositivo portátil de monitorización de ECG: Un dispositivo portátil que captura continuamente la señal de ECG del paciente y la transmite a un sistema de análisis remoto.
 - Análisis automático de ECG: Un algoritmo de análisis automático que utiliza técnicas de extracción de características, selección de características y aprendizaje automático para          detectar arritmias cardíacas y clasificarlas con alta precisión.
 - Plataforma de telemedicina: Una plataforma que permite la comunicación entre el paciente, el dispositivo portátil y el médico especialista, facilitando la consulta y el diagnóstico a     distancia.

**Beneficios:**

Mejora en la precisión del diagnóstico: El análisis automático del ECG puede mejorar la precisión del diagnóstico al reducir la variabilidad interobservadora.
Detección temprana de arritmias: La monitorización continua del ECG permite la detección temprana de arritmias esporádicas que podrían pasar desapercibidas con los métodos tradicionales.
Mayor acceso a la atención médica: La telemedicina permite que los pacientes en áreas remotas tengan acceso a especialistas en cardiología.

**Referencias bibliográficas:**

**[1]“EsSalud advierte que varones mayores de 40 años son los que más padecen de arritmias cardíacas,” Essalud, Nov. 30, 2022. http://noticias.essalud.gob.pe/?inno-noticia=essalud-advierte-que-varones-mayores-de-40-anos-son-los-que-mas-padecen-de-arritmias-cardiacas#:~:text=Por%20su%20parte%2C%20el%20doctor**

**[2]Y. Ansari, O. Mourad, K. Qaraqe y E. Serpedin, “Deep learning for ECG Arrhythmia detection and classification:** 
**an overview of progress for period 2017–2023”, Frontiers Physiol., vol. 14, septiembre de 2023. doi: 10.3389/fphys.2023.1246746.**

**[3] F. Vega L., A.G. Cadena H., S. Larraza R., "Algoritmo para identificar y cuantificar cuadros arrítmicos utilizando Matlab,"** 
**en Actas de la Conferencia de Ingeniería Biomédica, Universidad de Monterrey, Nuevo León, México, 2024. dx.doi.org/10.24254/CNIB.17.60**

**[4]O. I. Coronado Reyes, A. D. C. Téllez Anguiano, J. A. Gutiérrez Gnecchi and M. E. Olvera Cortes,"Discrete wavelet transform-based**
**ECG features detection and extraction using low-cost ADS1293EVM," 2023 IEEE International Autumn Meeting on Power,**
**Electronics and Computing (ROPEC), Ixtapa, Mexico, 2023, pp. 1-6, doi: 10.1109/ROPEC58757.2023.10409404.**

**PPT**

<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGBUOTVuPE&#x2F;Qk2MVuU3_7_si0GifD074g&#x2F;view?utm_content=DAGBUOTVuPE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Entregable 2:Planteamiento de Problemática y propuesta de solución</a> de GRUPO 1
