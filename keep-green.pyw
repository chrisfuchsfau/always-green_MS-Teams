import pyautogui
import time


def press_ctrl(t_min):
    t_sec = t_min * 60
    while time:
        pyautogui.hotkey('ctrl')
        time.sleep(t_sec)


press_ctrl(9.9)
