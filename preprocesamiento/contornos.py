import cv2
import numpy as np

input_video = "user_files/tiro.mp4"   # usa tu video original a color
output_video = "preprocesamiento/video_balon_tracking.mp4"

cap = cv2.VideoCapture(input_video)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height), isColor=True)

# --- Rango de color naranja/rojizo en HSV ---
lower_orange = np.array([0, 100, 80])
upper_orange = np.array([30, 255, 255])

# Tracker (se creará solo cuando se detecte el balón)
tracker = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = frame.copy()

    if tracker is None:
        # ===== DETECCIÓN POR COLOR =====
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_blur = cv2.GaussianBlur(hsv, (5, 5), 0)
        mask = cv2.inRange(hsv_blur, lower_orange, upper_orange)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

        contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if 200 < area < 8000:  # rango de tamaño del balón
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                circle_area = 3.14 * (radius ** 2)
                if circle_area == 0:
                    continue
                circularidad = area / circle_area

                if 0.7 < circularidad < 1.3:  # casi circular
                    x, y, w, h = cv2.boundingRect(cnt)

                    # Inicializar tracker
                    tracker = cv2.TrackerCSRT_create()
                    tracker.init(frame, (x, y, w, h))

                    cv2.putText(output, "TRACKING INICIADO", (30, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                    break
    else:
        # ===== TRACKING =====
        success, box = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(output, "BALON", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            # Tracker falló → reiniciamos
            tracker = None
            cv2.putText(output, "BUSCANDO BALON...", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    writer.write(output)
    cv2.imshow("Deteccion + Tracking", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
