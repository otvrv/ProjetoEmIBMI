
# Classificação de Ruídos em Imagens Médicas com Redes Neurais Convolucionais

## Introdução

Imagens médicas são essenciais para diagnósticos e decisões clínicas, mas frequentemente apresentam ruídos (como Gaussiano, Speckle, e Sal e Pimenta) que dificultam sua interpretação. Métodos tradicionais de remoção de ruído têm limitações, enquanto abordagens com redes neurais convolucionais (CNNs) mostram resultados promissores por sua capacidade de aprender padrões complexos de degradação.

## Justificativa

A identificação automática do tipo de ruído é uma etapa fundamental no pré-processamento de imagens médicas. Um erro nessa etapa pode comprometer o diagnóstico. Além disso, diferentes modalidades de imagem apresentam ruídos distintos — o que exige soluções adaptativas e robustas. Este projeto visa desenvolver um modelo capaz de reconhecer automaticamente o tipo de ruído presente na imagem, como etapa prévia à sua remoção.

## Metodologia

- **Base de dados**: Imagens de conjuntos do MedMNIST (OrganCMNIST, ChestMNIST, DermaMNIST) e MRI do Kaggle.
- **Pré-processamento**: Conversão para escala de cinza e redimensionamento para 224x224 pixels.
- **Tipos de ruído simulados**:
  - Gaussiano (variâncias: 0.001, 0.01, 0.02)
  - Sal e pimenta (densidades: 0.002, 0.01, 0.05)
  - Speckle (variâncias: 0.04, 0.07, 0.1)
- **CNN**:
  - 3 blocos convolucionais com camadas Conv2D, BatchNormalization, MaxPooling e GlobalAveragePooling
  - Camadas densas com `Dropout(0.5)` e `Dense(4, softmax)`
  - Otimizador: Adam (`lr=1e-4`), função de perda: `categorical_crossentropy`
- **Treinamento**:
  - `batch_size=32`, `epochs=50`, `early stopping` com paciência de 5 épocas
  - Classes: `clean`, `gauss`, `sp`, `speckle`

## Resultados

- **Acurácias**:
  - Treino: 89%
  - Validação: 78%
  - Teste: 72%
- **Matriz de confusão**:
  - Confusão notável entre ruído gaussiano e speckle.
  - Ruído sal e pimenta em baixa intensidade confundido com imagens limpas.
- **Considerações**:
  - Modelo apresenta desempenho promissor.
  - Possibilidades de melhoria com redes pré-treinadas (ResNet, VGG) e aumento de dados.

## Referências

1. ZHANG, F. et al. *Image denoising method based on a deep convolution neural network*. IET Image Processing, 2017.
2. SAGHEER, S. V. M.; GEORGE, S. N. *A review on medical image denoising algorithms*. Biomedical Signal Processing and Control, 2020.
3. ILESANMI, A. E.; ILESANMI, T. O. *Methods for image denoising using convolutional neural network*. Complex & Intelligent Systems, 2021.
4. GOYAL, B. et al. *Noise issues prevailing in various types of medical images*. Biomedical and Pharmacology Journal, 2018.
5. KAVITHA, G. et al. *Noise estimation and type identification...*. Journal of Healthcare Engineering, 2022.
6. NAZIR, N.; SARWAR, A.; SAINI, B. S. *Recent developments in denoising medical images using deep learning*. Micron, 2024.
7. KHAW, H. Y. et al. *Image noise types recognition using CNN with PCA*. IET Image Processing, 2017.
8. NAVONEEL. *Brain MRI Images for Brain Tumor Detection*. Kaggle, 2019. https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection
9. YANG, J. et al. *MedMNIST: A lightweight benchmark for biomedical image classification*. https://medmnist.com/

---

> **Autor**: Otávio Rogério Vieira – Universidade de São Paulo – FMRP  
> Contato: otavio.vieira@usp.br
