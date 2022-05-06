###details###
#this is a bot that plays minesweeper im really lazy so use this link https://www.google.com/search?q=minesweepr&rlz=1C1CHBD_en-GBGB991GB991&oq=minesweepr&aqs=chrome..69i57j46i10i433j0i10i131i433j0i10i433j0i10i131i433j0i10l4.1390j0j7&sourceid=chrome&ie=UTF-8
#at 175% zoom in on the crt only with the scroll bars in the top left corner

###imports###
import pyautogui as pag
import pytesseract, cv2, time
from pytesseract import image_to_string
from PIL import Image
import matplotlib.image as img



###variables###
#mouse cordinates
middleBlock = (920, 538)
fireFox = (704, 1085)
currentTab = (796, 1002)

startLeft = 565
startRow = 286
incrament = 76

cols = []

def startClick(x, y, z):
    pag.click(x)
    pag.click(y)
    pag.click(z)

def rowSlicer(capture, left, row):
    screenshot = pag.screenshot(region=(left, row, 75, 75))
    screenshot.save(capture + ".png")

def checker(counter):
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR'
    img = cv2.imread(str(counter) + '.png')
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(HSV_img)
    thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    checker.txt = image_to_string(thresh, config="--psm 6 digits")

def hiddenCheck():
    batman_image = img.imread('6.png')
    print(batman_image.shape)

def mousePos():
    x, y = pag.position()
    print(x, y)
###main event###
while True:
    #time.sleep(5)
    #mousePos()
    startClick(fireFox, currentTab, middleBlock)
    for row in range(0, 1):
        row = []
        counter = 0
        for i in range(0, 10):
            counter = counter + 1
            rowSlicer(str(counter), startLeft, startRow)
            startLeft = startLeft + incrament
        counter = 0
        startRow = startRow + incrament
        for i in range(0, 10):
            counter = counter + 1
            if counter == 6969696969:
                print('something is most definetly wrong')
            #checker(counter)
            #if checker.txt[:1] == '1':
            #    row.append('1')
            #elif checker.txt[:1] == '2':
            #    row.append('2')
            #elif checker.txt[:1] == '3':
            #    row.append('3')
            else:
                print(i)
                hiddenCheck()
                print('**********************************************')
                row.append('e')
        cols.append(row)
        startLeft = 94
    for row in cols:
        print(row)
    #mousePos()
    break