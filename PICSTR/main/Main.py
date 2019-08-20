'''
Created on 2019年8月14日

@author: ml
'''

import services.CutWindow as cw
from pynput import mouse,keyboard
import ctypes

whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)

keyInst = {}

win = None

def on_press(key):
    global keyInst,win
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char == 'a' and 'alt_l' in keyInst and 'shift_l' in keyInst and (win is None or win.isDestroy):
            win = cw.CutWindow()
            win.win.mainloop()
        else:
            keyInst = {}
        return
    '''当 ctrl_l he shift_l 都按下的时候'''
    if key == keyboard._win32.Key.alt_l:
        keyInst['alt_l'] = 1
    elif key == keyboard._win32.Key.shift:
        keyInst['shift_l'] = 1
        
    
def on_release(key):
    global keyInst
    
    keyInst = {}
    
    
# 监听键盘按键
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
