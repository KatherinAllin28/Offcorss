# -*- coding: utf-8 -*-
import numpy as np
import argparse
import pickle
import os
from PIL import Image
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


def generar_imagen_sintetica(tamaño=(128, 128), tipo="OK"):
    """
    Genera una imagen sintética simple:
    - OK: textura uniforme
    - DEFECTO: textura con 'mancha' o ruido local
    """
    img = np.random.normal(128, 10, tamaño).astype(np.uint8)
    if tipo == "DEFECTO":
        # Crear defecto tipo mancha circular
        x, y = np.random.randint(30, 98), np.random.randint(30, 98)
        radio = np.random.randint(5, 15)
        yy, xx = np.ogrid[:tamaño[0], :tamaño[1]]
        mask = (xx - x) ** 2 + (yy - y) ** 2 <= radio ** 2
        img[mask] = np.random.randint(50, 80)
    return img


def extraer_caracteristicas(img):
    """Extrae 4 características simples (media, std, gradiente medio y std)."""
    img = img.astype(np.float32) / 255.0
    mean = img.mean()
    std = img.std()
    gx, gy = np.gradient(img)
    grad = np.sqrt(gx ** 2 + gy ** 2)
    gmean = grad.mean()
    gstd = grad.std()
    return np.array([mean, std, gmean, gstd], dtype=np.float32)


def main():
    parser = argparse.ArgumentParser(description="Demo Reto 1 con imágenes guardadas (solo valor real).")
    parser.add_argument("--samples", type=int, default=40, help="Número de muestras sintéticas (por defecto: 40).")
    parser.add_argument("--model", default="reto1_model.pkl", help="Ruta al modelo .pkl.")
    parser.add_argument("--out_dir", default="imagenes_generadas", help="Carpeta donde guardar las imágenes generadas.")
    parser.add_argument("--csv_out", default="resultados_reto1.csv", help="Archivo CSV con los resultados.")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    # Cargar modelo (aunque no lo usemos para mostrar predicción, se mantiene por compatibilidad)
    with open(args.model, "rb") as f:
        clf = pickle.load(f)
    print(f"Cargando modelo: {args.model}\nGenerando {args.samples} muestras sintéticas...")

    resultados = []

    for i in range(args.samples):
        tipo_real = np.random.choice(["OK", "DEFECTO"])
        img = generar_imagen_sintetica(tipo=tipo_real)

        # Guardar imagen (solo etiqueta real)
        filename = f"muestra_{i+1:03d}_{tipo_real}.png"
        path = os.path.join(args.out_dir, filename)
        Image.fromarray(img).save(path)

        resultados.append({
            "muestra": i + 1,
            "real": tipo_real,
            "archivo": filename
        })

        if i < 10:
            print(f"[{i+1:03d}] real={tipo_real}")
        elif i == 10:
            print("...")

    # Guardar CSV
    df = pd.DataFrame(resultados)
    df.to_csv(args.csv_out, index=False, encoding="utf-8-sig")

    print(f"\nTotal muestras: {args.samples}")
    print(f"Imágenes guardadas en: {os.path.abspath(args.out_dir)}")
    print(f"CSV con resultados: {os.path.abspath(args.csv_out)}")


if __name__ == "__main__":
    main()

