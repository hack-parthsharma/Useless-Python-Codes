import pyautogui
from time import sleep

sleep(2)

for i in range(20):
	pyautogui.click(712,600)
	sleep(0.5)
	pyautogui.typewrite("ALL ARE IMPOSTOR")
	pyautogui.press("enter")
	sleep(0.5)
	pyautogui.press("enter")
	sleep(3)
	