# importar bibliotecas
from re import I
from selenium import webdriver
import time
from selenium.webdriver.common import keys
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar até o whatsapp Web
driver = webdriver.Chrome(ChromeDriverManager().install())
# Buscar contatos/ grupos
driver.get('https://web.whatsapp.com/')
time.sleep(30)
# Definir contatos, grupos, e mensagens a serem enviadas
contatos = ['Friends']
#não colocar em [] pois se não ele identifia como uma lista
mensagem = 'teste!'


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')

    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

   


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)