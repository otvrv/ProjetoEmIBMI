import numpy as np
import os
from PIL import Image

# Caminho base dos arquivos .npz
base_path = r"C:\Users\otavi\.medmnist"

# Nomes dos arquivos
datasets = {
    "chest": "pneumoniamnist_128.npz",
    "abdomen": "organcmnist_128.npz",
    "derma": "dermamnist_128.npz"
}

# Pasta de saída
output_dir = "imagens_png"
num_samples = 250

os.makedirs(output_dir, exist_ok=True)

for nome, arquivo in datasets.items():
    print(f"Processando {nome}...")

    # Caminho completo do .npz
    arquivo_npz = os.path.join(base_path, arquivo)

    # Criar pasta do dataset
    dataset_dir = os.path.join(output_dir, nome)
    os.makedirs(dataset_dir, exist_ok=True)

    # Carregar os dados
    data = np.load(arquivo_npz)

    # Selecionar amostras do split 'val'
    imagens = data["val_images"][:num_samples]

    for i, img in enumerate(imagens):
        # Converter para grayscale se tiver 3 canais
        if img.ndim == 3 and img.shape[2] == 3:
            img = np.mean(img, axis=2)

        # Escalar para 0–255 se estiver normalizado
        if img.max() <= 1.0:
            img = (img * 255).astype(np.uint8)

        # Converter para imagem PIL e salvar como PNG (modo L = 8-bit grayscale)
        img_pil = Image.fromarray(img).convert("L")
        img_pil.save(os.path.join(dataset_dir, f"{nome}_{i:03d}.png"))

print("Conversão finalizada com sucesso.")