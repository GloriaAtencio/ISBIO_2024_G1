# **Laboratorio N°5: Uso de BiTalino para EEG**

***

# **Tabla de contenidos**
1. [Contexto](#id1)
2. [Procedimiento](#id2)
3. [Videos](#id3)
4. [Ploteos y análisis](#id4)
5. [Discusión](#id5)
6. [Referencias bibliográficas](#id6) 

***

# 1.Contexto<a name="id1"></a>

<p align="justify">

</p>


# 2.Procedimiento<a name="id2"></a>

## Conexión del BiTalino 

### Materiales y equipos 

|     Modelo       |                  Descripción                  |   Cantidad    |
|  :-------------: |:--------------------------------------------: |:-------------:|
| (R)EVOLUTION     | Kit BITalino                                  | 1             |
| -                | Laptop                                        | 1             |

<p align="center">
 <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/9a7420da071748b34dc40f665ea7b1db2cfc3242/ISB/Laboratorios/Im%C3%A1genes/ECG/mat_bitalino_ecg.jpeg" alt="fotog" width="500" height="300"/>
</p>
<p align="center"><i>Figura 1. Tarjeta BiTalino</i></p>

### Posicionamiento de electrodos

<p align="justify">

</p>

# 3.Videos<a name="id3"></a>

## Caso 1: Respiración normal, sin movimientos oculares/ojos cerrados durante 30 segundos

<p align="justify">

</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/reposo_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>|
</div>

## Caso 2: Ciclo de ojos abiertos - ojos cerrados cinco veces

<p align="justify">

</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/reposo_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>|
</div>

## Caso 3: Fase de referencia de 30 segundos

<p align="justify">

</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/reposo_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>|
</div>

## Caso 4: Solución de serie de ejercicios matemáticos

<p align="justify">

</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/reposo_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>|
</div>

## Caso 5: Solución de acertijos

<p align="justify">

</p>

<div align="center">
  
|  **Señal en OpenSignals**  | **Video** |
|:------------:|:---------------:|
|<img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/10c003765b5e66b1e052993c466b867c704fb94a/ISB/Laboratorios/Im%C3%A1genes/ECG/reposo_op.png" alt="fotog" />|<video src="https://github.com/GloriaAtencio/ISBIO_2024_G1/assets/164522281/33cc886b-a9b8-4a4b-af11-691bb0b28b30" width="300" height="300"></video>|
</div>

# 4.Ploteos y análisis<a name="id4"></a>

## Caso 1: Respiración normal, sin movimientos oculares/ojos cerrados durante 30 segundos

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal EEG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

<p align="justify">

</p>

## Caso 2: Ciclo de ojos abiertos - ojos cerrados cinco veces

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/c_a_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal ECG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/c_a_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

<p align="justify">

</p>

## Caso 3: Fase de referencia de 30 segundos

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo2_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal ECG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/reposo2_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

<p align="justify">

</p>

## Caso 4: Solución de acertijos

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/acertijo_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal ECG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/acertijos_fft_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

<p align="justify">

</p>

## Caso 5: Solución de preguntas de 100 peruanos dicen


<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/100preruanosdicen_plot.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 10. Reconstrucción de la señal ECG obtenida durante el reposo a partir de los datos txt adquiridos en Open Signals</i></p>

<p align="center">
  <img src="https://github.com/GloriaAtencio/ISBIO_2024_G1/blob/0ca257ca920d49329a3f88ed40c87eec76aa313f/ISB/Laboratorios/Im%C3%A1genes/EEG/plot_eeg/100peruanosdicen_fft.jpeg" alt="fotog" width="560" height="300"/>
</p>
<p align="center"><i>Figura 11. Ploteo de la Señal ECG obtenida durante el reposo en python</i></p>

<p align="justify">

</p>

## Código empleado - Python


# 5.Discusión<a name="id5"></a>

<p align="justify">

</p>

# 6.Referencias bibliográficas<a name="id6"></a>

<p align="justify">

</p>
