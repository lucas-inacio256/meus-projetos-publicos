# Captura eventos do mouse

from pynput import mouse

def onMove(x, y):
    print('Pointer moved to {0}'.format(x, y))

def onClick(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed: # Stop listener
        return False

def onScroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# Collect events until released
with mouse.Listener(on_move=onMove,on_click=onClick,on_scroll=onScroll) as listener:
    listener.join()

# non-blocking version
#listener = mouse.Listener(on_move=onMove,on_click=onClick,on_scroll=onScroll)
#listener.start()
