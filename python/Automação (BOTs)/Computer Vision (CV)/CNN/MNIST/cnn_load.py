# Carrega o modelo e faz as predições

import tensorflow as tf
import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

imgpixels = 28

modelpath = 'python/Automação (BOTs)/Computer Vision (CV)/CNN/MNIST/'
imgpath = 'C:/Users/luhhl/Documents/GitHub/meus-projetos-publicos/python/Automação (BOTs)/Computer Vision (CV)/Perceptron/numbers_0-9_3x_200px/'

model = tf.keras.models.load_model(modelpath+'meu_modelo.keras')
model.summary()

images = ['0a','0b','0c',
          '1a','1b','1c',
          '2a','2b','2c',
          '3a','3b','3c',
          '4a','4b','4c',
          '5a','5b','5c',
          '6a','6b','6c',
          '7a','7b','7c',
          '8a','8b','8c',
          '9a','9b','9c']

for i in images:
    # Abrir a imagem e converter para escala de cinza ('L')
    img = Image.open(imgpath+i+'.png').convert('L')

    # Redimensionar
    img = img.resize((imgpixels, imgpixels))

    # Transformar em um array NumPy e normalizar (0.0 a 1.0)
    img_array = np.array(img) / 255.0

    # Inverter cores, fundo precisa ser preto por causa do dataset usado
    #img_array = 1.0 - img_array

    # Força o fundo a ser zero absoluto e o traço a se destacar (Thresholding)
    img_array[img_array < 0.2] = 0.0  # O que for quase preto vira preto
    img_array[img_array > 0.7] = 1.0  # O que for quase branco vira branco

    # Dilatação de traços
    img_array = ndimage.maximum_filter(img_array, size=2)

    # Encontra onde o desenho está concentrado
    cy, cx = ndimage.center_of_mass(img_array)
    
    # Se o desenho não estiver vazio, calcula o deslocamento necessário até o centro (13.5, 13.5)
    if not np.isnan(cx) and not np.isnan(cy):
        shift_x = 13.5 - cx
        shift_y = 13.5 - cy
        # Move o número para o centro exato da imagem
        img_array = ndimage.shift(img_array, shift=[shift_y, shift_x], cval=0.0)

    # Suavização
    img_array = ndimage.gaussian_filter(img_array, sigma=0.4)

    # Adicionar as dimensões extras que o Keras exige
    # De (altura, largura) vai para (quantidade, largura, altura, canal de cor)
    img_array = img_array.reshape((1, imgpixels, imgpixels, 1))

    # Fazer a previsão
    predict = model.predict(img_array)

    # O predict retorna uma lista com 10 probabilidades
    # Usamos o argmax para pegar o índice com a maior probabilidade (que é o próprio número)
    classe_predict = np.argmax(predict)
    confianca = predict[0][classe_predict] * 100

    print('='*20)
    c = 0
    for j in predict[0]:
        f = j * 100
        print(f'{c}: {f:.2f}')
        c += 1
    print('='*20)
    print(f'Numero: {classe_predict}\nConf: {confianca:.2f}%')
    print(f'Real: {i}')
