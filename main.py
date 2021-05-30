import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui
from util import reader
from util import util
from util.cell import Cell
import time
import json
import jsonpickle

show_mouse_pos = False

if __name__ == "__main__":
    print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")
else:
    print("Datei wurde als Modul aufgerufen")

# img = ImageGrab.grab(bbox=(100, 10, 400, 780)) #bbox specifies specific region (bbox= x,y,width,height)
# img_np = np.array(img)
# frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
# cv2.imshow("test", frame)
# cv2.waitKey(0)
# print(reader.read_text(img))
#
# pyautogui.click(100, 100)
# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

if show_mouse_pos:
    pos = pyautogui.position()
    while(True):
        new_pos = pyautogui.position()
        if new_pos != pos:
            print(new_pos)
        pos = new_pos

cells = []

for y in range(110, 1640, 5):
    for x in range(320, 1640, 10):
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
        time.sleep(3)
        if reader.read_pixel() > 0:
            cell = Cell(reader.read_pixel(), reader.read_potential(), reader.read_sinus(), x, y)
            cells.append(cell)

        if len(cells) % 10 == 0:
            jsonStr = jsonpickle.encode(cells)
            text_file = open("Output.json", "w")
            text_file.write(jsonStr)
            text_file.close()
            print(jsonStr)



