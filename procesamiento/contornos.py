import cv2
import os

# Archivo de entrada (ya generado en escala de grises)
input_video = "preprocesamiento/video_gris.mp4"
output_video = "preprocesamiento/video_contornos.mp4"

cap = cv2.VideoCapture(input_video)

# Resolución y fps del video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# VideoWriter para guardar la salida
writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height), isColor=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. El video ya está en gris, pero aseguramos:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Umbralización
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # 3. Detección de bordes con Canny
    edges = cv2.Canny(thresh, 50, 150)

    # 4. Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 5. Dibujar los contornos sobre el frame original (en color para visualización)
    contoured_frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contoured_frame, contours, -1, (0, 255, 0), 2)

    # Guardar
    writer.write(contoured_frame)

    # Mostrar en ventana
    cv2.imshow("Contornos", contoured_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
