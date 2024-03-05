import pyautogui
import time
import keyboard 
import pandas 
import numpy as np

time.sleep(2)
pyautogui.PAUSE = 0.2
pyautogui.keyDown('alt')
pyautogui.press("tab")   
pyautogui.keyUp('alt')
viavarejo = pandas.read_csv("VIAVAREJO.csv", delimiter=";")#viavarejo = pandas.read_csv("VIAVAREJO.csv", delimiter=";")
# print(viavarejo)

planilhaCPNJ = pandas.read_excel("CNPJ.xlsx")
planilhaCPNJ.fillna(0,inplace=True)#celula vazia solução
planilhaCPNJ['CodigoLoja'] = planilhaCPNJ['CodigoLoja'].astype(np.int64)#problema do .0

data = viavarejo.loc[0,"DATA NOTA"]
print(data)
time.sleep(3)
pyautogui.press("alt")#inicia poha
pyautogui.press("right")
for i in range(2):
    pyautogui.press("down")
pyautogui.press("right")
for i in range(28):
    pyautogui.press("down")
pyautogui.press("enter")
pyautogui.PAUSE = 1
time.sleep(5)
pyautogui.press("del")#tem que executar so uma vez
for i in range(3):
    pyautogui.press("tab")
pyautogui.write(str(data))
pyautogui.press("tab") 
pyautogui.write(str(data))
for i in range(10):
    pyautogui.press("tab")
pyautogui.write("254")
pyautogui.press("tab") 
for i in range(26):
    pyautogui.press("tab")
for linha in viavarejo.index:
    loja = viavarejo.loc[linha,"LOJA"]
    loja = (loja)
    data = viavarejo.loc[linha,"DATA NOTA"]
    # print(data)
    ot = viavarejo.loc[linha,"OT"]  
    ot = (ot)
    veic = viavarejo.loc[linha,"VEICULO"]
    veic = (veic) 

    if veic == "CBU0435":
        mot = 73
    elif veic == "MEQ7888":
        mot = 65
    elif veic == "BAW8H57":
        mot = 436299
    elif veic == "AVH1912":
        mot = 436280
    elif veic == "ALA0F56":
        mot = 619497
    elif veic == "BBZ6I36":
        mot = 620288
    elif veic == "LZB6A48":
        mot = 620335

    else:       
        mot = 0
        print("motorista incorreto")

    met = viavarejo.loc[linha,"METRAGEM"]
    met = (met)   
    # print(loja)
    
    codigoLoja = planilhaCPNJ.loc[planilhaCPNJ[planilhaCPNJ['Loja'] == loja].index.values, 'CodigoLoja'].values[0]
    linhaLoja = planilhaCPNJ.loc[planilhaCPNJ[planilhaCPNJ['Loja'] == loja].index.values, 'linhaLoja'].values[0]
    cnpjLoja = planilhaCPNJ.loc[planilhaCPNJ[planilhaCPNJ['Loja'] == loja].index.values, 'cnpjLoja'].values[0]
    # print(codigoLoja)
    print(linhaLoja)
    print(cnpjLoja)
    print("codigo da loja {}".format(loja))
    print(codigoLoja)
    print(mot)
    print(veic)
    print(met)  
    if mot != 0 and codigoLoja != 0:
        for i in range(10):
            pyautogui.press("backspace")
        pyautogui.write(str(codigoLoja))
        pyautogui.press("tab")
        for i in range(34):
            pyautogui.press("tab")
        pyautogui.press("space")
        time.sleep(5)
        pyautogui.press("tab") 
        pyautogui.press("enter")
        for i in range(32):
            pyautogui.press("tab")
        pyautogui.write("5")
        pyautogui.press("tab")
        pyautogui.write("254")
        pyautogui.press("tab")
        pyautogui.write("1")
        for i in range(2):
            pyautogui.press("tab")
        for i in range(10):
            pyautogui.press("backspace")
        pyautogui.write(str(ot))
        for i in range(3):
            pyautogui.press("tab")        
        pyautogui.write(str(veic))
        pyautogui.press("tab")
        for i in range(5):
            pyautogui.press("tab")
        pyautogui.write(str(linhaLoja))
        time.sleep(1)
        for i in range(8):
            pyautogui.press("tab")        
        if codigoLoja == 130698:
            pyautogui.press("space")  
        for i in range(2):
            pyautogui.press("tab")    
        for i in range(13):
            pyautogui.press("up")     
        time.sleep(5)
        if met == 'VUC':
            for i in range(6):
                pyautogui.press("down")            
        elif met == 'HR':
            for i in range(3):
                pyautogui.press("down")             
        else:
            for i in range(2):
                pyautogui.press("down")            
        time.sleep(2)
        for i in range(17):
            pyautogui.press("tab")     
        for i in range(10):
            pyautogui.press("del") 
        for i in range(9):
            pyautogui.press("tab") 
        if codigoLoja == 130698:#8
            pyautogui.write("u")
        else:
            pyautogui.write("1")
        for i in range(15):
            pyautogui.press("tab")        
        pyautogui.press("enter")
        time.sleep(2)  
        pyautogui.press("enter")
        time.sleep(5)  
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(5)       
            
        if codigoLoja == 130698:
            for i in range(4):
                pyautogui.press("tab")            
            pyautogui.press("space") 
            for i in range(5):
                pyautogui.press("tab")            
        else:
            for i in range(9):
                pyautogui.press("tab")
            
        












