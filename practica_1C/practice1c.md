
# Práctica 1C. Mediciones de potencia y frecuencia

## **Objetivo General**
Familiarizarse con el uso de herramientas de software definido por radio (SDR) como GNU Radio, junto con equipos de medición como el USRP 2920, el osciloscopio R&S RTB2004 y el analizador de espectros R&S FPC1000. Los estudiantes aprenderán a medir y analizar parámetros clave en comunicaciones, como potencia, ancho de banda, relación señal a ruido (SNR) y piso de ruido.

---

## **Materiales y Equipos**
- **USRP 2920**: Radio definido por software.
- **Osciloscopio R&S RTB2004**: Para visualización de señales en el dominio del tiempo y frecuencia.
- **Analizador de Espectros R&S FPC1000**: Para mediciones en el dominio de la frecuencia.
- **Computador con GNU Radio**: Para simulación y generación de señales usando el USRP 2920.
- **Cables y conectores**: Para interconexión de equipos.

---

## **Actividad 1: Revisión de Especificaciones de los Equipos**

### **Objetivo**
Familiarizarse con las especificaciones técnicas de los equipos de laboratorio y entender cómo configurarlos para realizar mediciones.

### **Procedimiento**
1. **Revisar Manuales y Verificar Equipos**:
   - Revisar las especificaciones de los equipos de laboratorio (USRP 2920, Osciloscopio R&S RTB2004 y Analizador de Espectros R&S FPC1000).
   - Identificar las principales funciones y controles de los equipos.

2. **Seleccionar Especificaciones Relevantes**:
   - Seleccionar las **5 especificaciones** que consideren **más relevantes** de cada equipo. 

3. **Configuración de los Equipos**:
   - **USRP 2920**: Identificar el rango de frecuencia y ganancia configurable mediante el comando `uhd_usrp_probe`.
   - **Osciloscopio R&S RTB2004**: Identificar el ancho de banda máximo, resolución vertical y tipos de mediciones soportadas.
   - **Analizador de Espectros R&S FPC1000**: Identificar el rango de frecuencia, resolución y figura de ruido.
   - 
### **Preguntas Orientadoras**
1. ¿Cuál es el rango de frecuencia del USRP 2920 y cómo se compara con el del analizador de espectros?
2. ¿Qué parámetros del USRP 2920 se deben configurar para transmitir una señal en una frecuencia específica?
3. ¿Cómo se configura el osciloscopio para medir la amplitud y la frecuencia de una señal?
4. ¿Qué diferencia hay entre medir una señal en el dominio del tiempo (osciloscopio) y en el dominio de la frecuencia (analizador de espectros)?
5. ¿Cómo se mide el piso de ruido en el analizador de espectros?

### **Evidencia**
- Lista con las 5 especificaciones más relevantes de cada equipo.

---

## **Actividad 2: Simulación de Señales en GNU Radio**

### **Objetivo**
Generar y analizar señales en GNU Radio para entender cómo se comportan diferentes formas de onda en tiempo y frecuencia.

### **Procedimiento**
1. **Abrir GNU Radio**:
   - Abrir GNU Radio Companion (GRC) (`gnuradio-companion`).
   - Cargar el flujograma [`simple_flowgraph.grc`](https://github.com/omreyes/LabComUIS/blob/develop/guides/practice1/simple_flowgraph.grc).

2. **Configurar el Flujograma**:
   - Identificar los bloques principales: `Signal Source`, `Throttle`, `QT GUI Time Sink` y `QT GUI Frequency Sink`.
   - Cambiar la forma de onda en el bloque `Signal Source` (seno, coseno, cuadrada, triangular, etc.).
   - Ajustar la frecuencia y amplitud de la señal generada.
   - Modifique los parámetros del modelo de canal.

3. **Ejecutar el Flujograma**:
   - Ejecutar el flujograma y observar las señales generadas en las ventanas de tiempo (`Time Sink`) y frecuencia (`Frequency Sink`).

4. **Análisis de las Señales**:
   - Comparar las formas de onda en el dominio del tiempo y la frecuencia.
   - Anotar las diferencias entre las señales generadas con diferentes formas de onda.

### **Preguntas Orientadoras**
1. ¿Cómo afecta la forma de onda a la distribución de energía en el dominio de la frecuencia?
2. ¿Qué sucede con la señal en el dominio del tiempo si se aumenta la frecuencia en el bloque `Signal Source`?
3. ¿Cómo se relaciona la amplitud de la señal con la potencia observada en el dominio de la frecuencia?
4. ¿Qué diferencias se observan entre una señal senoidal y una señal cuadrada en el dominio de la frecuencia?
5. ¿Cómo se podría modificar el flujograma para generar una señal con ruido añadido?

### **Evidencia**
- Capturas de pantalla de las señales generadas en el dominio del tiempo y la frecuencia.

---

## **Actividad 3: Transmisión y Medición de Señales con el USRP 2920**

### **Objetivo**
Transmitir señales usando el USRP 2920 y medir parámetros clave como potencia, ancho de banda, piso de ruido y relación señal a ruido (SNR).

### **Procedimiento**
1. **Configurar el USRP 2920**:
   - Configurar el flujograma en GNU Radio para transmitir una señal a través del USRP (habilite y deshabilite los bloques correspondientes).
   - Ajustar la frecuencia y ganancia del USRP.
   - Varíe la frecuencia de portadora para evaluar la respuesta en frecuencia del canal.
   - Compare los resultados de transmitir usando un cable y usando antenas.

2. **Medición con el Analizador de Espectros**:
   - Conectar la salida del USRP al analizador de espectros R&S FPC1000.
   - Cambiar la forma de onda en el bloque `Signal Source` (seno, coseno, cuadrada, triangular, etc.).
   - Ajustar la frecuencia y amplitud de la señal generada.
   - Medir la potencia de la señal transmitida, el ancho de banda y el piso de ruido.
   - Determinar la máxima potencia de transmisión.
   - Varíe la frecuencia de portadora para evaluar la respuesta en frecuencia del canal.
   - Compare los resultados de transmitir usando un cable y usando antenas.

3. **Medición con el Osciloscopio**:
   - Conectar el osciloscopio R&S RTB2004 al USRP.
   - Visualizar la señal en el dominio del tiempo.
   - Medir la amplitud y el tiempo de subida de la señal cuadrada.
   - Mida la potencia de las señales transmitidas y contrástela con la medición obtenida con el analizador de espectros.

4. **Cálculo de la Relación Señal a Ruido (SNR)**:
   - Usar las mediciones de potencia y piso de ruido para calcular la SNR de algunas de las señales generadas.
   - Anotar el valor de la SNR en dB.

### **Preguntas Orientadoras**
1. ¿Cómo se configura el USRP 2920 para transmitir una señal en una frecuencia específica?
2. ¿Qué parámetros del flujograma afectan la potencia de la señal transmitida?
3. ¿Cómo se mide el ancho de banda de la señal transmitida en el analizador de espectros?
4. ¿Cómo se calcula la relación señal a ruido (SNR) a partir de las mediciones de potencia y piso de ruido?
5. ¿Qué diferencias se observan en las mediciones de potencia cuando se varía la ganancia del USRP?

### **Evidencia**
- Capturas de pantalla de las mediciones realizadas en el analizador de espectros y el osciloscopio.

---

## **Actividad 4: Análisis de Resultados y Conclusiones**

### **Objetivo**
Analizar los resultados obtenidos y sacar conclusiones sobre el comportamiento de las señales en diferentes condiciones para elaborar el informe.

### **Para la Elaboración del Informe**
1. **Comparar Resultados**:
   - Comparar los resultados obtenidos en las simulaciones y las transmisiones reales.
   - Discutir las diferencias entre las mediciones realizadas con el osciloscopio y el analizador de espectros.

2. **Reflexionar sobre la SNR**:
   - Analizar la importancia de la relación señal a ruido (SNR) en las comunicaciones inalámbricas.
   - Discutir cómo el piso de ruido afecta la capacidad de detectar señales débiles.

3. **Conclusiones Finales**:
   - Escribir conclusiones basadas en los resultados obtenidos.
   - Reflexionar sobre las limitaciones de los equipos y cómo se podrían mejorar las mediciones.

### **Preguntas Orientadoras**
1. ¿Qué conclusiones se pueden obtener sobre la relación entre la potencia de la señal y la calidad de la comunicación?
2. ¿Cómo afecta el piso de ruido a la capacidad de detectar señales débiles?
3. ¿Qué limitaciones tienen los equipos utilizados en términos de ancho de banda y precisión en las mediciones?
4. ¿Cómo se pueden mejorar las mediciones de señal en un entorno con alto nivel de ruido?
5. ¿Qué aplicaciones prácticas tienen las mediciones de potencia y ancho de banda en sistemas de comunicaciones reales?
6. ¿Cómo se puede medir la respuesta en frecuencia de un canal alámbrico?
7. ¿Cómo se puede obtener un modelo sencillo de las pérdidas (_pathloss_) en un canal inalámbrico?
