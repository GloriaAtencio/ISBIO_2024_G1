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



## Código empleado 

unsigned long lastMsg = 0;
float F=1;                      // 1 hz
double Fs = 50*F;               // 10 hz
double Ts_ms = (1/Fs)*1000;     //  100 ms  

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



