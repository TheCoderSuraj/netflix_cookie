from cookie_read import CookieRead as cr
from gui_interact import GuiInteract
import os
import pyautogui as pag
import pyperclip

dirPath = "data"
delay = 0.2
files = cr.getFilePathList(dirPath)
gi = GuiInteract()

def validateCookie(cookie):
    gi.open_cookie_editor()
    pag.sleep(delay)
    gi.click_delete()
    pag.sleep(delay)
    gi.click_import()
    pag.sleep(delay)
    gi.write_cookie(cookie=cookie)
    pag.sleep(delay)
    gi.click_import()
    pag.sleep(delay)
    return gi.validateNetflix()



for path in files:
    p = os.path.join(dirPath,path)
    cookie = cr.fetch_cookie(p)
    pag.sleep(1)
    print("working on file: ",p)

    a = validateCookie(cookie)
    if a:
        print("----++++___"*8)
        print("working cookie: ",p)
        print("----++++___"*8)

    # print(cookie)
    # print("---+---"*4)
