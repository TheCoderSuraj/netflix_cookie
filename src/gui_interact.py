import pyautogui as pag
from asset_path import *
import platform
import pyperclip

class GuiInteract:
    # os_system = platform.system()
    # def openNetflix(self):
    #     pass 

    def check_cookie_editor_open(self):
        try:
            # print("Executing Opening cookie editor")
            pag.locateCenterOnScreen(CHECK_COOKIE_EDITOR_OPEN_PATH,grayscale=True,confidence=0.7)
            # print("Cookie editor is open")
            return True
        except pag.ImageNotFoundException :
            # print("Cookie Editor not Opened yet")
            pass
        return False

    def open_cookie_editor(self):
        if self.check_cookie_editor_open():
            return
        try:
            # print("Executing Opening cookie editor")
            editor = pag.locateCenterOnScreen(COOKIE_EDITOR_PATH,grayscale=True,confidence=0.7)
            # #print("cookie Editor position",(editor[0]/2,editor[1]/2))
            pag.moveTo(editor[0]/2,editor[1]/2)
            pag.mouseDown()
            pag.click()
        except Exception as e:
            print("Unexpected error",e)

    def click_import(self):
        try:
            #print("Executing Cookie import")
            editor = pag.locateCenterOnScreen(IMPORT_PATH,grayscale=True,confidence=0.7)
            #print("cookie import position",(editor[0]/2,editor[1]/2))
            pag.moveTo(editor[0]/2,editor[1]/2)
            # pag.mouseDown()
            pag.click()
        except Exception as e:
            print("Unexpected error",e)

    def click_delete(self):
        try:
            #print("Executing Cookie delete")
            editor = pag.locateCenterOnScreen(DELETE_PATH,grayscale=True,confidence=0.7)
            #print("cookie delete position",(editor[0]/2,editor[1]/2))
            pag.moveTo(editor[0]/2,editor[1]/2)
            pag.mouseDown()
            pag.click()
        except Exception as e:
            print("Unexpected error",e)

            
    def click_delete(self):
        try:
            #print("Executing Cookie delete")
            editor = pag.locateCenterOnScreen(DELETE_PATH,grayscale=True,confidence=0.7)
            #print("cookie delete position",(editor[0]/2,editor[1]/2))
            pag.moveTo(editor[0]/2,editor[1]/2)
            pag.mouseDown()
            pag.click()
        except Exception as e:
            print("Unexpected error",e)

    def click_reload_page(self):
        try:
            #print("Executing Reload page")
            editor = pag.locateCenterOnScreen(RELOAD_PATH,grayscale=True,confidence=0.7)
            #print("cookie reload position",(editor[0]/2,editor[1]/2))
            pag.moveTo(editor[0]/2,editor[1]/2)
            pag.mouseDown()
            pag.click()
        except Exception as e:
            print("Unexpected error",e)
        # pag.hotkey('command','r',interval=0.35)

    def addText2Clipboard(self,cookie):
        pyperclip.copy(cookie)

    def paste_cookie(self):
        pag.sleep(0.5)

        try:
            #print("Executing Cookie Paste")
            #print("Executing Right click")
            pag.rightClick()
            editor = pag.locateCenterOnScreen(PASTE_PATH,grayscale=True,confidence=0.7)
            #print("cookie delete position",(editor[0]/2,editor[1]/2))
            pag.moveTo(editor[0]/2,editor[1]/2)
            pag.mouseDown()
            pag.click()
        except Exception as e:
            print("Unexpected error",e)
        # pag.mouseDown()
        # pag.hotkey('command','v',interval=0.25)

    
    def write_cookie(self,cookie):
        self.addText2Clipboard(cookie=cookie)
        self.paste_cookie()
       
    def validateNetflix(self,delay=3):
        self.click_reload_page()
        pag.sleep(delay)
        try:
            pag.locateOnScreen(GET_STARTED_PATH, confidence=0.7,grayscale=True)
            return False
        except:
            self.open_cookie_editor()
            try:
                pag.locateOnScreen(VALIDATE_PATH, confidence=0.7,grayscale=True)
                return True
            except:
                pass
            pass
        return False
    # open_cookie_editor(COOKIE_EDITOR_PATH)

# open_cookie_editor()
# pag.sleep(1)
# click_delete()
# pag.sleep(1)
# click_import()
# pag.sleep(1)
# pasteCookie("test cookie")
# pag.sleep(1)
# click_import()
