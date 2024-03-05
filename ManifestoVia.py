import pyautogui
import time
import keyboard 
import pandas 

pyautogui.PAUSE = 2

# pyautogui.click(x=1, y=1)
# pyautogui.press("right")
# pyautogui.press(["right","right","right"])
# pyautogui.press("down")
# pyautogui.press("right")
# pyautogui.press(["down","down","down","down","down","down"])
# pyautogui.press("right")
# pyautogui.press("enter")
# pyautogui.click(x=1111, y=1)

# time.sleep(5)
# pyautogui.write("5")
# pyautogui.press(["tab","tab","tab"])
# time.sleep(2)

viavarejo = pandas.read_csv("VIAVAREJO.csv", delimiter=";")
print(viavarejo)
var = 0
for linha in viavarejo.index:
    if var == linha:
        print(linha)
        loja = viavarejo.loc[linha,"LOJA"]
        loja = (loja)
        data = viavarejo.loc[linha,"DATA NOTA"]
        print(data)
        cte = viavarejo.loc[var,"CTE"]  
        cte = (cte)
        veic = viavarejo.loc[linha,"VEICULO"]
        veic = (veic) 
        kmini = viavarejo.loc[linha,"KM INICIAL"]
        kmini = (kmini) 
        kmfin = viavarejo.loc[linha,"KM FINAL"]
        kmfin = (kmfin)
        viagem = viavarejo.loc[linha,"VIAGEM"]
        viagem = (viagem)
        controle = viavarejo.loc[var,"VIAGEM"]
        controle = (controle)
        
        
        
        if veic == "CBU0435":
            mot = 73
        elif veic == "MEQ7888":
            mot = 65
        elif veic == "BAW8H57":
            mot = 436299
        elif veic == "AVH1912":
            mot = 436280
        else:       
            mot = 0
            print("motorista incorreto")

        met = viavarejo.loc[linha,"METRAGEM"]
        met = (met)   
        print(loja)

        if loja == 1196.0:    
            codloja = 17036     
            linha = 'SJPCTO'
        elif loja == 1242.0:    
            codloja = 17087 
            linha = 'SJPCTO'
        elif loja == 1267.0:
            codloja = 17089
            linha = 'SJPCTO' 
        elif loja == 1363.0:    
            codloja = 17566    
            linha = 'SJPNOM'
            codhor = 239
        elif loja == 1381.0:    
            codloja = 18231     
            linha = 'SJPCLI'
        elif loja == 1481.0:    
            codloja = 17033     
            linha = 'SJPCTO'
        elif loja == 1581.0:    
            codloja = 17134     
            linha = 'SJPCTO'
        elif loja == 2179.0:    
            codloja = 94325      
            linha = 'SJPBKG'
        elif loja == 1119.0:    
            codloja = 130698      
            linha = 'SJPSJP'
        elif loja == 1201.0:
            codloja = 185425 
            linha = 'SJPNDC' 
        elif loja == 1311.0:    
            codloja = 182332     
            linha = 'SJPCTO'
        elif loja == 1113.0:    
            codloja = 252930     
            linha = 'SJPCTO'
        elif loja == 1153.0:    
            codloja = 33070     
            linha = 'SJPCTO'
        elif loja == 546.0:    
            codloja = 192679 
            linha = 'SJPCTO'
        elif loja == 1734.0:    
            codloja = 108647 
            linha = 'SJPAXQ'    
        elif loja == 1655.0:    
            codloja = 212672 
            linha = 'SJPFAV'
        elif loja == 2403.0:    
            codloja = 551828
            linha = 'SJPNQO'
        elif loja == 2039:    
            codloja = 263186 
            linha = 'SJPCTO'
        elif loja == 1426.0:    
            codloja = 57227 
            linha = 'SJPCTO'
        elif loja == 442:    
            codloja = 43565 
            linha = 'SJPCTO'
        elif loja == 199.0:    
            codloja = 212671 
            linha = 'SJPCTO'
        elif loja == 1160.0:    
            codloja = 555378 
            linha = 'SJPCTO' 
        else:
            codloja = 0
            print("deu ruim")    

            print("codigo da loja {}".format(loja))
            print(codloja)
            print(mot)
            print(veic)
            print(met)  
        if mot != 0 and codloja != 0:

            time.sleep(5)
            pyautogui.press(["down","down","down"])
            pyautogui.press("tab")
            pyautogui.write(str(mot))
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])#11
            pyautogui.write(str(linha))
            pyautogui.press("tab")
            pyautogui.write("5")
            pyautogui.press("tab")

            pyautogui.keyDown('shift')
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
            pyautogui.keyUp('shift')
            pyautogui.keyUp('shift')
            pyautogui.press(["up","up","up","up","up","up","up","up"])
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])


            pyautogui.write("0")    
            pyautogui.press("tab")
            pyautogui.write("99")
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])#12
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])#13
            pyautogui.press(["right","right","right","right"])
            pyautogui.press("space")
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab"])
            pyautogui.press("right")
            time.sleep(2)


            pyautogui.press(["tab","tab","tab","tab","tab","tab"])
            pyautogui.press(["right","right","right","right","right","right","right","right","right","right","right","right","right"])#13
            pyautogui.press("tab")
            pyautogui.press(["left","left"])
            

            pyautogui.press("enter")
            time.sleep(3) 
            for linha in viavarejo.index:
                
                cte = viavarejo.loc[var,"CTE"]  
                cte = (cte)
                controle = viavarejo.loc[var,"VIAGEM"]
                controle = (controle)
                if controle == viagem:
                    pyautogui.press("tab")
                    pyautogui.write("5")
                    pyautogui.press("tab")
                    pyautogui.write("1")
                    pyautogui.press("tab")
                    pyautogui.write(str(cte))
                    pyautogui.press(["tab","tab","tab","tab","tab"])
                    pyautogui.press("space")
                    time.sleep(5)
                    
                    print(var)
                    print(linha)
                    if linha <= var:
                        var = var + 1
                        time.sleep(2)
                        print("inseriu cte {}" .format(cte))
                        print("valor de linha {}" .format(linha))
                        print("valor de var {}" .format(var))
                    else:
                        print("nao inseriu")
                    pyautogui.press("enter")
                
            



            pyautogui.press("space")
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab"])
            pyautogui.press("right")
            pyautogui.press("space")
            time.sleep(2)




            pyautogui.press("right")
            pyautogui.press(["tab","tab"])
            pyautogui.press("left")
            time.sleep(4)
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
            pyautogui.press(["left","left","left","left","left","left","left","left","left","left"])#10
            pyautogui.press("space")
            time.sleep(10)
            pyautogui.press("space")
            time.sleep(10)
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab"])#9
            pyautogui.press(["right","right","right","right","right","right"])
            pyautogui.press("space")#efetuar
            time.sleep(10)
            pyautogui.press("space")
            time.sleep(10)

            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.press(["left","left","left","left","left","left","left"])#6
            pyautogui.press("space")   
            time.sleep(2)
            pyautogui.press(["tab","tab","tab","tab","tab","tab"])    
            time.sleep(1)
            pyautogui.press("space")  
            time.sleep(2)
            pyautogui.press("space") 
            time.sleep(10)
            pyautogui.press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
            time.sleep(2)
            pyautogui.press("space") 
            time.sleep(2)
            pyautogui.press(["right","right","right","right","right","right","right","right"])
            time.sleep(5)
            pyautogui.press("space") 