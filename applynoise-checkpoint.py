import os
import numpy as np
from skimage import io, util
from PIL import Image

# Caminhos de entrada e saída
base_input_dir = r"C:\Users\otavi\OneDrive\Área de Trabalho\Projeto em IBM I\imagens_png"
base_output_dir = r"C:\Users\otavi\OneDrive\Área de Trabalho\Projeto em IBM I\dataset_reduzido"

# Modalidades
modalidades = ['abdomen', 'chest', 'derma']

noise_types = {
    'gauss': [0.001, 0.01],  # baixo, alto
    'poisson': ['low', 'high'],  # baixo, alto
    's&p': [0.002, 0.01]  # baixo, alto
}

def apply_gaussian_noise(image, var):
    return util.random_noise(image, mode='gaussian', var=var)

def apply_poisson_noise(image, mode):
    if mode == 'low':
        return util.random_noise(image, mode='poisson')
    else:
        scaled = (image * 255).astype(np.uint8)
        noisy = util.random_noise(scaled, mode='poisson')
        return noisy / noisy.max()

def apply_salt_pepper_noise(image, amount):
    return util.random_noise(image, mode='s&p', amount=amount)

def save_image(img_array, save_path):
    img_uint8 = (img_array * 255).astype(np.uint8)
    Image.fromarray(img_uint8).save(save_path)

# Geração do dataset
for modalidade in modalidades:
    input_dir = os.path.join(base_input_dir, modalidade)
    output_base = os.path.join(base_output_dir, modalidade)

    os.makedirs(os.path.join(output_base, "sem_ruido"), exist_ok=True)

    arquivos = sorted([f for f in os.listdir(input_dir) if f.lower().endswith('.png')])[:100]

    print(f"Processando {modalidade}... ({len(arquivos)} imagens)")

    for nome in arquivos:
        caminho_imagem = os.path.join(input_dir, nome)
        image = io.imread(caminho_imagem) / 255.0  # Normalizar

        # Salvar imagem original
        save_path = os.path.join(output_base, "sem_ruido", nome)
        save_image(image, save_path)

        # Aplicar ruídos
        for noise_type, intensities in noise_types.items():
            for intensity in intensities:
                if noise_type == 'gauss':
                    noisy = apply_gaussian_noise(image, var=intensity)
                    pasta = f"gauss_{int(intensity*100)}"
                elif noise_type == 'poisson':
                    noisy = apply_poisson_noise(image, mode=intensity)
                    pasta = f"poisson_{intensity}"
                elif noise_type == 's&p':
                    noisy = apply_salt_pepper_noise(image, amount=intensity)
                    pasta = f"sp_{int(intensity*100)}"

                save_dir = os.path.join(output_base, pasta)
                os.makedirs(save_dir, exist_ok=True)
                save_image(noisy, os.path.join(save_dir, nome))

print("✅ Dataset reduzido com ruídos gerado com sucesso!")
