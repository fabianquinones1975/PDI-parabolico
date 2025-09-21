import subprocess
import os

def ejecutar_preprocesamiento():
    print("=== INICIANDO PREPROCESAMIENTO ===")

    # 1. Convertir a escala de grises
    print("[1] Convirtiendo video a escala de grises...")
    subprocess.run(["python3", "preprocesamiento/abrirvideo.py"])

    # 2. Detectar contornos
    print("[2] Detectando bordes y contornos...")
    subprocess.run(["python3", "preprocesamiento/contornos.py"])

    print("=== PREPROCESAMIENTO FINALIZADO ===")

if __name__ == "__main__":
    ejecutar_preprocesamiento()
