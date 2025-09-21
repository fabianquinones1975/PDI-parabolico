import cv2

#1. Abre el archivo de video
cap = cv2.VideoCapture('../user_files/tiro.mp4') # Reemplaza 'tu_video.mp4' con la ruta de tu video

# 2. Obtén el archivo de video para escribir la salida
#    (asegúrate de que el códec sea compatible)
#    Define el FourCC (códec de video)
#    Para MP4, se puede usar 'mp4v' o 'XVID'
#    writer = cv2.VideoWriter('video_gris.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
#    Si no tienes la resolución, usa cap.get() para obtenerla
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('video_gris.mp4', cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS), (width, height), isColor=False)


# 3. Itera sobre los fotogramas del video
while True:
    # Lee un fotograma
    ret, frame = cap.read()

    # Si no hay fotograma (fin del video), sale del bucle
    if not ret:
        break

    # 4. Convierte el fotograma a escala de grises
    #    OpenCV lee los videos en formato BGR por defecto
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Escribe el fotograma en escala de grises
    writer.write(gray_frame)

    # (Opcional) Muestra el fotograma en escala de grises
    cv2.imshow('Video en Escala de Grises', gray_frame)

    # 6. Espera a que se presione 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 7. Libera los recursos
cap.release()
writer.release() # Cierra el archivo de video de salida
cv2.destroyAllWindows() 
