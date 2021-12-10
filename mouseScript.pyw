import pyautogui
import time


def mouse_move(t_min):
    t_sec = t_min * 60
    while time:
        pyautogui.hotkey('ctrl')
        time.sleep(t_sec)


mouse_move(9.9)
