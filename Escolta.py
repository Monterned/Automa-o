import pyautogui
import time
import keyboard 
import pandas 
import numpy as np

pyautogui.PAUSE = 1.5
tabela = pandas.read_csv("esco.csv", delimiter=";")
print(tabela)
time.sleep(10)

tabela.fillna(0,inplace=True)#celula vazia solução
tabela['man'] = tabela['man'].astype(np.int64)#problema do .0
tabela['val'] = tabela['val'].astype(np.int64)#problema do .0

pyautogui.click(x=1, y=1)
pyautogui.press("right")
pyautogui.press(["right","right","right"])
pyautogui.press("down")
pyautogui.press("right")
pyautogui.press(["down","down","down","down","down","down"])
pyautogui.press(["down","down","down","down","down","down","down","down"])
pyautogui.press(["down","down","down","down","down"])
pyautogui.press(["down","down","down","down","down","down"])
pyautogui.press("enter")

pyautogui.write("5")
pyautogui.press(["tab","tab"])
pyautogui.press(["del","del","del","del","del","del","del","del","del","del","del","del"])
time.sleep(1)

for linha in tabela.index:
    man = tabela.loc[linha,"man"]
    print(man)

    val = tabela.loc[linha,"val"]
    print(val)

    data = tabela.loc[linha,"data"]
    print(data)

    pyautogui.write(str(data))
    pyautogui.write("0600")
    pyautogui.press("tab")
    pyautogui.press(["down","down","down"])
    pyautogui.press("tab")
    pyautogui.press(["down","down","down","down"])
    pyautogui.press("tab")
    pyautogui.write("5")
    pyautogui.press("tab")
    pyautogui.write("1")
    pyautogui.press("tab")
    pyautogui.write(str(man))
    time.sleep(3)
    pyautogui.press(["tab","tab"])
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("del")
    pyautogui.write(str(val))
    pyautogui.press(["tab","tab","tab"])
    time.sleep(3)
    pyautogui.write("51")
    time.sleep(1)
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press("enter")#salvar
    time.sleep(2)
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    time.sleep(1)
    pyautogui.press(["left","left","left"])
    pyautogui.press("enter")#autorizar
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["left","left","left"])
    pyautogui.press("enter")#efetuar
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
    pyautogui.press(["right","right","right","right","right"])
    pyautogui.press("enter")#incluir
    time.sleep(2)
    pyautogui.press(["del","del","del","del","del","del","del","del","del","del","del","del"])