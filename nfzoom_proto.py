from selenium import webdriver
import time
import pandas as pd

browser = webdriver.Chrome()

# opening the browser and going to Agenci@Net:
browser.get('https://www2.agencianet.fazenda.df.gov.br/')
time.sleep(15)

# clicking on 'Avançar'
browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/a').click()
time.sleep(15)

# navagating through the menus
browser.find_element_by_xpath('//*[@id="boxMainMenu"]/ul/li[2]/a').click()
browser.find_element_by_xpath('//*[@id="coluna1"]/ul/li[8]/a').click()
browser.find_element_by_xpath('//*[@id="coluna2"]/ul/li[5]/span/a/span[1]').click()
time.sleep(15)

# clicking on the CPF/CNPJ input form
#browser.find_element_by_xpath('//*[@id="CpfCnpj"]').send_keys('1025678')

# creating a data frame for the itaration
cnpj_db = pd.read_excel('cnpjs.xlsx')

def cnpj_iteration():
    for cnpj in cnpj_db:
        browser.find_element_by_xpath('//*[@id="CpfCnpj"]').send_keys(cnpj)
        

cnpj_iteration()
#creating a function to iterate the copy/paste on the CNPJ dataframe 

#browser.quit()