import pyautogui
import time

pyautogui.keyDown('altleft')
pyautogui.press('tab', presses=1)
# pyautogui.press(['tab'])

time.sleep(1)

pyautogui.keyUp('altleft')

for i in range(5):
    screen = pyautogui.screenshot()
    page = screen.crop((477,10,1400,985))
    page.save(f'page{i:03d}.png')
    pyautogui.press(['pageDown'])
