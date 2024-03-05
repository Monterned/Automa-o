from time import sleep
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

nav = webdriver.Chrome()
wait = WebDriverWait(nav, timeout=40, poll_frequency=1)

nav.get("https://sil.opentechgr.com.br/Login.aspx")


#Login e senha
controle = wait.until(EC.element_to_be_clickable((By.ID,"txtUser")))
controle = nav.find_element(By.ID,"txtUser").send_keys("CANAA/02")
controle = nav.find_element(By.ID,"txtPass").send_keys("CANAA/02")
controle = nav.find_element(By.ID,"btnAutenticar").click()

controle = wait.until(EC.element_to_be_clickable((By.ID,"txtPas")))



controle = nav.find_element(By.ID,"txtPas").click()
controle = nav.find_element(By.ID,"txtPas").send_keys("CANAA")

controle = nav.find_element('xpath','//*[@id="txtPas"]').send_keys(Keys.DOWN)

controle = nav.find_element('xpath','//*[@id="txtPas"]').send_keys(Keys.TAB)

nav.find_element('xpath','//*[@id="txtPas"]').send_keys(Keys.ENTER)

#opções Menu
controle = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[4]/div[8]/div/div/ul/li[3]/a")))
controle = nav.find_element(By.XPATH,'/html/body/form/div[4]/div[8]/div/div/ul/li[3]/a').click()

controle = nav.find_element(By.XPATH,'/html/body/form/div[4]/div[8]/div/div/ul/li[3]/ul/li[2]/a').click()

controle = nav.find_element(By.XPATH,'/html/body/form/div[4]/div[8]/div/div/ul/li[3]/ul/li[2]/ul/li[1]/a').click()

controle = nav.find_element(By.XPATH,'/html/body/form/div[4]/div[8]/div/div/ul/li[3]/ul/li[2]/ul/li[1]/ul/li[1]/a').click()

sleep(2)





controle = nav.find_element(By.XPATH,"/html/body/form/div[3]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/input").click()
# controle = nav.find_element(By.ID,"txtPas").send_keys("CANAA")

# controle = nav.find_element('xpath','/html/body').click()
# controle = nav.find_element('xpath','/html/body').send_keys("02518893946")

# //*[@id="OpenPopup_ctl00_PW0"]()
#controle = wait.until(EC.element_to_be_clickable((By.ID,"OpenPopup_ctl00_PW0(txtCPFMot1)")))
# controle = nav.find_element((By.ID,"OpenPopup_ctl00_PW0(txtCPFMot1)")).send_keys("02518893946")


# controle = wait.until(EC.element_to_be_clickable((By.ID,"txtCPFMot1")))
# controle = nav.find_element(By.ID,"txtCPFMot1").click()
# controle = nav.find_element(By.ID,"txtCPFMot1").send_keys("02518893946")

# //*[@id="txtCPFMot1"]


sleep(5)

# /html/body

# nav.save_screenshot("fototeste.png")
# sleep(5)
# //*[@id="cmbNacionalidadeMOT1"]

# //*[@id="txtCPFMot1"]
# /html/body/form/div[3]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/input





