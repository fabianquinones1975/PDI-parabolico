# Análisis del Movimiento de un Tiro Parabólico 📹📈

**Universidad de Antioquia**  
Facultad de Ingeniería  
Departamento de Ingeniería de Sistemas, Telecomunicaciones y Electrónica  
Asignatura: Procesamiento Digital de Imágenes – 2025-2

**Fecha de entrega:** 22 de Septiembre de 2025  
**Autor:** Fabian  
**Proyecto:** Análisis del Movimiento de un Tiro Parabólico  

---

## 🎯 Objetivo

Este proyecto tiene como objetivo capturar y analizar el movimiento de un objeto en un tiro parabólico mediante técnicas de procesamiento digital de imágenes y visión por computador. Se busca:

- Detectar y seguir el objeto a lo largo del video.
- Calcular parámetros como posición, velocidad y aceleración.
- Comparar los resultados experimentales con las fórmulas teóricas del tiro parabólico.
- Visualizar los resultados superpuestos en el video original y en gráficas.

---

## 🗂️ Estructura del Proyecto

PDItarea1/
│

├── app.py # Script principal del proyecto

├── app/

│ ├── app.py # Punto de entrada o controlador de la app

│ ├── frontend/ # Archivos relacionados con la visualización (si aplica)

│ ├── preprocesamiento/

│ │ ├── abrirvideo.py # Lógica para cargar y leer el video

│ │ └── contornos.py # Detección de bordes, umbrales, centroides, etc. y genera el csv con las trazas

│ ├── procesamiento/ # Módulo para cálculos físicos y visualizaciones

│ │ └── regresion.py # hace la regresion

│ └── user_files/

│ └── tiro.mp4 # Video original del tiro parabólico

---

## 🧰 Librerías Usadas

Este proyecto utiliza las siguientes librerías de Python:

| Librería              | Propósito                                         |
|----------------------|---------------------------------------------------|
| `opencv-contrib-python` | Procesamiento de imágenes, detección de objetos |
| `numpy`              | Cálculos numéricos y manejo de vectores/matrices |
| `matplotlib`         | Visualización de resultados y gráficas           |

Instalación recomendada (desde pip):

```bash
pip install opencv-contrib-python numpy matplotlib
O usando apt en Ubuntu para una versión integrada:

sudo apt install python3-opencv

⚙️ Instrucciones de Uso

Coloca tu video en la carpeta app/user_files/ con el nombre tiro.mp4 (o ajusta el nombre en el código).

Ejecuta el archivo principal:

python3          app.py


El sistema:

Lee el video

Detecta el objeto en movimiento

Calcula y guarda los datos del análisis (posición, velocidad, aceleración)

Superpone los resultados y genera gráficas

plt.figure(figsize=(10, 6))  # crea una nueva figura de 10x6 pulgadas
plt.scatter(x, y, label='Trayectoria real', color='blue')  # dibuja puntos (trayectoria real)
plt.plot(x, y_ajustada, label='Regresión parabólica', color='red')  # dibuja línea de la regresión
plt.gca().invert_yaxis()  # invierte eje Y (0 arriba como en imágenes)
plt.title("Regresión Parabólica del Movimiento del Balón")  # título de la gráfica
plt.xlabel("X (pixeles)")  # etiqueta del eje X
plt.ylabel("Y (pixeles)")  # etiqueta del eje Y
plt.legend()  # muestra la leyenda (colores y etiquetas)
plt.grid(True)  # activa cuadrícula de fondo
plt.tight_layout()  # ajusta diseño para que nada se corte
plt.savefig("user_files/regresion_parabolica.png")  # guarda la imagen en esa ruta
plt.show()  # muestra la gráfica en una ventana emergente

📊 Resultados Esperados

Video con anotaciones que muestren la trayectoria, velocidad y aceleración.

Gráficas comparativas entre los valores experimentales y los teóricos.

Informe técnico con el análisis de los resultados (formato IEEE).




🧪 Estado Actual
Carga y lectura del video
convertir a escala de grises
deteccion de contornos
//falta///
Calculo de velocidad y acelracion
Comparacion con formulas teoricas 
Visualizacion final 

Referencias

Fisicalab: Movimiento Parabólico

Licencia

Uso académico. Proyecto desarrollado como parte del curso de Procesamiento Digital de Imágenes (2025-2).
