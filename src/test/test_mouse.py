import pyautogui as pag
import pyperclip

# while True:
#     print(pag.mouseInfo())

pyperclip.copy("this is test copy")
pag.sleep(1)
# # pag.typewrite("this")

pag.hotkey('command','v',interval=0.2)
pag.hotkey('command','a',interval=0.25)
