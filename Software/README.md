# Características del software

***

# **Tabla de contenidos**
1. [Introducción](#id1)
2. [Procedimiento](#id2)
3. [Ploteos y análisis](#id3)
4. [Resultados](#id4)
5. [Referencias bibliográficas](#id6) 

***

# 1.Introducción<a name="id1"></a>

<p align="justify">

## Objetivo:

- Desarrollar un método para analizar señales de ECG y detectar con precisión niveles de fobia en pacientes con fobias específicas como la aracnofobia.
- Crear una interfaz gráfica amigable (GUI) utilizando Tkinter para visualizar e interactuar con los datos de ECG y BPM.
- Realizar análisis estadísticos como ANOVA y visualización de diagramas de caja para evaluar diferencias significativas en BPM entre diferentes niveles de fobia (alta, moderada, baja). Esto ayuda a validar la efectividad del uso de métricas de ECG (BPM y HRV) para la evaluación objetiva de fobias.

</p>

# 2.Procedimiento<a name="id2"></a>

### Materiales

<p align="justify">
- Anaconda 
- Visual Studio Code
</p>

Bibliotecas usadas:
- numpy
- SciPy
- Pandas
- Matplotlib
- PyWavelets

### 2.1. Organización de archivos en VSC 

<p align="justify">
Al haber un total de 57 personas que son tomadas como la muestra, todas los archivos fueron obtenidos de PhysioNet y al descargarlos se obtuvieron 57 carpetas denominadas VP.Dentro de ellas se encontraban dos archivos txt: BitalinoECG.txt y Triggers.txt. 
</p>

<p align="justify">
- BitalinoECG.txt: Electrocardiograma en mV (columna 1), rango de valores de -1.5 mV a 1.5 mV; marca de tiempo con formato hhmmss.milliseconds (columna 2, utilizada para el mapeo de las ventanas de tiempo del videoclip); etiqueta para datos RAW (columna 3, puede ser ignorada).
</p>

<p align="justify">
- Triggers.txt: ID de disparador utilizando CLIP-1 a CLIP-16 como videoclips que estimulan la ansiedad (columna 1) y BIOFEEDBACK-REST para la fase de descanso; marca de tiempo con formato hhmmss para el inicio (columna 2) y el final (columna 3) del videoclip o fase de descanso.
</p>

# 3.Ploteos y análisis<a name="id3"></a>

## Código empleado - Python

```python





```

# 4.Resultados<a name="id4"></a>




# 5.Referencias bibliográficas<a name="id5"></a>
