from pynput import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()

def tap(key):
    kb.press(key)
    kb.release(key)

def on_press(key):
    try:
        if getattr(key, 'vk', None) == 97:
            print("Reinforce registered")

            tap(Key.up)
            tap(Key.down)
            tap(Key.right)
            tap(Key.left)
            tap(Key.up)

        elif getattr(key, 'vk', None) == 98:
            print("Railgun registered")

            tap(Key.down)
            tap(Key.right)
            tap(Key.down)
            tap(Key.up)
            tap(Key.left)
            tap(Key.right)
        
        elif getattr(key, 'vk', None) == 99:
            print("Hellbomb registered")

            tap(Key.down)
            tap(Key.up)
            tap(Key.left)
            tap(Key.down)
            tap(Key.up)
            tap(Key.right)
            tap(Key.down)
            tap(Key.up)

    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
