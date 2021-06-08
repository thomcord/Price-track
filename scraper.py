import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

URL = 'https://www.amazon.de/Dell-S2421H-Zoll-1920x1080-entspiegelt/dp/B08GGDHQ99/ref=sr_1_12?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=monitor&qid=1622205502&sr=8-12'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

#Price function

def price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price.replace(" €", "").replace(",", "."))

    if(converted_price < 140):
        send_email()

  

    print(converted_price)
    print(title.strip())
# Send email function

def send_email():
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

# Password must be added

    server.login('thomcord@gmail.com', 'PASSWORD')

    subject = "Price fell down"
    body = "Check the link https://www.amazon.de/Dell-S2421H-Zoll-1920x1080-entspiegelt/dp/B08GGDHQ99/ref=sr_1_12?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=monitor&qid=1622205502&sr=8-12"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'thomcord@gmail.com',
        'thomcord@me.com',
        msg
    )
    print('Email has been sent')

    server.quit()

price()
