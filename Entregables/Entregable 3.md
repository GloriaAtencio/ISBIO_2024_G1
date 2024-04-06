# Entregable 3: Ploteo de señales

## Objetivos

- Obtener señales reconocidas como cuadradas, triangulares, senoidales, rampas, entre otras.
- Comprender los factores que influyen en la elección de la frecuencia de muestreo.
- Manejar y ajustar correctamente un suministro de energía regulable, un multímetro digital, un generador de señales y un osciloscopio digital.


## Materiales y equipos
|     Modelo       |                  Descripción                  |   Cantidad    |
|  :-------------: |:--------------------------------------------: |:-------------:|
| AFG1022          | Generador de Señales                          | 1             |
| TBS 1000C Series | Osciloscopio Digital                          | 1             |
| -                | Cable BNC Male- Male                          | 1             |
| -                | Punta de osciloscopio con conector BNC(Male)  | 1             |
| -                | Par de cables Male- Male                      | 1             |
| SAMD             | Arduino 33 loT                                | 1             |

## Procedimiento

### Adquisición de señales
- Primero, encendimos el Generador de Señales y el Osciloscopio
- Configuramos el Generador de Señales para proporcionar una señal sinusoidal de 1 kHz de frecuencia, 
3 V de High Level y 0V de offset, por el canal 1.
- Mediante los controles de Posición Vertical, Horizontal y Disparo ajustamos la visualización de la señal 
sinusoidal.
- Configuramos el Generador de Señales para proporcionar una señal sinusoidal de 1 Hz de frecuencia, 
1.5V de High Level y 0V de offset, por el canal 2.
- Se buscaron las medidas de la amplitud de ambas señales usando measure.
- Conectamos la Punta de osciloscopio con conector BNC en el canal 2 del generador de señales y la unimos al puerto A0 del arduino.
  
### Visualización de señal en el plotter en Arduino ino
Para ello, utilizamos el código en el cual especificamos nuestra frecuencia F que en este caso fue de 1 Hz.Asimismo, usamos analogRead() para poder leer la señal que correspondía al pin A0 del arduino. Finalmente, para que la señal pueda ser ploteada agregamos la función Serial.println(). Luego, de todos estos pasos pudimos obtener el ploteo de la señal y así poder realizar el ingreso de distintal señales a fin de compararlas.

## Código empleado 
```
unsigned long lastMsg = 0;
float F=1;                      // 1 Hz
double Fs = 50*F;               // 50 Hz
double Ts_ms = (1/Fs)*1000;     //  20 ms  

void setup() {
  Serial.begin(9600);
  while (!Serial);
  //Serial.println("R1:");
}

void loop() {

  unsigned long now = millis();

  if (now - lastMsg > Ts_ms) {
    
    lastMsg = now;

    int r1 = analogRead(A0);

    Serial.print("Señal1:");
    Serial.println(r1);
    Serial.print(",");
    
  }
}
```


#### 1.Señal configurada en el generador de señales (canal 2):

Los parámetros para las señales son las siguientes:
- Frecuencia: 1Hz
- Amplitud: 3V
- Offset: 0V

##### 1.1 Señal sinusoidal: 

##### 1.2 Señal cuadrada:

##### 1.3 Señal Rampa:





