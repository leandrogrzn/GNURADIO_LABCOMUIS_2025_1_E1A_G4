# Laboratorio de Comunicaciones
## Universidad Industrial de Santander

---
# Práctica 2. Modelo de canal

### Integrantes
- **Leandro José Garzón Nieto** - 2194232
- **David Josué Díaz Ortiz** - 2204269

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
28 de marzo de 2025

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento. 

Se utilizó ChatGPT para la corrección ortográfica, gramatical y de puntuación del texto, asegurando claridad y coherencia. No obstante, el contenido técnico y la interpretación de los resultados fueron desarrollados íntegramente por los autores.

---
## Contenido

### Resumen
La práctica tuvo como objetivo analizar el impacto del canal en la transmisión de señales, evaluando la relación señal-ruido y la eficiencia de transmisión mediante simulaciones en GNU Radio y experimentación con el uso de herramientas como osciloscopio y el analizador de espectros. Se estudiaron los efectos del ruido, la atenuación y la desviación de frecuencia, así como métodos de mitigación mediante filtrado y ajustes en la transmisión. Se compararon los resultados de simulación con mediciones reales en el dominio del tiempo y la frecuencia, considerando variaciones en la distancia de transmisión y el medio utilizado (cables coaxiales o aire). Los experimentos permitieron visualizar de forma práctica los fenómenos de canal y su influencia en la calidad de la señal, fortaleciendo conocimientos teóricos y habilidades en el manejo de equipos especializados.


**Palabras clave:** ruido, filtrado, señal-ruido, atenuación, frecuencia. 

### Introducción
La transmisión de señales a través de un canal está sujeta a diversos fenómenos que pueden degradar su calidad, afectando la confiabilidad con la que la información es recibida. Factores como el ruido, la atenuación, la interferencia y la desviación de frecuencia introducen distorsiones que alteran la relación señal-ruido y pueden comprometer la integridad de la comunicación. Comprender estos efectos es fundamental para diseñar estrategias que permitan mitigar su impacto, optimizando la transmisión de datos en sistemas reales. Esta práctica abordó el estudio de estos fenómenos a través de simulaciones en GNU Radio y experimentación con equipos de medición avanzados como el USRP 2920, el osciloscopio y el analizador de espectros. Se evaluaron los efectos del filtrado en la señal, la influencia del ruido en el dominio del tiempo y la frecuencia, y el impacto de la distancia en la transmisión alámbrica e inalámbrica. A partir de estos análisis, se buscó responder preguntas clave, tales como: ¿cómo afecta el filtrado a las frecuencias de una señal?, ¿cómo se manifiesta la degradación de la señal en presencia de ruido?, ¿qué impacto tiene la variación de la frecuencia de portadora en la transmisión?, y ¿qué técnicas pueden emplearse para mejorar la calidad de la señal recibida?. El desarrollo de estas actividades permitió no solo verificar la teoría mediante la observación experimental, sino también fortalecer habilidades en el manejo de instrumentación. De esta manera, se adquirió un conocimiento más certero sobre la influencia del canal en la transmisión de señales y las estrategias empleadas para contrarrestar sus efectos en distintos escenarios de comunicación.

### Procedimiento

Para llevar a cabo esta práctica, se realizaron cuatro actividades principales: simulación de canal en GNU Radio, Fenómenos de canal en el osciloscopio, Fenómenos de canal en el analizador de espectro y Efectos de los fenómenos de canal en la conversión de frecuencia. A continuación, se detallan los pasos a seguir en cada actividad:

## Actividad 1: Actividades de simulación de canal en GNU Radio

Se realizaron simulaciones para analizar el impacto del ruido, la atenuación y el filtrado en la transmisión de señales. Se estudió cómo la relación señal-ruido (SNR) afecta la calidad de la señal y cómo el filtrado puede mejorar su recepción.

- **Se generan diferentes señales y se observa el efecto de variar las frecuencias de corte del filtro**

| <img src="./capturas_1/capturas/tiempo_cuadrada_LCF_1000_HCF_8000.png" alt="cuadrada_tiempo_filtro" width="300" height="150"> | <img src="./capturas_1/capturas/frecuencia_cuadrada_LCF_1000_HCF_8000.png" alt="cuadrada_frecuencia_filtro" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Cuadrada en tiempo con filtro** | **Cuadrada en frecuencia con filtro** |

| <img src="./capturas_1/capturas/tiempo_triangulo_LCF_10_HCF_4000.png" alt="triangulo_tiempo_filtro" width="300" height="150"> | <img src="./capturas_1/capturas/frecuencia_triangulo_LCF_10_HCF_4000.png" alt="triangulo_frecuencia_filtro" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Triangular en tiempo con filtro** | **Triangular en frecuencia con filtro** |

Como se observa en las imágenes, la señal cuadrada generada por GNU Radio, al pasar por el proceso de filtrado, se transforma en una señal sinusoidal. Este fenómeno se explica a través de la descomposición en series de Fourier, donde una señal cuadrada puede representarse como la suma de múltiples componentes senoidales con frecuencias que son múltiplos de la frecuencia fundamental. Al aplicar el filtro, se atenúan o eliminan ciertas bandas de frecuencia, lo que provoca la anulación de los armónicos de orden superior o inferior según la configuración del filtro. Como resultado, la señal filtrada conserva únicamente las componentes de frecuencia permitidas, generando una salida predominantemente sinusoidal. así mismo para la señal triangular.

- **Se analiza el efecto del ruido en el dominio del tiempo y la frecuencia para al menos dos formas de onda distintas**

Una manera de analizar el efecto del ruido teoricamente es la relacion señal a ruido(SNR), la cual se expresa como: 

$$
\text{SNR} = \frac{P_s}{P_n}
$$

Donde:  
- $P_{s}$, es la potencia de la señal.  
- $P_{n}$, es la potencia del ruido.  

En decibeles (*dB*), se calcula como:  

$$
\text{SNR}{dB} = 10 \log_{10} \left( \frac{P_s}{P_n} \right)
$$

#### Señales generadas por GNU radio

| <img src="./capturas_1/capturas/cuadrada_con_ruido_tiempo.png" alt="cuadrada_tiempo_filtro" width="300" height="150"> | <img src="./capturas_1/capturas/cuadrada_ruido_frecuencia.png" alt="cuadrada_frecuencia_filtro" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Cuadrada en tiempo con ruido** | **Cuadrada en frecuencia con ruido** |

| <img src="./capturas_1/capturas/triangulo_ruido_tiempo.png" alt="cuadrada_tiempo_filtro" width="300" height="150"> | <img src="./capturas_1/capturas/triangulo_ruido_frecuencia.png" alt="cuadrada_frecuencia_filtro" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Triangulo en tiempo con ruido** | **Triangulo en frecuencia con ruido** |

Como observamos en las imágenes el ruido afecta tanto la representación temporal como espectral de las señales, alterando su forma y agregando componentes no deseadas en el espectro de frecuencia. Esto puede dificultar la correcta interpretación de la señal y su posterior procesamiento, haciendo necesario el uso de técnicas de filtrado para mejorar su calidad.

## Actividad 2: Fenómenos de canal en el osciloscopio

Se utilizó un osciloscopio para medir y visualizar las señales en el tiempo, identificando efectos como la atenuación y la desviación de frecuencia. Esto permitió comparar las señales transmitidas y recibidas para evaluar la frecuencia en los rangos establecidos (50MHz hasta 500MHz) de la actividad.

### **Variacion de la frecuencia portadora**


## *Ecuación de la señal modulada en amplitud*  

Cuando modulamos una señal en amplitud (AM), la forma matemática general es:

$$
s(t) = A_{c} [1 + m(t)] \cos(2\pi f_{c} t)
$$

donde:  
- $A_{c}$, es la amplitud de la portadora.
- $f_{c}$, es la frecuencia de la portadora.  
- $m(t)$, es la señal moduladora.
- $cos(2\pi f_{c} t)$, es la señal portadora.

| <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 6.56.13 PM.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 6.57.07 PM.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 6.58.03 PM.jpeg" alt="cos_float" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Señal cuadrada con portadora 50MHz** | **Señal cuadrada con portadora 100MHz** | **Señal cuadrada con portadora 500MHz** |

| <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 7.02.36 PM.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 7.02.01 PM.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 6.59.17 PM.jpeg" alt="cos_float" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Señal triangular con portadora 50MHz** | **Señal triangular con portadora 100MHz** | **Señal triangular con portadora 500MHz** |


| <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 7.04.52 PM.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/WhatsApp Image 2025-03-12 at 7.05.49 PM.jpeg" alt="cos_float" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Señal triangular con ruido con portadora 50MHz** | **Señal cuadrada con ruido con portadora 300MHz** |

Las imágenes capturadas en el osciloscopio muestran señales moduladas en amplitud con diferentes frecuencias portadoras: 50 MHz, 100 MHz y 500 MHz. Se observa que, a medida que la frecuencia portadora aumenta, la densidad de oscilaciones dentro de cada pulso también incrementa. En la señal de 50 MHz, la envolvente se percibe de manera clara, con oscilaciones internas bien definidas y relativamente estables. Al aumentar la frecuencia a 100 MHz, se notan más oscilaciones dentro de los pulsos, manteniendo aún una envolvente reconocible. Finalmente, en la señal de 500 MHz, la cantidad de oscilaciones es considerablemente mayor, y pueden notarse posibles efectos de aliasing o atenuación, dependiendo del ancho de banda del osciloscopio utilizado.

## Actividad 3: Fenómenos de canal en el analizador de espectro

Se empleó un analizador de espectros para observar la respuesta en frecuencia de las señales y se estudiaron los efectos del canal en la distribución espectral.

Para calcular el espectro de una señal podemos utilizar herramientas como lo es la transformada de fourier la cual nos permite descomponer la señal en sus comoponentes en frecuencia.




### 1. Transformada de Fourier de Tiempo Continuo

Si tienes una señal en el dominio del tiempo \( x(t) \), su espectro \( X(f) \) se obtiene con la *Transformada de Fourier* definida como:

$$
X(f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi f t} dt
$$

Esto te da el espectro de frecuencia, indicando las componentes de frecuencia de la señal.

#### Señal Senoidal

Si $ x(t) = A \cos(2\pi f_0 t) $, su *Transformada de Fourier* es:

$$
X(f) = \frac{A}{2} \left[ \delta(f - f_0) + \delta(f + f_0) \right]
$$

Lo que significa que la señal tiene picos en $ f_0 $ y  $ -f_0 $. Este caso seria el mismo análisis para una señal cuadratica y triangular, solo que esta va a ser una serie de sumatorias en el dominio de la frecuencia con una amplitud dependiente de la forma de la señal. 

| <img src="./capturas_2_3/capturas/seno_1KHz_100MHz.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/cuadrada_1KHz_100MHz.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/triangular_1KHz_300MHz.jpeg" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_3/capturas/triangular_ruido_1.jpg" alt="cos_float" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|:-----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Seno frecuencia 1KHz portadora 100MHz** | **Cuadrada frecuancia 1KHz portadora 100MHz** | **Triangular freuancia 1KHz portadora 300MHz** | **Triangular con ruido** |

Teniendo en cuenta las distintas formas de onda visualizadas en el analizador de espectro, se observa que los espectros de frecuencia obtenidos presentan una correspondencia con los patrones teóricos esperados para cada tipo de señal. La distribución de los componentes espectrales y la presencia de armónicos concuerdan con el análisis teórico de Fourier, donde cada forma de onda se descompone en una serie de frecuencias fundamentales y sus armónicos correspondientes. Ademas, El efecto del ruido sobre la respuesta en frecuencia de las señales medidas en el analizador de espectro se evidencia en un incremento del nivel de fondo en todo el espectro, lo que introduce una mayor densidad espectral fuera de las frecuencias principales y genera una reducción en la claridad de los armónicos dominantes. En la imagen correspondiente a la señal con ruido, se observa cómo la forma espectral esperada de la onda triangular sigue presente, pero con una mayor dispersión de energía en frecuencias no deseadas y reduccion de espectros.


## Actividad 4: Efectos de los fenómenos de canal en la conversión de frecuencia

Se examinó cómo la conversión de frecuencia influye en la transmisión, tanto en sistemas cableados como inalámbricos. Se evaluó el impacto de la variación de frecuencia y la distancia en la calidad de la señal recibida.


| <img src="./capturas_2_4/captura2_4bcc.png" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_4/captura2_4cc.png" alt="cos_float" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Señal Triangular cable corto** | **Señal Cuadrada cable corto** |

| <img src="./capturas_2_4/captura2_4ccl.png" alt="cos_float" width="300" height="150"> | <img src="./capturas_2_4/captura2_4cl.png" alt="cos_float" width="300" height="150"> |
|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| **Señal Triangular cable largo** | **Señal Cuadrada cable largo** |

Como se observa en las imagenes se presenta cuatro escenarios en los que se analizan señales triangulares y cuadradas transmitidas a través de cables de diferente longitud: un cable corto de aproximadamente 1.10 metros y un cable largo de aproximadamente 37 metros. A partir de la comparación de estas señales en el dominio del tiempo y su espectro de frecuencia, el uso de un cable largo introduce atenuación, distorsión y retardo en la señal. Mientras que la señal triangular mantiene mejor su forma, la señal cuadrada es más susceptible a la pérdida de armónicos y presenta oscilaciones en los flancos. En aplicaciones prácticas, estos efectos deben ser considerados para minimizar la degradación de la señal, por ejemplo, mediante el uso de cables de menor longitud, amplificadores de señal o técnicas de compensación de pérdidas.



### Conclusiones
- El espectro de las señales analizadas muestra que el ruido introducido en el sistema modifica la distribución de frecuencias, generando un ensanchamiento del espectro y una disminución en la nitidez de los armónicos. La señal cuadrada, al depender de múltiples armónicos de alta frecuencia, experimenta una mayor distorsión en comparación con la señal triangular, que conserva mejor su estructura fundamental. Esto confirma que el ruido y la impedancia del medio influyen directamente en la calidad espectral de la señal.

- Los resultados obtenidos resaltan la importancia de seleccionar adecuadamente la longitud del cable en función de la aplicación. Ya que las señales transmitidas a través del cable largo presentan una disminución en amplitud y una mayor afectación en la transmisión de armónicos, lo que provoca una pérdida en la fidelidad de la señal original, en comparacion con el cable corto.



### Referencias


- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)

- Rohde & Schwarz GmbH & Co. KG. (2017). R&S®FPC1000 Spectrum Analyzer User Manual (Firmware versión 1.10 y posteriores). Múnich, Alemania: Rohde & Schwarz.

- National Instruments. (2025). USRP-2920 Specifications. National Instruments.

- Rohde & Schwarz GmbH & Co. KG. (2017). R&S RTB2000 Digital Oscilloscope User Manual. Rohde & Schwarz.

---
