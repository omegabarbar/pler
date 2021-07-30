from pyscreeze import _screenshot_win32
from pyautogui import alert, leftClick, position, typewrite
from pyttsx3 import speak
from time import ctime
from os import system, startfile
from keyboard import press
import cv2
from getpass import getuser

_screenshot_win32 = _screenshot_win32
alert = alert
speak = speak
ctime = ctime
system = system
press = press
typewrite = typewrite
click = leftClick
position = position
startfile = startfile
cv2 = cv2
user = getuser
