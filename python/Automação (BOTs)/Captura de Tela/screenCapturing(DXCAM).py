# Captura de tela com dxcam
# Mostra imagem
# Mostra FPS

import dxcam
import cv2
import time

cam = dxcam.create(output_color="BGR")
cam.start() # Remove if using cam.grab()

fps = 0
deltaTime = time.time()

while True:
    frame = cam.get_latest_frame() # cam.grab((x, y, width, high)) faster to specific location
    frame = cv2.resize(frame, (640, 360))
    
    if frame is not None:
        cv2.imshow("GAME", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break
    
    if time.time() - deltaTime >= 1:
        print(f'FPS: {fps}')
        deltaTime = time.time()
        fps = 0
    else:
        fps += 1

cam.stop()
