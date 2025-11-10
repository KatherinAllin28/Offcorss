import argparse, pickle, numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

def synth_texture(n=64):
    base = rng.normal(0, 1, (n, n))
    base = np.cumsum(np.cumsum(base, axis=0), axis=1)
    base = (base - base.min()) / (base.max() - base.min())
    return base

def add_defect(img, kind="line"):
    img = img.copy()
    n = img.shape[0]
    if kind == "line":
        r = rng.integers(5, n-5); t = rng.integers(1, 3); img[r:r+t, :] = 1.0
    elif kind == "spot":
        r, c = rng.integers(8, n-8, size=2)
        rr, cc = np.ogrid[:n, :n]
        mask = (rr-r)**2 + (cc-c)**2 <= rng.integers(9, 25)
        img[mask] = 1.0
    elif kind == "stain":
        r, c = rng.integers(10, n-10, size=2); h, w = rng.integers(5, 12, size=2)
        img[r:r+h, c:c+w] = 0.0
    return img


def extract_simple_features(img):
    g = img
    mean = g.mean()
    std = g.std()
    # Gradientes con la misma forma
    gx = np.gradient(g, axis=1)
    gy = np.gradient(g, axis=0)
    grad = (gx**2 + gy**2) ** 0.5
    g_mean = grad.mean()
    g_std = grad.std()
    # Importante: devolvemos SOLO 4 features (sin 'high')
    return np.array([mean, std, g_mean, g_std])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=64)
    ap.add_argument("--samples", type=int, default=4)
    args = ap.parse_args()

    model_path = Path(__file__).parent / "reto1_model.pkl"
    if not model_path.exists():
        print("No se encontró reto1_model.pkl en la carpeta actual.")
        return
    clf = pickle.loads(model_path.read_bytes())

    print("Generando muestras sintéticas y evaluando...")
    for i in range(args.samples):
        img = synth_texture(args.n)
        if i % 2 == 1:
            img = add_defect(img)
        x = extract_simple_features(img).reshape(1, -1)
        pred = clf.predict(x)[0]
        print(f"Muestra {i+1}: {'DEFECTO' if pred==1 else 'OK'}")

if __name__ == "__main__":
    main()
