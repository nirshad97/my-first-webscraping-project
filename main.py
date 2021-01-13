from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = 'email@gmail.com'
MY_PASSWORD = 'password'
URL = "https://www.amazon.com/CyberpowerPC-Notebook-i5-10300H-Bluetooth-GTS99801/dp/B086QMB1DW/" \
      "ref=sr_1_1_sspa?dchild=1&keywords=gaming+laptops&qid=1610510478&sr=8-1-spons&psc=1&spLa=ZW5" \
      "jcnlwdGVkUXVhbGlmaWVyPUEyRk5ORUs4QllMREVVJmVuY3J5cHRlZElkPUEwOTYwNTg5MVJaSFZERFE2N0RHNyZlbmNyeX" \
      "B0ZWRBZElkPUEwNTQwMTc0MjJUMzZNUFFSRkQxUiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05" \
      "vdExvZ0NsaWNrPXRydWU="

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
ACCEPTED_LANGUAGE = 'en-GB,en-US;q=0.9,en;q=0.8,ta;q=0.7'
MY_PRICE = 950.00
response = requests.get(url=URL, headers={'Accept-Language': ACCEPTED_LANGUAGE, 'User-Agent': USER_AGENT})
product_webpage = response.text

soup = BeautifulSoup(product_webpage, "lxml")
current_price = float(soup.find(name='span', id='priceblock_ourprice').getText().replace("$", ""))

if MY_PRICE > current_price:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()  #  Securing the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                              to_addrs='email@yahoo.com',
                              msg=f"Subject: Lower Price\n\nThe laptop you are looking for is now ${current_price}")