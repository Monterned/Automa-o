import pyautogui
import time
import keyboard 
import pandas 

pyautogui.PAUSE = 2.5
time.sleep(3)

# pyautogui.click(x=69, y=24)
# pyautogui.press(["down","down","down"])
# pyautogui.press("right")
# pyautogui.press("enter")#8
# pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab"])#24     
# pyautogui.press(["down","down","down","down","down","down"])
# pyautogui.press(["down","down","down","down","down","down","down","down"])
# pyautogui.press(["down","down","down","down","down"])
# pyautogui.press(["down","down","down","down","down"])
# pyautogui.press("enter")#


Contratos = pandas.read_csv("impCont.csv", delimiter=";")
print(Contratos)



for linha in Contratos.index:
    num = Contratos.loc[linha,"CONTRATO"] 

    for i in range(4):
        pyautogui.press("backspace")
    
    pyautogui.write(str(num))
    for i in range(2):
        pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(12)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    for i in range(4):
        pyautogui.press("tab")
    time.sleep(5)
    pyautogui.press(["up"])
    time.sleep(5)
    pyautogui.press("tab")
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(12)
    pyautogui.keyDown('alt')
    pyautogui.press("f4")
    pyautogui.keyUp('alt')
    time.sleep(10)
    for i in range(4):
        pyautogui.press("tab")

