import pyautogui
import time
import keyboard 
import pandas 

pyautogui.PAUSE = 3

viavarejo = pandas.read_csv("VIAVAREJO.csv", delimiter=";")
print(viavarejo)
time.sleep(3)
pyautogui.click(x=1, y=1)   
pyautogui.press("right")
pyautogui.press(["right","right","right"])
                                                                                                                        
pyautogui.press("down")
pyautogui.press("right")
pyautogui.press(["down","down"])
pyautogui.press("enter")
pyautogui.click(x=1111, y=1)
time.sleep(5)
pyautogui.write("5")
pyautogui.press("tab")
for linha in viavarejo.index:
    cte = viavarejo.loc[linha,"CTE"]
    cte = (cte)
    frete = viavarejo.loc[linha,"FRETE"]
    print(frete)
    escolta = viavarejo.loc[linha,"ESCOLTA"]  
    escolta = (escolta)
    adicional = viavarejo.loc[linha,"ADICIONAL"]
    adicional = (adicional)   
      
    
    pyautogui.write(str(cte))
    pyautogui.press("tab")
    time.sleep(5)



    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.write(str(frete))
    pyautogui.press("tab")
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab",])#16

    pyautogui.write(str(escolta))#escolta
    pyautogui.press(["tab","tab","tab","tab","tab","tab"])


    pyautogui.write(str(adicional))#valor adicional 
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab",]) #15
    pyautogui.keyDown('ctrl')
    pyautogui.press("tab")
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("space")
    pyautogui.press(["left","left","left"])#3 EFETUAR

    time.sleep(1)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.press("enter")

    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])#37
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.keyDown('ctrl')
    pyautogui.press("tab")
    pyautogui.keyUp('ctrl')

    pyautogui.press("tab")
    pyautogui.press("left")
    
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])#10 enviar
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])#19
    pyautogui.press("space")#incluir   
    pyautogui.press(["right","right"])
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.write("5")
    pyautogui.press("tab")
    pyautogui.press("tab")