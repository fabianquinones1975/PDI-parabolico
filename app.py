import subprocess
import os

def ejecutar_preprocesamiento():
    print("=== INICIANDO PREPROCESAMIENTO ===")

    print("[1] Convirtiendo video a escala de grises...")
    subprocess.run(["python3", "preprocesamiento/abrirvideo.py"])

    print("[2] Detectando bordes y contornos...")
    subprocess.run(["python3", "preprocesamiento/contornos.py"])

    print("=== PREPROCESAMIENTO FINALIZADO ===")


def ejecutar_procesamiento():
    print("=== INICIANDO PROCESAMIENTO ===")
    try:
        from procesamiento.regresion import ajustar_parabola
        coef = ajustar_parabola()
        print(f"[OK] Regresión completada: a={coef[0]:.4f}, b={coef[1]:.4f}, c={coef[2]:.4f}")
    except Exception as e:
        print("[ERROR] No se pudo realizar la regresión:", e)
    print("=== PROCESAMIENTO FINALIZADO ===")


if __name__ == "__main__":
    ejecutar_preprocesamiento()
    ejecutar_procesamiento()
