from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# setting pre-requisites for the script
browser = webdriver.Chrome()
cnpj_db = pd.read_excel('cnpjs.xlsx')
date_init = str(input('set initial date: '))
date_final = str(input('set final date: '))

# opening the browser and going to Agenci@Net:
browser.get('https://www2.agencianet.fazenda.df.gov.br/')
time.sleep(10)

# clicking on 'Avançar'
browser.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[2]/a').click()
time.sleep(10)

# navigating through the menus 'Serviços -> Outros -> Chaves de Acesso/XML'
browser.find_element(by=By.XPATH, value='//*[@id="boxMainMenu"]/ul/li[2]/a').click()
browser.find_element(by=By.XPATH, value='//*[@id="coluna1"]/ul/li[8]/a').click()
browser.find_element(by=By.XPATH, value='//*[@id="coluna2"]/ul/li[5]/span/a/span[1]').click()
time.sleep(10)


# creating a function to iterate the copy/paste on the CNPJ dataframe
def cnpj_iteration():
    for cnpj in cnpj_db:
        browser.find_element(by=By.XPATH, value='//*[@id="CpfCnpj"]').send_keys(cnpj)
        browser.find_element(by=By.XPATH, value='//*[@id="DataInicio"]').send_keys(date_init)
        browser.find_element(by=By.XPATH, value='//*[@id="DataFim"]').send_keys(date_final)
        browser.find_element(by=By.XPATH,
                             value='/html/body/div[5]/div/div/div[1]/div/div/div[2]/form/div[7]/div/button[2]').click()
        time.sleep(10)
        browser.find_element(by=By.XPATH,
                             value='/html/body/div[5]/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[5]/a[2]/img').click()


cnpj_iteration()

browser.quit()
