from selenium import webdriver
from time import sleep
import pickle

link = 'https://meet.google.com/ygj-njmz-hsu'

browser = webdriver.Firefox()
browser.get(link)
for cookie in pickle.load(open("cookie_google.pkl", "rb")): 
    browser.add_cookie(cookie)
browser.get(link)

entrar = browser.find_element_by_css_selector('div.uArJ5e:nth-child(1) > span:nth-child(3)')
entrar.click()
abrir_chat = browser.find_element_by_css_selector('.KdraA')
abrir_chat.click()
chat = browser.find_element_by_css_selector('.KHxj8b')
for x in range(10):
    chat.send_keys('é só um teste boy')
    submit = browser.find_element_by_css_selector('.hhikbc')
    submit.click()
    submit.click()
