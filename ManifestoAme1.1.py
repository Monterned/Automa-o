import pyautogui
import time
import keyboard 
import pandas 
import numpy as np
import datetime

pyautogui.PAUSE = 0.7
time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press("tab")   
pyautogui.keyUp('alt')

# pyautogui.press("alt")
# pyautogui.press("right")
# pyautogui.press(["right","right","right"])
# pyautogui.press("down")
# pyautogui.press("right")
# pyautogui.press(["down","down","down","down","down","down"])
# pyautogui.press("right")
# pyautogui.press("enter")




time.sleep(5)
pyautogui.keyDown('alt')
pyautogui.press("i")   
pyautogui.keyUp('alt')
time.sleep(2)

frete = pandas.read_excel("FRETE.xlsx")
frete.fillna(0,inplace=True)#celula vazia solução
frete['CODIGO MOTORISTA'] = frete['OST'].astype(np.int64)#problema do .0
print(frete)



planilhamotoristas = pandas.read_excel("MOTORISTAS.xlsx")
planilhamotoristas.fillna(0,inplace=True)#celula vazia solução
planilhamotoristas['CODIGO MOTORISTA'] = planilhamotoristas['CODIGO MOTORISTA'].astype(np.int64)#problema do .0
# print(planilhamotoristas)

cidades = pandas.read_excel("CIDADES.xlsx")
cidades.fillna(0,inplace=True)#celula vazia solução
cidades['COD HOR'] = cidades['COD HOR'].astype(np.int64)#problema do .0
# print(cidades)

for linha in frete.index:
    for i in range(3):
        pyautogui.press("down") 
    pyautogui.press("tab")

    destino = frete.loc[linha,"CIDADE"] 
    linhaLoja = cidades.loc[cidades[cidades['CIDADES'] == destino].index.values, 'LINHA'].values[0]
    codHorario = cidades.loc[cidades[cidades['CIDADES'] == destino].index.values, 'COD HOR'].values[0]
    # print(destino)  
    # print(linhaLoja)
    # print(codHorario)   
    motorista = frete.loc[linha,"MOTORISTA"] 
    # print(motorista)
    codMotorista = planilhamotoristas.loc[planilhamotoristas[planilhamotoristas['MOTORISTA'] == motorista].index.values, 'CODIGO MOTORISTA'].values[0]
    # print(codMotorista)
    numeroOST = frete.loc[linha,"OST"]
    
    pyautogui.write(str(codMotorista))
    for i in range(11):
        pyautogui.press("tab") 
    pyautogui.write(str(linhaLoja))
   
    pyautogui.press("tab")  
    pyautogui.write("5")     
    pyautogui.press("tab")
    pyautogui.write("0")
    pyautogui.press("tab")
    pyautogui.write("99")
    for i in range(12):
        pyautogui.press("tab")
    pyautogui.write(str(codHorario))
    pyautogui.keyDown('shift')
    for i in range(23):
        pyautogui.press("tab")
    pyautogui.keyUp('shift')
    for i in range(8):
        pyautogui.press("up")
    pyautogui.keyDown('alt')
    pyautogui.press("s")   
    pyautogui.keyUp('alt')
    for i in range(9):
        pyautogui.press("tab")
    pyautogui.press("right")
    for i in range(19):
        pyautogui.press("tab")
    pyautogui.press("right")
    pyautogui.press("space")
    time.sleep(2)
    for i in range(2):
        pyautogui.press("up")
    pyautogui.press("tab")
    pyautogui.write("5")
    pyautogui.press("tab")
    pyautogui.write("U")
    pyautogui.press("tab")
    pyautogui.write(str(numeroOST))
    for i in range(5):
        pyautogui.press("tab")
    pyautogui.press("space")
    time.sleep(2)
    time.sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.press("s")   
    pyautogui.keyUp('alt')

    agora = datetime.datetime.now()
    # print(agora)
    # print(agora.ctime())
    ano = agora.year
    mes = agora.month #colocar um 0 na frente com um if quando for menor que 10
    dia = agora.day #colocar um 0 na frente com um if quando for menor que 10
    hora = agora.hour #colocar um 0 na frente com um if quando for menor que 10
    minutos = agora.minute #colocar um 0 na frente com um if quando for menor que 10
    # print(dia)
    # print(mes)
    # print(ano)
    # print(hora)
    # print(minutos)


    for i in range(7):
        pyautogui.press("tab")
    pyautogui.press("left")
    for i in range(12):
        pyautogui.press("tab")
    for i in range(10):
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.press("s")   
    pyautogui.keyUp('alt')
    for i in range(2):
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press("space")
    for i in range(7):
        pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(5)
    for i in range(6):
        pyautogui.press("tab")
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press("space")
    time.sleep(5)

    for i in range(12):
        pyautogui.press("tab")
    pyautogui.press("space")
    # pyautogui.keyDown('alt')
    # pyautogui.press("i")   
    # pyautogui.keyUp('alt')

    #GERAR CONTRATO
    for i in range(5):
        pyautogui.press("right")
    pyautogui.press("space")
    time.sleep(2)
    for i in range(2):
        pyautogui.press("enter")
    time.sleep(2)
    for i in range(2):
        pyautogui.press("enter")
    time.sleep(2)
    for i in range(4):
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("left")
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.keyDown('shift')
    for i in range(2):
        pyautogui.press("tab")   
    pyautogui.keyUp('shift')
    pyautogui.press("f2")
    time.sleep(3)
    pyautogui.write("transporte")#tarefa
    time.sleep(3)
    for i in range(6):
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)
    for i in range(23):
        pyautogui.press("tab")
    pyautogui.write("101120232359")#data de pagamento
    pyautogui.keyDown('alt')
    pyautogui.press("s")   
    pyautogui.keyUp('alt')
    for i in range(8):
        pyautogui.press("tab")
    pyautogui.press("right")
    pyautogui.press("tab")
    pyautogui.press("left")
    pyautogui.keyDown('shift')
    for i in range(10):
        pyautogui.press("tab")   
    pyautogui.keyUp('shift')
    #valor adiantamento
    pyautogui.press("tab")
    pyautogui.keyDown('alt')
    pyautogui.press("s")   
    pyautogui.keyUp('alt')
    for i in range(6):
        pyautogui.press("tab") 
    pyautogui.keyUp('alt')
    pyautogui.press('space')
    time.sleep(5)
    pyautogui.press('space')
    time.sleep(5)
    for i in range(2):
        pyautogui.press("right") 
    pyautogui.press('space')
    time.sleep(3)
    for i in range(5):
        pyautogui.press("tab") 
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.keyDown('alt')
    pyautogui.press("f4") 
    pyautogui.keyUp('alt')
    time.sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.press("p") 
    pyautogui.keyUp('alt')
    for i in range(2):
        pyautogui.press("tab") 
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.press("tab") 
    pyautogui.press('space')
    for i in range(4):
        pyautogui.press("tab") 
    pyautogui.press("up") 
    pyautogui.press("tab")
    pyautogui.press('space')
    pyautogui.keyDown('alt')
    pyautogui.press("f4") 
    pyautogui.keyUp('alt')
    time.sleep(5)
    pyautogui.press('space')
    pyautogui.press("right")
    pyautogui.press('space')
    time.sleep(5)
    pyautogui.keyDown('alt')
    for i in range(3):
        pyautogui.press("tab") 
    pyautogui.keyUp('alt')
    for i in range(2):
        pyautogui.press("right")
    pyautogui.press('space')
    time.sleep(2)

    if dia <10:
        pyautogui.write("0")
    pyautogui.write(str(dia))
    if mes <10:
        pyautogui.write("0")
    pyautogui.write(str(mes))
    pyautogui.write(str(ano))
    if hora <10:
        pyautogui.write("0")
    pyautogui.write(str(hora))
    if minutos <10:
        pyautogui.write("0")
    pyautogui.write(str(minutos))
    pyautogui.press("tab") 
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press("right")
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.keyDown('alt')
    for i in range(9):
        pyautogui.press("tab") 
    pyautogui.keyUp('alt')
    for i in range(9):
        pyautogui.press("right") 
    pyautogui.press('space')
    time.sleep(5)
    for i in range(3):
        pyautogui.press("tab")
    pyautogui.keyDown('ctrl')
    pyautogui.press("c")
    pyautogui.keyUp('ctrl')
    for i in range(2):
        pyautogui.press("tab")
    pyautogui.keyDown('ctrl')
    pyautogui.press("v")
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('alt')
    pyautogui.press("tab") 
    pyautogui.keyUp('alt')
    pyautogui.press('space')
    pyautogui.press("tab")
    pyautogui.press('space')
    pyautogui.keyDown('alt')
    pyautogui.press("i")   
    pyautogui.keyUp('alt')
