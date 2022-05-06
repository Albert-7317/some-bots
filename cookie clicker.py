import pyautogui as pag
import time

minPrice = 10
breakCounter = 0

def startClick():
    pag.click(704, 1085)
    pag.click(796, 1002)
    for i in range(0, 100):
        pag.click(280, 457)
    
def bulkBuyer(y):
    for i in range(0, 11):
        pag.click(1612, y)
        y = y + 66

def topBuyer():
    for i in range(0, 3):
        pag.click(1629, 185)

startClick()
while True:
    for i in range(0, minPrice):
        pag.click(280, 457)
    breakCounter = breakCounter + 1
    if breakCounter == 2:
        topBuyer()
    if breakCounter == 3:
        bulkBuyer(278)
        breakCounter = 0
    if breakCounter == 99999999:
        break
        