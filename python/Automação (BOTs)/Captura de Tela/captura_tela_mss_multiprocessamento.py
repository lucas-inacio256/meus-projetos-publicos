# Captura tela em multiprocessamento com delay

from threading import Thread
from queue import Queue
import numpy as np
import mss
import time

def capturar_tela(queue):
    frame_time = 0.50  # Tempo mínimo entre capturas (1.00 = 1000ms)
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        while True:
            start = time.time()

            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            queue.put(img)  # Envia a imagem para outro processo

            elapsed = time.time() - start
            time.sleep(max(0, frame_time - elapsed))  # Ajusta dinamicamente para evitar lag

def processar_imagem(queue):
    while True:
        if not queue.empty():
            img = queue.get()
            # Aqui você pode fazer a detecção rápida
            # TODO code application logic here

if __name__ == "__main__":
    queue = Queue()
    p1 = Thread(target=capturar_tela, args=(queue,))
    p2 = Thread(target=processar_imagem, args=(queue,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
