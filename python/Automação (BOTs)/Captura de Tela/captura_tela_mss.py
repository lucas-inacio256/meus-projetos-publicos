# Captura de tela com mss

import mss
import time
import numpy as np
import cv2

with mss.mss() as sct:
    monitor = sct.monitors[1]  # Captura a tela inteira (ou ajuste região)
    
    while True:
        start = time.time()  # Marca o tempo inicial
        
        screenshot = sct.grab(monitor)  # Captura a tela

        # Tratamento de imagem
        #img = np.array(screenshot)  # Converte para NumPy
        #img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # Remove transparência
        
        end = time.time()  # Marca o tempo final
        print(f"Captura de tela em {end - start:.4f} segundos")
