from pynput.keyboard import Key,Controller
import time 
import cv2 
import numpy as np
import pyautogui
from win32api import GetKeyState 

keyboard=Controller()
time.sleep(2)
keyboard.press(' ')
keyboard.release(' ')

def click(button):
    state=GetKeyState(button)
    if (state ==0) and (state == 1):
        return False
    if (state !=0) and (state !=1):
        return True

while(True):
    img = pyautogui.screenshot()
    img=np.array(img)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    ret,th=cv2.threshold(img,75,255,cv2.THRESH_BINARY)
    img2=th[210:235,737:750]
    flat=img2.ravel()
    total_pixel=len(flat)
    white_pixel=np.count_nonzero(img2)
    white_percent=white_pixel/total_pixel
 
    if white_percent >= 0.1:
        keyboard.press(' ')
        keyboard.release(' ')

    if click(0x51):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()