import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Sony-Mirrorless-Digital-Camera-ILCE7M3/dp/B07STH7C9F/ref=sr_1_2?crid=2J7RNYR1U78I7&keywords=sony+alpha+ilce-7m3+e-mount+full+format+digital+camera&qid=1565870072&s=gateway&sprefix=sony+alpha+ilce-7m3+e-mount+full+format+%2Caps%2C153&sr=8-2'
headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def checkprice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    pricerip = (price[1:9])
    print(type(pricerip))
    p=  pricerip.replace(',', '')
    print(p)


    converted_price =float(p)

    if converted_price < 1.700:
        sendMail()

    if converted_price > 1.700:
        sendMail()
    print(converted_price)
    print(title.strip())

def sendMail():
    server =smtplib.SMTP('smtp.gmail.com', 587 )
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('cretube53@gmail.com', 532155521)
    subject = 'Price has changed !'
    body = ' Check the amazon link: https://www.amazon.com/Sony-Mirrorless-Digital-Camera-ILCE7M3/dp/B07STH7C9F/ref=sr_1_2?crid=2J7RNYR1U78I7&keywords=sony+alpha+ilce-7m3+e-mount+full+format+digital+camera&qid=1565870072&s=gateway&sprefix=sony+alpha+ilce-7m3+e-mount+full+format+%2Caps%2C153&sr=8-2'

    msg = ("Subject: {}\n\n{} ").format(subject,body)
    server.sendmail('cretube53@gmail.com', 'cpejiofor@gmail.com',msg)
    print('An email has been sent')
    server.quit()

checkprice()