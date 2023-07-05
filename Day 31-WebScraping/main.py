from bs4 import BeautifulSoup
import requests
import smtplib
import lxml
import os

URL = 'https://www.amazon.com/F3-Unlocked-Global-Triple-Verizon/dp/B0921YGQ6V/ref=sr_1_12?crid=1JOCXKCR4IV3K&keywords=xiaomi+' \
      'cell+phone+256gb&qid=1655043019&sprefix=xiaomi+cell+phone+256gb%2Caps%2C236&sr=8-12'


headers = {
    'Accept-Language': 'en-US,en-GB;q=0.9,en;q=0.8,pt-BR;q=0.7,pt;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

#price = soup.find(name="span", class_="a-offscreen").get_text()


# Todo Step 2: Email Alert When Price Below Preset Value
# price below R$ 500,00


title = soup.find(name='span', id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 380

MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
       )

