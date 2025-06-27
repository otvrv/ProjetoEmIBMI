# ProjetoEmIBMI

INTRODUÇÃO

Este repositório apresenta um projeto de pesquisa aplicado em Processamento de Imagens Médicas, com foco na identificação automática e classificação de ruídos presentes em imagens como raios-X, tomografia computadorizada (CT) e outras modalidades. O objetivo é facilitar o pré-processamento e melhorar o desempenho de tarefas como segmentação, detecção e classificação clínica com auxílio de redes neurais profundas (deep learning).

MOTIVAÇÃO

Em aplicações médicas, ruído nas imagens compromete diretamente a qualidade da análise clínica. Durante a aquisição, fatores como flutuações elétricas, movimento corporal, gordura e líquidos contribuem para a inserção de diferentes tipos de ruídos — especialmente ruído Gaussiano e quântico.

OBJETIVO

Desenvolver um modelo de deep learning capaz de detectar e classificar automaticamente diferentes tipos de ruído em imagens médicas

DATASET

Foram utilizados datasets públicos do MedMNIST, um repositório de imagens médicas otimizadas para aprendizado de máquina, e Kaggle

ABORDAGEM

Framework principal: TensorFlow/Keras
Pré-processamento com ImageDataGenerator
Dados organizados em batches para treinamento eficiente
Redes convolucionais (CNNs), classificação multiclasses, augmentação de dados e aplicação de métricas de desempenho
