import pyautogui
import time

time.sleep(4)
count = 0
pyautogui.FAILSAFE = False
while count < 100:
    pyautogui.typewrite(f"Boom :{count}")
    pyautogui.press("enter")
    count = count + 1