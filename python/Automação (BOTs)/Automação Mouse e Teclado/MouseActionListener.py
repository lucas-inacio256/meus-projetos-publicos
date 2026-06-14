# Captura eventos do mouse na ordem e no tempo que foram
# executados e salva em arquivo json

from pynput import keyboard
from pynput import mouse
from threading import Thread
from time import sleep

from os.path import exists
from os import mkdir
import json

class MouseActionListener:
    def __init__(self, time=0.05):
        self.time = time

        self.stop = False

        self.pressed = False
        self.click = False

        self.mouseAction_onMove = None
        self.lastAction = None
        self.actions = [{'type':'Init'}]

        self.actionsAppendThread = Thread(target=self.actionsAppend,
                                          daemon=True)
        self.keyboardThread = Thread(target=self.keyboardListener,
                                     daemon=True)
        self.mouseThread = Thread(target=self.mouseListener,
                                  daemon=True)

        self.mouseThread.start()
        self.keyboardThread.start()
        self.actionsAppendThread.start()

        print('='*50)
        print('Listening!')

    def actionsAppend(self):
        while True:
            if self.stop:
                break

            if self.mouseAction_onMove != self.lastAction:
                self.actions.append(self.mouseAction_onMove)
                self.lastAction = self.mouseAction_onMove
                #print(self.mouseAction_onMove)

            sleep(self.time)

    def keyboardListener(self):
        with keyboard.Listener(on_release=self.onRelease) as listener:
            listener.join()

    def onRelease(self, key):
        if key == keyboard.Key.esc:
            self.stop = True
            return False

    def mouseListener(self):
        with mouse.Listener(on_move=self.onMove,
                            on_click=self.onClick) as listener:
            listener.join()

    def onMove(self, x, y):
        if self.stop:
            return False

        if self.pressed:
            actType = 'drag'
        else:
            actType = 'move'

        self.mouseAction_onMove = {'type':actType, 'x':x, 'y':y}

    def onClick(self, x, y, button, pressed):
        if self.stop:
            return False

        if self.pressed:
            if self.click:

                if self.actions[-1]['type'] == 'drag':
                    self.actions.append({'type':'AntiMissClick'})

                else:
                    self.actions.append({'type':'click', 'x':x, 'y':y,
                                         'button':str(button)[7:]})
                    self.click = False
                    #print('Click!')

            self.click = True

        self.pressed = pressed

if __name__ == '__main__':
    mal = MouseActionListener()
    mal.actionsAppendThread.join()
    mal.keyboardThread.join()
    mal.mouseThread.join()

    print('Saving...')

    if not exists('Log'):
        mkdir('Log')

    fileNumber = 0
    while True:
        if exists('Log/'+str(fileNumber)+'.json'):
            fileNumber += 1
        else:
            break

    file = open('Log/'+str(fileNumber)+'.json' ,'w')
    json.dump(mal.actions, file)
    file.close()

    print('Saved!')
    print('='*50)
