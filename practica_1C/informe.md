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

## **Actividad 3: Transmisión y Medición de Señales con el USRP 2920**
En esta actividad se exploró la transmisión y medición de señales con el USRP 2920, un sistema de radio definido por software (SDR). Se configuró el equipo en GNU Radio para transmitir señales y analizar su comportamiento en el dominio del tiempo y la frecuencia. Se midieron parámetros clave como potencia, ancho de banda, piso de ruido y relación señal a ruido (SNR) utilizando un analizador de espectros y un osciloscopio. Finalmente, se compararon diferentes configuraciones y medios de transmisión para evaluar el impacto en la calidad de la señal.

### **Evidencia**
- Capturas de pantalla de las mediciones realizadas en el analizador de espectros y el osciloscopio.

### **Señal Cuadrada**
<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <p>Espectro señal cuadrada tipo flotante</p>
    <img src="./capturas/square_float.jpg" alt="square_float" width="200" height="100">
  </div>
  <div>
    <p>Osciloscopio señal cuadrada tipo flotante</p>
    <img src="./capturas/osc_square_float.jpg" alt="osc_square_float" width="200" height="100">
  </div>
  <div>
    <p>GNU Radio señal cuadrada tipo flotante</p>
    <img src="./capturas/cuadrada_float.png" alt="cuadrada_float" width="200" height="100">
  </div>
</div>

<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <p>Espectro señal cuadrada tipo compleja</p>
    <img src="./capturas/square_complex.jpg" alt="square_complex" width="200" height="100">
  </div>
  <div>
    <p>Osciloscopio señal cuadrada tipo compleja</p>
    <img src="./capturas/osc_square_complex.jpg" alt="osc_square_complex" width="200" height="100">
  </div>
  <div>
    <p>GNU Radio señal cuadrada tipo compleja</p>
    <img src="./capturas/cuadrada_complex.png" alt="cuadrada_complex" width="200" height="100">
  </div>
</div>
Para calcular en ancho de banda se utilizo el criterio de 20dB, que consiste en tomar las muestras mas significativas que no pasen de mas de 20dB. En este caso el ancho de banda seria aproximadamente 30 KHz.

### **Señal Coseno**
<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <p>Espectro señal Coseno tipo flotante</p>
    <img src="./capturas/cos_float.jpg" alt="cos_float" width="200" height="100">
  </div>
  <div>
    <p>Osciloscopio señal Coseno tipo flotante</p>
    <img src="./capturas/osc_cos_float.jpg" alt="osc_cos_float" width="200" height="100">
  </div>
  <div>
    <p>GNU Radio señal Coseno tipo flotante</p>
    <img src="./capturas/coseno_float.png" alt="coseno_float" width="200" height="100">
  </div>
</div>

<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <p>Espectro señal Coseno tipo compleja</p>
    <img src="./capturas/cos_complex.jpg" alt="cos_complex" width="200" height="100">
  </div>
  <div>
    <p>Osciloscopio señal Coseno tipo compleja</p>
    <img src="./capturas/osc_cos_complex.jpg" alt="osc_cos_complex" width="200" height="100">
  </div>
  <div>
    <p>GNU Radio señal Coseno tipo compleja</p>
    <img src="./capturas/coseno_complex.png" alt="coseno_complex" width="200" height="100">
  </div>
</div>
En este caso se utilizo el espaciado del analizador de espectros a 1 KHz para un total del spam de 10 KHZ lo cual dio como resultado un ancho de banda aproximadamente de 4 KHz.

### **Señal Triangulo**
<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <p>Espectro señal Triangulo tipo flotante</p>
    <img src="./capturas/triangle_float.jpg" alt="cos_float" width="200" height="100">
  </div>
  <div>
    <p>Osciloscopio señal Triangulo tipo flotante</p>
    <img src="./capturas/osc_triangle_float.jpg" alt="osc_cos_float" width="200" height="100">
  </div>
  <div>
    <p>GNU Radio señal Triangulo tipo flotante</p>
    <img src="./capturas/triangulo_float.png" alt="coseno_float" width="200" height="100">
  </div>
</div>

<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <p>Espectro señal Triangulo tipo compleja</p>
    <img src="./capturas/triangle_complex.jpg" alt="cos_complex" width="200" height="100">
  </div>
  <div>
    <p>Osciloscopio señal Triangulo tipo compleja</p>
    <img src="./capturas/osc_triangle_complex.jpg" alt="osc_cos_complex" width="200" height="100">
  </div>
  <div>
    <p>GNU Radio señal Triangulo tipo compleja</p>
    <img src="./capturas/triangulo_complex.png" alt="coseno_complex" width="200" height="100">
  </div>
</div>
En este caso se utilizo el espaciado del analizador de espectros a 1 KHz para un total del spam de 10 KHZ lo cual dio como resultado un ancho de banda aproximadamente de 4 KHz.

### **Espectro de una señal FM**
La emisora FM que se sintonizó fue la 91.73 MHz, la cual tuvo un ancho de banda de 150 KHz.
<div style="display: flex; justify-content: space-evenly; align-items: center">
  <div>
    <img src="./capturas/FM_1.jpg" alt="cos_float" width="200" height="100">
  </div>
  <div>
    <img src="./capturas/FM.jpg" alt="osc_cos_float" width="200" height="100">
  </div>
</div>

## Para el calculo de la relacion señal a ruido (SNR) se utilizo la siguiente formula:
$$ SNR(dB) = 10 log_{10}(\frac{P_{señal}}{P_{ruido}}) $$
## Convertir los valores de dBm a mW:
$$ P(mW) = 10^{P(dBm)/10} $$

### Teniendo en cuenta lo anterior se calculo el SNR para las siguientes señales:
1. Señal Coseno
$$ P_{señal}(mW) = 10^{-30 dB/10} $$
$$ P_{señal}(mW) = 0.001 (mW) $$

$$ P_{ruido}(mW) = 10^{-80 dB/10} $$
$$ P_{ruido}(mW) = 10^{-8} (mW) $$

$$ SNR(dB) = 10 log_{10}(\frac{0.001}{10^{-8}}) $$
$$ SNR(dB) = 40 (dB) $$
---
2. Señal Triangulo
$$ P_{señal}(mW) = 10^{-30 dB/10} $$
$$ P_{señal}(mW) = 0.001 (mW) $$

$$ P_{ruido}(mW) = 10^{-85 dB/10} $$
$$ P_{ruido}(mW) = 3.162*10^{-9} (mW) $$

$$ SNR(dB) = 10 log_{10}(\frac{0.001}{3.162*10^{-9}}) $$
$$ SNR(dB) = 55 (dB) $$

## **Actividad 4: Análisis de Resultados y Conclusiones**

1. Comparacion de resultados:
   - A partir de las señales generadas en GNU Radio, verificamos que los resultados coincidían tanto con la simulación como con las mediciones realizadas en el analizador de espectro y el osciloscopio. En particular, observamos que la señal senoidal presenta en el dominio de la frecuencia dos componentes espectrales en su forma real, mientras que en su representación compleja aparece una única componente. Esta correspondencia se evidenció tanto en las simulaciones como en las mediciones experimentales, validando así el comportamiento esperado de la señal.
   - A partir del cálculo de la relación señal a ruido (SNR), se verificó que los valores teóricos coincidían con las mediciones obtenidas en el analizador de espectros, lo que confirma la precisión del modelo utilizado. En la práctica, se observó que la potencia de la señal y el nivel del piso de ruido medidos eran coherentes con los cálculos previos, lo que indica que los factores que afectan la transmisión, como la frecuencia, la ganancia y el tipo de modulación, fueron correctamente considerados.

2. Reflexionar sobre la SNR:
   - La relación señal a ruido (SNR) es un parámetro fundamental en las comunicaciones inalámbricas, ya que determina la calidad y confiabilidad de la transmisión de datos. Un SNR alto indica que la señal es significativamente más fuerte que el ruido de fondo, lo que permite una mejor recepción y reduce la probabilidad de errores. En cambio, un SNR bajo implica que la señal está más afectada por el ruido, lo que puede generar una mayor tasa de errores, pérdidas de paquetes y la necesidad de aplicar técnicas más avanzadas de corrección de errores.

3. Concluciones:
   - Las señales complejas permiten una representación más eficiente en términos de ancho de banda, mientras que las señales reales requieren el doble del espectro debido a su simetría. Este principio es fundamental en la transmisión de señales moduladas y en el diseño de sistemas de comunicación eficientes.
   - El SNR es un indicador clave en la transmisión de señales, ya que determina la claridad con la que una señal puede ser detectada y procesada en presencia de ruido.
   - La potencia de la señal tiene una relación directa con la calidad de la comunicación, ya que una mayor potencia generalmente mejora la SNR y reduce la interferencia del ruido. No obstante, el incremento de potencia debe gestionarse de manera eficiente, considerando restricciones regulatorias, consumo energético y la optimización del ancho de banda

### Referencias

- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)

- Rohde & Schwarz GmbH & Co. KG. (2017). R&S®FPC1000 Spectrum Analyzer User Manual (Firmware versión 1.10 y posteriores). Múnich, Alemania: Rohde & Schwarz.

- National Instruments. (2025). USRP-2920 Specifications. National Instruments.

- Rohde & Schwarz GmbH & Co. KG. (2017). R&S RTB2000 Digital Oscilloscope User Manual. Rohde & Schwarz.

---