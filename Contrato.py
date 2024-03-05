import pyautogui
import time
import keyboard 
import pandas 

pyautogui.PAUSE = 0.7
pyautogui.keyDown('alt')
pyautogui.press(["tab","tab"])
pyautogui.keyUp('alt')
pyautogui.keyDown('alt')
pyautogui.press(["tab","tab"])
pyautogui.keyUp('alt')
#pyautogui.press(["right","right","right","right"])
#pyautogui.press("enter")
pyautogui.click(x=513, y=70)
pyautogui.press(["enter","enter"])
time.sleep(2)
pyautogui.press(["enter","enter"])
time.sleep(2)
pyautogui.press(["tab","tab","tab","tab"])
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=1254, y=408)
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=140, y=284)
pyautogui.press("f2")
time.sleep(3)
pyautogui.write("transporte")#tarefa
time.sleep(3)
pyautogui.press(["tab","tab","tab","tab","tab","tab"])
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

pyautogui.press(["tab","tab","tab","tab","tab","tab"])#data de vencimento
pyautogui.press(["tab","tab","tab","tab","tab","tab"])
pyautogui.press(["tab","tab","tab","tab","tab","tab"])
pyautogui.press(["tab","tab","tab","tab","tab"])
pyautogui.write("251020232359")

pyautogui.press(["tab","tab"])#valor frete
pyautogui.keyDown('alt')
pyautogui.press("tab")
pyautogui.keyUp('alt')
pyautogui.keyDown('ctrl')
pyautogui.press("c")
pyautogui.keyUp('ctrl')
pyautogui.keyDown('alt')
pyautogui.press("tab")
pyautogui.keyUp('alt')
pyautogui.keyDown('ctrl')
pyautogui.press("v")
pyautogui.keyUp('ctrl')
pyautogui.press(["tab","tab","tab","tab","tab"])


pyautogui.keyDown('alt')#valor adiantamento
pyautogui.press("tab")
pyautogui.keyUp('alt')
pyautogui.press(["right","right","right","right"])
pyautogui.keyDown('ctrl')
pyautogui.press("c")
pyautogui.keyUp('ctrl')
pyautogui.press(["left","left","left"])
pyautogui.keyDown('alt')
pyautogui.press("tab")
pyautogui.keyUp('alt')
pyautogui.keyDown('ctrl')
pyautogui.press("v")
pyautogui.keyUp('ctrl')




pyautogui.press(["tab","tab","tab","tab","tab","tab"])#salvar
pyautogui.press(["tab","tab","tab","tab","tab","tab"])
pyautogui.press("enter")
time.sleep(2)





pyautogui.press(["tab","tab","tab","tab","tab","tab"])#salvar
pyautogui.press(["tab","tab"])
pyautogui.press("left")
time.sleep(1)

pyautogui.click(x=251, y=209)#salvar contrato
time.sleep(2)
pyautogui.click(button='right')#numero de contrato
pyautogui.press(["down","down","down"])
pyautogui.press("enter")
pyautogui.keyDown('alt')
pyautogui.press("tab")
pyautogui.keyUp('alt')
pyautogui.keyDown('ctrl')
pyautogui.press("v")
pyautogui.keyUp('ctrl')
# pyautogui.click(x=417, y=1056)
pyautogui.keyDown('ctrl')
pyautogui.press("v")
pyautogui.keyUp('ctrl')
pyautogui.keyDown('alt')
pyautogui.press("tab")
pyautogui.keyUp('alt')
# pyautogui.click(x=417, y=1056)
time.sleep(2)



pyautogui.click(x=584, y=72)
time.sleep(3)
pyautogui.press("enter")
time.sleep(5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=530, y=82)
time.sleep(2)
pyautogui.press(["tab","tab","tab","tab","tab"])
pyautogui.press("enter")
time.sleep(20)
pyautogui.click(x=1463, y=313)
time.sleep(2)
pyautogui.click(x=896, y=71)
pyautogui.press(["tab","tab"])
pyautogui.press("enter")
time.sleep(20)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press(["tab","tab","tab","tab"])
pyautogui.press(["up"])
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=1909, y=8)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=992, y=81)
time.sleep(2)
pyautogui.click(x=570, y=72)
pyautogui.write("051020231508")
pyautogui.press(["enter","enter"])
time.sleep(2)
pyautogui.press("enter")
pyautogui.press("right")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=311, y=200)
pyautogui.click(button='right')
pyautogui.press(["down","down","down"])
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=381, y=73)
time.sleep(2)
pyautogui.press(["tab","tab","tab","tab","tab"])
pyautogui.keyDown('ctrl')
pyautogui.press("v")
pyautogui.keyUp('ctrl')
time.sleep(2)
pyautogui.keyDown('shift')
pyautogui.press("tab")
pyautogui.keyUp('shift')
pyautogui.press("enter")
time.sleep(3)
pyautogui.keyDown('shift')
pyautogui.press(["tab","tab","tab","tab","tab","tab","tab"])
pyautogui.keyUp('shift')
pyautogui.press("enter")






