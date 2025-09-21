import numpy as np
import matplotlib.pyplot as plt
import csv
import os

def ajustar_parabola(csv_path="user_files/trayectoria.csv", mostrar_grafica=True):
    if not os.path.exists(csv_path):
        print(f"Archivo CSV no encontrado: {csv_path}")
        return

    # Leer datos del CSV
    frames, x_vals, y_vals = [], [], []
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            frames.append(int(row["frame"]))
            x_vals.append(int(row["x"]))
            y_vals.append(int(row["y"]))

    x = np.array(x_vals)
    y = np.array(y_vals)

    # Ajustar regresión cuadrática: y = ax^2 + bx + c
    coeficientes = np.polyfit(x, y, 2)
    a, b, c = coeficientes
    print(f"Coeficientes de la parábola ajustada: a={a:.4f}, b={b:.4f}, c={c:.4f}")

    # Crear valores de Y ajustados
    y_ajustada = a * x**2 + b * x + c

    if mostrar_grafica:
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, label='Trayectoria real', color='blue')
        plt.plot(x, y_ajustada, label='Regresión parabólica', color='red')
        plt.gca().invert_yaxis()  # Invertir eje Y porque en imágenes el 0 está arriba
        plt.title("Regresión Parabólica del Movimiento del Balón")
        plt.xlabel("X (pixeles)")
        plt.ylabel("Y (pixeles)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("user_files/regresion_parabolica.png")
        plt.show()

    return coeficientes
