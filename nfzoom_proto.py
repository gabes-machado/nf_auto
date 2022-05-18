import pyautogui as auto
import pyperclip as pyclip
import pandas as pd
import time

auto.PAUSE = 1

auto.press('win')
auto.write('chrome')
auto.press('enter')

pyclip.copy('https://www2.agencianet.fazenda.df.gov.br/')
auto.hotkey('ctrl','v')
auto.press('enter')
time.sleep(5)
auto.press('enter')

auto.click(x=1839, y=480)
time.sleep(10)
auto.click(x=153, y=274)
auto.click(x=51, y=550)
auto.click(x=1544, y=382)
time.sleep(10)

db = pd.read_excel('cnpjs.xlsx')

display(db)
# def auto_cnpj():
 #   cnpj = db['CNPJ'].values
 #   display(cnpj)

# auto_cnpj()
