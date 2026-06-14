# Captura de tela com dxcam (muito rapido)

import dxcam
import time
import numpy as np
import cv2

cam = dxcam.create(output_color="BGR")
cam.start() # Remove if using cam.grab()

while True:
    start = time.time()  # Marca o tempo inicial
    
    screenshot = cam.get_latest_frame()  # Captura a tela

    # Tratamento de imagem
    #img = np.array(screenshot)  # Converte para NumPy
    #img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # Remove transparência
    
    end = time.time()  # Marca o tempo final
    print(f"Captura de tela em {end - start:.4f} segundos")

#cam.stop()
