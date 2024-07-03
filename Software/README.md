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

### 2.1. Organización y lectura de archivos en VSC 

<p align="justify">
Al haber un total de 57 personas que son tomadas como la muestra, todas los archivos fueron obtenidos de PhysioNet y al descargarlos se obtuvieron 57 carpetas denominadas VP.Dentro de ellas se encontraban dos archivos txt: BitalinoECG.txt y Triggers.txt. 
</p>

<p align="justify">
- BitalinoECG.txt: Electrocardiograma en mV (columna 1), rango de valores de -1.5 mV a 1.5 mV; marca de tiempo con formato hhmmss.milliseconds (columna 2, utilizada para el mapeo de las ventanas de tiempo del videoclip); etiqueta para datos RAW (columna 3, puede ser ignorada).
</p>

<p align="justify">
- Triggers.txt: ID de disparador utilizando CLIP-1 a CLIP-16 como videoclips que estimulan la ansiedad (columna 1) y BIOFEEDBACK-REST para la fase de descanso; marca de tiempo con formato hhmmss para el inicio (columna 2) y el final (columna 3) del videoclip o fase de descanso.
</p>

<p align="justify">
Entonces para empezar el proyecto se creó un entorno virtual de Python versión 3.9.16 en Anaconda, y se optó por almacenar todas las carpetas VP en una sola carpeta denominada "ECG". Con la finalidad de acceder a los archivos txt se realizó un for que leyera cada carpeta de los sujetos.
</p>

#### Configuración de Directorios y Archivos

- Definición de Directorios: base_dir y output_dir son definidos para especificar las ubicaciones de los datos de ECG de entrada y donde se guardarán los resultados, respectivamente.
- Obtención de Carpetas de VP: Se utilizan glob.glob y os.path.join para obtener todas las carpetas de los sujetos VP (por ejemplo, VP01, VP02, etc.) dentro de base_dir.


#### Procesamiento de Clips Individuales

Iteración sobre Carpetas VP: Para cada carpeta VP:

- Creación de Archivo Excel: Se crea un archivo Excel usando pd.ExcelWriter donde se almacenarán los resultados para ese VP específico.

- Lectura de Datos ECG y Triggers: Los datos de la señal ECG (BitalinoECG.txt) y los disparadores (Triggers.txt) se leen en pandas DataFrames. Los datos de ECG se filtran para cada clip definido por los disparadores.

- Creación de Directorios de Salida: Se crea un directorio de salida específico para cada VP dentro de output_dir.

### 2.2. Procesamiento de Datos de ECG para Cada Clip (Triggers.txt)

<div align="center">
<h2> Filtrado de la Señal ECG </h2>
</div>
Se filtra la señal ECG utilizando la wavelet 'db5' y se reconstruye la señal filtrada. Y para ello se empleó el siguiente código:

```python
# Apply wavelet filtering with db5
                signal = clip_data['ECG'].values
                max_level = pywt.dwt_max_level(len(signal), 'db5')
                level = min(5, max_level)
                if len(signal) > 0:
                    coeffs = pywt.wavedec(signal, 'db5', level=level)
                    reconstructed_signal = pywt.waverec(coeffs, 'db5')
                    clip_data['Filtered_ECG'] = reconstructed_signal[:len(signal)]

```
<div align="center">
<h2> Cálculo del BPM </h2>
</div> 

Se utilizó la función calculate_bpm que nos permitió calcular el BPM para la señal ECG filtrada.

```python
def calculate_bpm(ecg_signal, fs):
    # Normalización de la señal ECG (opcional)
    ecg_signal_norm = (ecg_signal - np.mean(ecg_signal)) / np.std(ecg_signal)

    # Detección de picos R usando find_peaks
    peaks, _ = find_peaks(ecg_signal_norm, distance=int(fs * 0.6))

    # Calcular intervalos RR (en segundos)
    rr_intervals = np.diff(peaks) / fs

    # Calcular el promedio de los intervalos RR
    mean_rr_interval = np.mean(rr_intervals)

    # Calcular el BPM
    bpm = 60 / mean_rr_interval

    return bpm, rr_intervals

```
<div align="center">
<h2> Visualización y Guardado de Gráficos </h2>
</div>

Se genera un gráfico de la señal ECG filtrada con el valor de BPM mostrado, y se guarda como una imagen PNG en el directorio de salida del VP.

```python
                    plt.figure(figsize=(10, 4))
                    plt.plot(clip_data['Seconds'], clip_data['Filtered_ECG'], label='Filtered ECG (db5)')
                    plt.xlabel('Time (s)')
                    plt.ylabel('ECG (mV)')
                    plt.title(f'ECG Signal with db5 Wavelet Filter for {clip_id}')
                    plt.legend()
                    plt.grid(True)
                    plt.text(0.95, 0.95, f'BPM: {float(bpm):.2f}', transform=plt.gca().transAxes, fontsize=14, ha='right', va='top',
                             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
                    output_file = os.path.join(vp_output_dir, f'{clip_id}_ecg_plot_with_db5_filter.png')
                    plt.savefig(output_file)
                    plt.close()
```
<p align="justify">
La señal ECG filtrada se guarda como una hoja de datos en el archivo Excel del VP correspondiente. Simultáneamente, los valores de BPM calculados para cada clip se agregan a una lista denominada bpm_list, acompañados del ID del clip respectivo, para un seguimiento organizado y para facilitar la clasificación posterior.
</p>

<div align="center">
<h2> Cálculo de Métricas de HRV </h2>
</div>

<p align="justify">
En el paso de calcular métricas HRV (variabilidad de la frecuencia cardíaca), se siguen los siguientes procedimientos:
</p>


<p align="justify">
- Filtrado de Intervalos RR: Los intervalos RR (intervalos de tiempo entre latidos consecutivos) se convierten a un array de NumPy para facilitar el cálculo. Luego, se eliminan los intervalos RR que son cero o negativos, ya que estos valores no son válidos para el análisis de HRV.
</p>


### Cálculo de Métricas Básicas:

<p align="justify">
- Intervalos NN: Se consideran los intervalos RR como intervalos NN (normal a normal).
</p>

<p align="justify">
- Media y Desviación Estándar de los Intervalos RR: Se calcula la media (rr_mean) y la desviación estándar (rr_std) de los intervalos RR.
</p>

<p align="justify">
- Media y Desviación Estándar de la Frecuencia Cardíaca: La frecuencia cardíaca media (hr_mean) se calcula como 60 dividido por la media de los intervalos RR (esto convierte los intervalos en frecuencia en latidos por minuto). La desviación estándar de la frecuencia cardíaca (hr_std) se obtiene calculando la frecuencia cardíaca para cada intervalo RR y luego hallando su desviación estándar.
</p>

<p align="justify">
- Cálculo del RMSSD: La raíz cuadrada de la media de las diferencias cuadráticas sucesivas (rmssd) se calcula a partir de las diferencias entre intervalos RR consecutivos. Este es un indicador común de la variabilidad de la frecuencia cardíaca.
</p>

<p align="justify">
Las métricas calculadas (intervalos NN, media y desviación estándar de los intervalos RR, media y desviación estándar de la frecuencia cardíaca, y RMSSD) se devuelven como un diccionario.
</p>

# 3.Ploteos y análisis<a name="id3"></a>

## Código empleado - Python

```python





```

# 4.Resultados<a name="id4"></a>




# 5.Referencias bibliográficas<a name="id5"></a>
