# Cria videos de prints da tela

import cv2
import keyboard
import pyautogui
import numpy as np

fps = 30 # Frames per second
screen_size = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*'XVID') # avi=XVID mp4=mp4h
video = cv2.VideoWriter('video.avi', codec, fps, screen_size)

while True:
    frame = pyautogui.screenshot()
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # Convert RGB to BGR

    video.write(frame)

    # Stop condition
    if keyboard.is_pressed('esc'):
        break

video.release() # Compile video
cv2.destroyAllWindows() # Recommended for cv
