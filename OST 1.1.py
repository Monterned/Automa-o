import pyautogui
import time
import keyboard 
import pandas 
import numpy as np

pyautogui.PAUSE = 1.5
time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press("tab")   
pyautogui.keyUp('alt')

pyautogui.press("alt")
pyautogui.press("right")
pyautogui.press(["down","down"])
pyautogui.press("right")
pyautogui.press("enter")
time.sleep(3) 

pyautogui.keyDown('shift')
for i in range(2):
    pyautogui.press("tab")   
pyautogui.keyUp('shift')
pyautogui.press("right")
for i in range(7):
    pyautogui.press('tab')
pyautogui.press(["right","right"])
for i in range(10):
    pyautogui.press("tab") 
pyautogui.press("left")
pyautogui.keyDown('alt')
pyautogui.press("i")
pyautogui.keyUp('alt')

teste = pandas.read_excel("TESTE.xlsx")
teste.fillna(0,inplace=True)#celula vazia solução
teste['MAN'] = teste['MAN'].astype(np.int64)#problema do .0
# print(teste)

motoristas = pandas.read_excel("MOTORISTAS.xlsx")
# print(codigomotoristas)



for linha in teste.index:
    print(linha)
    motorista = teste.loc[linha,"MOTORISTA"]    
    codigoMotorista = motoristas.loc[motoristas[motoristas['MOTORISTA'] == motorista].index.values, 'COD'].values[0]
    print(motorista)
    print(codigoMotorista)
    doc = teste.loc[linha,"DOC"]
    print("NOTA: {}" .format(doc))
    viagem = teste.loc[linha,"VIAGEM"]
    print("VIAGEM: {}" .format(viagem))
    data = teste.loc[linha,"DATA"]
    valorOst = str(teste.loc[linha,"VALOR OST"])
    valorOst = valorOst.replace('.',',')

    print(valorOst)
   

    time.sleep(2)  
    pyautogui.write("5")
    pyautogui.press(["tab","tab","tab"])
    for i in range(12):
        pyautogui.press("tab")
    pyautogui.write(str(codigoMotorista))
    pyautogui.press(["tab","tab","tab","tab","tab"])
    pyautogui.write("625195")
    pyautogui.press(["tab","tab"])
    pyautogui.write("625195")
    pyautogui.press(["tab","tab"])
    pyautogui.write("625195")
    for i in range(7):
        pyautogui.press("tab")
    time.sleep(2)  
    pyautogui.write("sjpsjp")
    pyautogui.press(["tab","tab","tab"])
    pyautogui.press(["down","down"])
    pyautogui.press("tab")
    pyautogui.keyDown('alt')
    pyautogui.press("s")
    pyautogui.keyUp('alt')

    
    pyautogui.press("space")#salvar
    for i in range(7):
        pyautogui.press("tab")
    pyautogui.press(["right","right"])
    for i in range(10):
        pyautogui.press("tab")
       
    for i in range(8):
        pyautogui.press("up")   
    for i in range(15):
        pyautogui.press("tab")    
    pyautogui.press("space") 
    
    pyautogui.write("0")
    pyautogui.press("tab")
    pyautogui.write(str(doc))
    pyautogui.press("tab")
    pyautogui.write(str(data))
    pyautogui.write("06:00")
    pyautogui.press(["tab","tab"])
    pyautogui.write("7")

    for i in range(4):
        pyautogui.press("tab")
    
    pyautogui.write("1")
    pyautogui.press("tab")
    pyautogui.write("1")
    for i in range(4):
        pyautogui.press("tab")
    pyautogui.write("1")
    pyautogui.press(["tab","tab","tab"])
    pyautogui.write(str(viagem))
    for i in range(25):
        pyautogui.press("tab")
    pyautogui.press("space")
    pyautogui.press("left")
    pyautogui.press("enter")
    time.sleep(5) 


    pyautogui.write(str(valorOst)) 
    pyautogui.press("tab")
    pyautogui.press("right")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.keyDown('alt')
    pyautogui.press("s")
    pyautogui.keyUp('alt')
    for i in range(2):
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(5) 
    pyautogui.press("enter")
    time.sleep(5) 
    pyautogui.keyDown('alt')
    pyautogui.press("i")
    pyautogui.keyUp('alt')
    for i in range(2):
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.keyDown('alt')
    pyautogui.press("i")
    pyautogui.keyUp('alt')

#     time.sleep(2) 
#     pyautogui.click(x=273, y=154)
#     pyautogui.press("tab")
#     pyautogui.press("enter")
#     pyautogui.click(x=240, y=563)
#     pyautogui.write("CURITIBA")
#     pyautogui.write("     ")
#     pyautogui.press("tab")
















