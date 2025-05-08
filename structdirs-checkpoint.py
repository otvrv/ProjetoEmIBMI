import os
import shutil
import random
from pathlib import Path

# Caminhos
origem = Path(r"C:\Users\otavi\OneDrive\Área de Trabalho\Projeto em IBM I\dataset_reduzido")
destino_base = Path(r"C:\Users\otavi\OneDrive\Área de Trabalho\Projeto em IBM I\dataset_final")

# Mapeamento das pastas para nomes unificados
mapeamento_ruido = {
    "gauss_0": "gauss",
    "gauss_1": "gauss",
    "sp_0": "sp",
    "sp_1": "sp",
    "poisson_low": "poisson",
    "poisson_high": "poisson",
    "sem_ruido": "clean"
}

# Inicializa um dicionário para armazenar os caminhos das imagens por tipo de ruído
imagens_por_classe = {"gauss": [], "sp": [], "poisson": [], "clean": []}

# Percorre todas as modalidades e coleta os caminhos das imagens
for modalidade in origem.iterdir():
    if modalidade.is_dir():
        for subpasta in modalidade.iterdir():
            tipo_ruido = mapeamento_ruido.get(subpasta.name)
            if tipo_ruido:
                for img in subpasta.glob("*.png"):
                    imagens_por_classe[tipo_ruido].append(img)

# Função para dividir a lista em treino/val/test
def dividir_lista(lista, train_ratio=0.7, val_ratio=0.15):
    random.shuffle(lista)
    n = len(lista)
    train = lista[:int(n * train_ratio)]
    val = lista[int(n * train_ratio):int(n * (train_ratio + val_ratio))]
    test = lista[int(n * (train_ratio + val_ratio)):]
    return train, val, test

# Copia as imagens para o novo diretório organizado
for classe, imagens in imagens_por_classe.items():
    train, val, test = dividir_lista(imagens)
    for split_name, split_list in zip(["train", "val", "test"], [train, val, test]):
        destino = destino_base / split_name / classe
        destino.mkdir(parents=True, exist_ok=True)
        for img_path in split_list:
            shutil.copy(img_path, destino / img_path.name)

print("Organização concluída com sucesso!")
