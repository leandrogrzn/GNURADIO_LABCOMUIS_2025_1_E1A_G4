# Práctica 1C. Mediciones de potencia y frecuencia
### Integrantes
- **Leandro José Garzón Niteto** - 2194232
- **David Josué Díaz Ortiz** - 2204269

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
5 de Marzo de 2025

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento. 

Uso de IA: [Indicar si se usó IA y para qué aspectos específicos, por ejemplo: "Se utilizó ChatGPT para reformular secciones del texto y verificar gramática, pero el contenido técnico fue desarrollado íntegramente por los autores."]

---

## Contenido

### Resumen
Esta practica se enfoco en la medicion de potencia y frecuencia en sistemas de radio definidos por dicho software el cual se utilizo GNU Radio y equipos especializados como el osciloscopio y el analizador de espectros. En la cual se realizaron las actividades propuestas por la guia para comprender el comportamiento de estas señales en el dominio del tiempo y frecuencia. Para llevar a cabo esta practica primero se revisaron las especificaciones de los equipos, identificando parametros claves como rango de frecuencia y ganancia. Luego de esto se simularon las señales en GNU Radio para anallizar su comportamiento al modificar caracteristicas como forma de onda y amplitud. Posteriormente se transmitieron señales con el GNU Radio evaluando potencia, ancho de banda y relacion señal a ruido mediante mediciones con el analizador de espectros y el osciloscopio. Finalmente se compararon los resultados de simulacion y experimentacion.

**Palabras clave:** Relacion señal a ruido (SNR), Ganancia, Frecuencia.

### Introducción
En las telecomunicaciones, entender cómo se comportan las señales es clave para garantizar una transmisión eficiente. En esta práctica, se exploró el uso del radio definido por software (SDR) USRP 2920 y su comparación con el analizador de espectros R&S FPC1000 para evaluar su rango de frecuencia. Además, se configuraron parámetros como la frecuencia de transmisión y la ganancia del GNU Radio, analizando su impacto en la señal generada. También se utilizó un osciloscopio R&S RTB2004 para medir la amplitud y la frecuencia en el dominio del tiempo, comparándolo con el análisis en el dominio de la frecuencia usando el analizador de espectros. Finalmente, se estudió el concepto de piso de ruido y cómo factores como la frecuencia central, el SPAN y la resolución de ancho de banda (RBW) afectan su medición, lo que es esencial para la detección de señales débiles en entornos reales.

### Procedimiento
Para llevar a cabo esta práctica, se realizaron tres actividades principales: la revisión y configuración de los equipos de medición, la simulación de señales en GNU Radio y la transmisión y análisis de señales con el USRP 2920. A continuación, se detallan los pasos a seguir en cada actividad:

## **Actividad 1: Revisión de Especificaciones de los Equipos**
Para llevar a cabo esta practica primero se realizo una revision detallada de los equipos de laboratorio con el objetivo de comprender su fincionamiento y configuraciones clave, a partie de esto se consultaron los manuales del GNU Radio, el osciloscopio y el analizador de espectros para conocer sus especificaciones tecnicas y las funciones de control mas relevantes de estos dispositivos.

### **Evidencia**
- Lista con las 5 especificaciones más relevantes de cada equipo.
#### **Osciloscopio(R&s RTB2004):**
1. Ancho de banda: Tiene disponible bandas de 70MHz a 300MHz.
2. Velocidad de muestreo: Tiene una velocidad de muestreo de hasta 2.5 GSa/s (gigasamples por segundo).
3. Memoria profunda de canal: Ofrece una memoria de adquisicion en el modo normal de 10 Mpts y en el modo intercalado de 20 Mpts.
4. Pantalla: Cuenta con una pantalla tactil de 10.1 pulgadas.
5. Conectividad: Dispone de puertos LAN y USB para control remoto y transferencia de datos.
#### **Analizador de espectros(R&S FPC1000):**
1. Rango de frecuancias: Cuenta con un rango de frecuencias de 5KHz a 1GHz.
2. Resolucion de ancho de banda: Ajustable entre 1Hz y 3MHz.
3. Maximo nivel de entrada: Hasta 36dBm(4 W).
4. Nivel de barrido: Ajustable manualmente o modo automatico desde 20ms hasta 600MHz de ancho de banda.
5. Pantalla y conectividad: Posee una pantalla de 10.1 pulgadas, interfaz USB y conectividad WI-FI. 
#### **USRP-2920:**
1. Rango de frecuencias: Soporta señales desde 50MHz hasta 2.2GHz.
2. Ancho de banda: Dependiendo del muestreo el ancho de banda puede ser de hasta 20MHz con 16 bits y 40MHz con 8 bits.
3. Potencia de salida maxima: Varia segun la frecuencia:
 - de 50 MHz a 1.2 GHz: entre 50 mW a 100 mW(17dBm a 20dBm)
 - de 1.2 GHz a 2.2 GHz: entre 30 mW a 70 mW(15dBm a 18dBm)
4. Rango de ganancia: Desde 0 dB a 31.5 dB.
5. Potencia:
 - tipica: 12 W hasta 15 W.
 - maxima: 18 W. 

## **Actividad 2: Simulación de Señales en GNU Radio**
Para  llavar a cabo la simulacion de señales se utilizo GNU Radio, configurando y ejecutando un flujograma, identificando los bloques claves y ajustando las frecuencias de muestreo correspondientes a la practica. Se analizaron las señales en el dominio del tiempo y de la frecuencia observando la relacion entre los bloques y los resultados obtenidos, evaluando el impacto al modificar los parametros como el tipo de dato (complejo o flotante), forma de onda, frecuencia, fase, amplitud y nivel de ruido.

### **Evidencia**
- Capturas de pantalla de las señales generadas en el dominio del tiempo y la frecuencia.

La diferencia matematica entre una señal flotante y una comleja tomando como referencia un coseno se puede describir de la siguiente manera:

- Fuente flotante real
$$ x(t) = A\cos^2(2 \pi f t + \phi) $$
Donde A es la amplitud, f es la frecuencia y phi la fase. Esta señal tiene dos picos espectrales de +/- f debido a la entidad de euler, esto hace que se refleje en el espectro como dos componentes simetricas.

- Fuente compleja
$$ x_{c}(t) = A e^{j(2 \pi f t + \phi)} $$
$$ e^{j(2 \pi f t + \phi)} = \cos(2 \pi f t) + j \sin(2 \pi f t) $$

Esta en el dominio de la frecuencia solo tiene un pico en la frecuancia f, eliminando la componente negativa.


#### Coseno complejo
<img src="./capturas/coseno_complex.png" alt="Coseno complejo" width="600">

#### Coseno flotante
<img src="./capturas/coseno_float.png" alt="Coseno complejo" width="600">

#### Triangular complejo
<img src="./capturas/triangular_complex.png" alt="triangular_complex" width="600">

#### Triangular flotante
<img src="./capturas/triangular_float.png" alt="triangular_float" width="600">

#### Cuadrada complejo
<img src="./capturas/cuadrada_complex.png" alt="cuadrada_complex" width="600">

#### Cuadrada flotante
<img src="./capturas/cuadrada_float.png" alt="cuadrada_float" width="600">





### Conclusiones
Se sintetizan los principales aportes y puntos relevantes de la práctica, evitando repetir lo ya consignado en las otras secciones del informe. 

### Referencias
Ejemplo de referencia:

- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. p. 164-165, 346. Chapter 5 In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)

---