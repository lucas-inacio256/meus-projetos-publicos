# Modelo de CNN para números usando dataset MNIST

# Devido a limitações no dataset, o modelo erra
# em 40% das tentativas, mas serviu de aprendizado.

import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Carregar e preparar o Dataset MNIST
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalizar os pixels para o intervalo [0.0, 1.0] (ajuda na convergência do gradiente)
train_images = train_images / 255.0
test_images = test_images / 255.0

# Redimensionar para garantir que o canal de cor (1 para escala de cinza) esteja explícito
# O formato esperado é: (número_de_imagens, largura, altura, canais)
train_images = train_images.reshape((-1, 28, 28, 1))
test_images = test_images.reshape((-1, 28, 28, 1))

# Redimensionando com TensorFlow
print('Redimensionando as imagens... (Isso pode levar alguns segundos)')
imgpixels = 28
train_images = tf.image.resize(train_images, [imgpixels, imgpixels]).numpy()
test_images = tf.image.resize(test_images, [imgpixels, imgpixels]).numpy()

# Construir a Arquitetura da CNN
model = models.Sequential([
    # Primeira camada convolucional: 32 filtros de tamanho 3x3
    # Input_shape define o tamanho da imagem de entrada (largura x altura x 1)
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(imgpixels, imgpixels, 1)),
    # Camada de Max Pooling: reduz o tamanho espacial pela metade (de 26x26 para 13x13)
    layers.MaxPooling2D((2, 2)),
    
    # Segunda camada convolucional: 64 filtros para extrair padrões mais complexos
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Camada de achatamento: transforma a matriz 3D em um vetor 1D
    layers.Flatten(),
    
    # Camada densa (totalmente conectada) com 64 neurônios
    layers.Dense(64, activation='relu'),
    
    # Camada de saída: 10 neurônios (um para cada dígito de 0 a 9)
    # Usamos 'softmax' para transformar as saídas em probabilidades que somam 1
    layers.Dense(10, activation='softmax')
])

# Exibir o resumo da estrutura da rede no console
model.summary()

# Compilar o Modelo
model.compile(
    optimizer='adam', # Otimizador moderno que ajusta a taxa de aprendizado dinamicamente
    loss='sparse_categorical_crossentropy', # Função de perda para classificação multiclasse com labels inteiros
    metrics=['accuracy'] # Métrica para acompanhar durante o treino
)

# Esse callback vai monitorar o treino e só vai salvar o arquivo se o 'val_loss' diminuir
modelpath = 'python/Automação (BOTs)/Computer Vision (CV)/CNN/MNIST/'
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=modelpath+'meu_modelo.keras',
    save_best_only=True,  # Garante que não vai salvar se o modelo piorar
    monitor='val_loss',
    mode='min',
    verbose=1
)

# Para o treino antes se o modelo parar de melhorar por 2 épocas seguidas
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=2,
    restore_best_weights=True
)

# Treinar a Rede
print('\nIniciando o treinamento...')
model.fit(
    train_images, 
    train_labels, 
    epochs=6, 
    batch_size=64, 
    validation_split=0.1,
    callbacks=[checkpoint_callback, early_stopping] # Ativando os protetores [checkpoint_callback, early_stopping]
)

# Força salvamento para garantir
model.save(modelpath + 'meu_modelo.keras')

# Avaliar com dados que a rede nunca viu
print('\nAvaliando com dados de teste...')
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\nAcurácia final nos dados de teste: {test_acc * 100:.2f}%')
