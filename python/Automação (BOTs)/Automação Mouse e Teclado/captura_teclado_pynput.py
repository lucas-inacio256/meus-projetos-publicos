# Captura eventos do teclado

from pynput import keyboard

def onPress(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def onRelease(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc: # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=onPress,on_release=onRelease) as listener:
    listener.join()

# non-blocking version
#listener = keyboard.Listener(on_press=onPress,on_release=onRelease)
#listener.start()
