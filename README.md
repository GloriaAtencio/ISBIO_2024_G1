<img src="https://img.freepik.com/fotos-premium/electrocardiograma-linea-latidos-pulso-traza-pulso-ecg-o-ekg-simbolo-grafico-cardio-salud-medicina_941429-23.jpg" alt="img principal" width="900" height="150"/>


========================================================================
# Introducción a Señales Biomédicas Grupo 1 (2024-1)
**Repositorio del curso**
**Integrantes:**

- Jennyfer Arantxa Arismendiz Millones(colaborador)- jennyfer.arismendiz@upch.pe
- Gloria Elvira Atencio Inga (colaborador) - gloria.atencio@upch.pe
- Raul Ricardo Gonzales Rodriguez (colaborador) - raul.gonzales@upch.pe
- Jhoana Olenka Rodriguez Diaz (colaborador)- jhoana.rodriguez@upch.pe

¡Bienvenidos! Somos el Grupo 1 del curso de Introducción a Señales Biomédicas. Nos apasiona el estudio de las señales EKG y estamos emocionados de compartir nuestro proyecto, 
donde exploramos en profundidad este fascinante campo. ¡Acompáñennos en este viaje hacia el corazón de la investigación biomédica! 
# **Tabla de Contenidos**

- [¿Qué es una bioseñal?](#encabezado-1)
- [Materiales](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/578d3e4870fdf292068b64dc123e4c206030affb/Tabla%20de%20Contenidos/Materiales)
- [Metodología](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/5ef8e18c9a211c9320726f0674edbedbfe208614/Tabla%20de%20Contenidos/Metodolog%C3%ADa)
- [Temática del proyecto](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/9a58e6762a9c63dfe3a61f5c6325aef80b887556/Tabla%20de%20Contenidos/Tem%C3%A1tica%20del%20proyecto)
- [Contenido del curso](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/578d3e4870fdf292068b64dc123e4c206030affb/Tabla%20de%20Contenidos/Contenido%20del%20curso)
- [Participantes](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/578d3e4870fdf292068b64dc123e4c206030affb/Tabla%20de%20Contenidos/Participantes)
- [Docentes del curso](https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/578d3e4870fdf292068b64dc123e4c206030affb/Tabla%20de%20Contenidos/Docente%20del%20curso)
  

# Acerca de nosotros:
# **Gloria Elvira Atencio Inga**
Estudiante de 8vo ciclo de la carrera de Ingeniería Biomédica PUCP-UPCH, mi área de interes es la ingenieria clínica y la ingeniería de tejidos.  Mi pasión por este campo se centra en la creación y ejecución de soluciones innovadoras que puedan mejorar la atención médica y contribuir al avance tecnológico en el sector de la salud. Correo personal: gloria.atencio@upch.pe

<p align="center">
  <img src="Fotos/gloria.jpeg" alt="fotog" width="220" height="300"/>
</p>

# **Jennyfer Arantxa Arismendiz Millones**
Estudiante del 7mo ciclo de la carrera de Ingeniería Biomédica PUCP-UCH, mis principales enfoques son las ramas de biomateriales e ingeniería clínica. Asimismo, muestro gran interés en el proceso de creación junto con desarrollo de proyectos innovadores que apoyan el campo médico.Correo personal: jennyfer.arismendiz@upch.pe

<p align="center">
  <img src="Fotos/jennyfer.jfif" alt="fotoj" width="220" height="300"/>
</p>



# **Jhoana Olenka Rodriguez Diaz**
Estudiante de la carrera de Ingeniería Biomédica que cursa su octavo ciclo y desea especializarse en las ramas de Ingeniería clínica e Imagenes.Me gusta la planificación de proyectos relacionados a los temas mencionados y también he sido partícipe sobre la creación de plantillas para pacientes de pie Diabetico Correo personal: rodriguezjhoana2802@gmail.com
<p align="center">
  <img src="Fotos/jhoana.jpg" alt="fotog" width="220" height="300"/>
</p>

# **Raul Ricardo Gonzales Rodriguez**
Estudiante de 7mo ciclo de la carrera de Ingeniería Biomédica. Mi enfoque se centra en aplicar los principios de la ingeniería , sobretodo en mi área de interés en Ingeniería Clinica; particularmente en investigación en gestión tecnológica y  metrología biomédica. Considero tener habilidades analíticas y críticas al momento de trabajar en equipo. Correo personal: raul.gonzales@upch.pe
<p align="center">
  <img src="Fotos/raul.jpg" alt="fotog" width="220" height="300"/>
</p>

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





