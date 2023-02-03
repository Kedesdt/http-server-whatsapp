from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def envia(numero, arquivo, msg = 'Segue sua foto'):

    global navegador
    navegador.get('https://wa.me/%s' %numero)
    try:
        iniciar = WebDriverWait(navegador, 60).until(
            EC.presence_of_element_located((By.XPATH, '// *[ @ id = "action-button"]'))
        )
    except:
        navegador.quit()
    #'// *[ @ id = "action-button"]'
    #iniciar = navegador.find_element(By.XPATH, '// *[ @ id = "action-button"]')
    time.sleep(0.1)

    iniciar.click()
    try:
        ww = WebDriverWait(navegador, 60).until(
            EC.presence_of_element_located((By.XPATH, '// *[ @ id = "fallback_block"] / div / div / h4[2] / a / span'))
        )
    except:
        navegador.quit()

    time.sleep(1)
    #'// *[ @ id = "fallback_block"] / div / div / h4[2] / a / span'
    #ww = navegador.find_element(By.XPATH, '// *[ @ id = "fallback_block"] / div / div / h4[2] / a / span')
    ww.click()
    try:
        clip = WebDriverWait(navegador, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'))
        )
    except:
        navegador.quit()
    #clip = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
    time.sleep(0.1)
    clip.click()
    try:
        input = WebDriverWait(navegador, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'))
        )
    except:
        navegador.quit()
    #input = navegador.find_element(By.XPATH,
    #                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')

    time.sleep(0.1)
    input.send_keys(arquivo)
    try:
        entrada_de_texto = WebDriverWait(navegador, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'))
        )
    except:
        navegador.quit()
    #entrada_de_texto = navegador.find_element(By.XPATH,
    #                                          '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
    time.sleep(0.1)
    entrada_de_texto.send_keys(msg + '\n')



while True:

    navegador = webdriver.Chrome()

    navegador.get('http://web.whatsapp.com')
    try:
        element = WebDriverWait(navegador, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[4]/div/div/div[2]/div[1]/h1'))
        )
        break
    except:
        navegador.quit()

print("Whatsapp Carregado")

#time.sleep(30)
# TESTE whatsapp.envia("5511973658126", 'C:\\Users\\kdtorres\\Pictures\\teste.png', 'Ficou muito bom')