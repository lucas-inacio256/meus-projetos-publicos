# Encontra um elemento na tela

import cv2
import numpy as np
from PIL import Image

def encontrar_elemento(img, elemento, precisao):
    # Converte para escala de cinza (acelera o processamento)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elemento_gray = cv2.cvtColor(elemento, cv2.COLOR_BGR2GRAY)

    # Aplica template matching rápido
    resultado = cv2.matchTemplate(img_gray, elemento_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= precisao:  # Precisão
        return max_loc
    return None

if __name__ == '__main__':
    img = Image.open('path.png') # Abre imagem
    img = np.array(img) # Converte para NumPy
    
    elem = Image.open('path.png') # Abre imagem
    elem = np.array(elem) # Converte para NumPy

    print( encontrar_elemento(img, elem, 0.95) ) # Retorna (x,y) do elemento ou None
