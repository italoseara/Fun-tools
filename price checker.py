import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.jbl.com.br/headset-gamer/JBLQUANTUM100BLK.html?gclid=CjwKCAjwrKr8BRB_EiwA7eFaphdrxS7X8mb9l9bYYjcJTcwYNCqX43u4URyk0SLBv3h0dxFiTE5_PBoC_u8QAvD_BwE'

headers = {"User-Agent": 'your_user_agent'}

email = 'your_email'
password = 'your_password'

price_you_want = 999.99

print('Checking the price...')
check_price()

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    tittle = soup.find('h1', class_="headline")
    tittle_formated = tittle.get_text().strip()

    price = soup.find('span', class_="price-sales")
    price_formated = float(price.get_text().strip()[3:].replace(',', '.'))
    print(f'price: {price_formated}')

    if price_formated <= price_you_want:
        print('The price is lower!')
        send_mail(tittle_formated, price_formated)
    else:
        print('The price isn\'t lower')
    
def send_mail(tittle, price):
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    print('Logging in...')
    conn.login(email, password)
    print('Logged')
    print('Sending email...')
    conn.sendmail('from@gmail.com', 'to@gmail.com', f'Subject: {tittle}\n\n The {tittle} is R${price}\n{URL}')
    print('Email has been sent!')
    conn.quit()
