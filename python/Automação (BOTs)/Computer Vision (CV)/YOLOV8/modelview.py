from yolov8_api import *
import numpy as np
import mss
import keyboard

yolo = YoloAPI()
yolo.load_model('model.pt')

def capture_screen(monitor):
    
    screenshot = sct.grab(monitor)
    img = np.array(screenshot)  # Converte para NumPy
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # Remove o canal alfa
    return img

with mss.mss() as sct:
    monitor = sct.monitors[1]
    cv2.namedWindow("ModelView", cv2.WINDOW_NORMAL)

    while True:
        # Captura a tela
        frame = capture_screen(monitor)
        
        # Executa a detecção de objetos
        results = yolo.predict(frame)
        
        # Desenha as caixas delimitadoras na imagem
        frame = yolo.plot_bboxes()

        # Diminui/Compacta imagem
        frame = cv2.resize(frame, (640, 360), interpolation=cv2.INTER_AREA)

        # Mostra na tela
        cv2.imshow("ModelView", frame)
        cv2.waitKey(1)

        # Stop condition
        if keyboard.is_pressed('esc'):
            break

cv2.destroyAllWindows()
