import pyautogui
import time
import pandas 
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

# pyautogui.PAUSE = 0.7
time.sleep(5)
# print(pyautogui.position())

# hoje = datetime.date.today()
# print(hoje)




agora = datetime.datetime.now()

print(agora)
print(agora.ctime())

ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minutos = agora.minute
print(dia)
print(mes)
print(ano)
print(hora)
print(minutos)
if hora <10:
    pyautogui.write("0")

# print(agora)
# qtd = input('qual o manifesto?')
# print(qtd)
    
# for i in range(3):
#     pyautogui.press([("tab")])





# viavarejo = pandas.read_csv("VIAVAREJO.csv", delimiter=";")#viavarejo = pandas.read_csv("VIAVAREJO.csv", delimiter=";")





planilhaCPNJ = pandas.read_excel("CNPJ.xlsx")#planilha em formato excell

# planilhaCPNJ.fillna(0,inplace=True)#celula vazia solução

# planilhaCPNJ['CodigoLoja'] = planilhaCPNJ['CodigoLoja'].astype(np.int64)#problema do .0

# print(planilhaCPNJ)

# for i in viavarejo['LOJA']:
#     codigoLoja = planilhaCPNJ.loc[planilhaCPNJ[planilhaCPNJ['Loja'] == i].index.values, 'CodigoLoja'].values[0]
#     linhaLoja = planilhaCPNJ.loc[planilhaCPNJ[planilhaCPNJ['Loja'] == i].index.values, 'linhaLoja'].values[0]
#     cnpjLoja = planilhaCPNJ.loc[planilhaCPNJ[planilhaCPNJ['Loja'] == i].index.values, 'cnpjLoja'].values[0]
#     print(codigoLoja)
#     print(linhaLoja)
#     print(cnpjLoja)