# Executa o arquivo json previamente salvo do mouse na
# ordem e no tempo que foram executados

from pynput import keyboard
from threading import Thread

from os.path import exists
from pyautogui import moveTo
from pyautogui import dragTo
from pyautogui import click
from time import sleep
import json

class MouseActionExec:
    def __init__(self, folderPath, fileName, duration=0.025):
        self.stop = False

        self.keyboardThread = Thread(target=self.keyboardListener,
                                     daemon=True)
        self.keyboardThread.start()

        print('='*50)

        if exists(folderPath):

            if exists(folderPath+'/'+fileName):
                file = open(folderPath+'/'+fileName, 'r')
                actions = json.load(file)
                file.close()

                print('Runing in 5s, press ESC to stop.')
                sleep(5)

                for i in actions:
                    if self.stop:
                        break

                    if i['type'] == 'move':
                        moveTo(i['x'], i['y'], duration=duration)

                    elif i['type'] == 'drag':
                        dragTo(i['x'], i['y'], duration=duration)

                    elif i['type'] == 'click':
                        click(i['x'], i['y'], duration=duration)

            else:
                print('File not found')

        else:
            print('Folder not found')

        print('='*50)

    def keyboardListener(self):
        with keyboard.Listener(on_release=self.onRelease) as listener:
            listener.join()

    def onRelease(self, key):
        if key == keyboard.Key.esc:
            print('Stoped!')
            self.stop = True
            return False

if __name__ == '__main__':
    mae = MouseActionExec('Log', '1.json')
