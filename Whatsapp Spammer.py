from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com')

while True:
    input('\nPressione ENTER para iniciar...')
    msg = str(input('Mensagem: '))
    num = int(input('Quantidade: '))
    chat = browser.find_element_by_css_selector('._2UL8j > div:nth-child(2)')
    for x in range(num):
        if msg == '': 
            chat.send_keys(Keys.CONTROL, 'v')
        else:
            chat.send_keys(msg)
        chat.send_keys(Keys.ENTER)
