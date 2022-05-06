import time
import pyautogui as pag

def mousePos():
    x, y = pag.position()
    print(x, y)

time.sleep(5)
mousePos()