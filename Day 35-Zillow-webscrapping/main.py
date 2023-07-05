from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests


GOOGLE_FORMS = ("https://docs.google.com/forms/d/e/1FAIpQLScDw6Rfr74F_6Nix2PHFOaqoW5z_j3ifZGLVsiHo8e5fIp0IQ/viewform?usp=sf_link")
URL = ('https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.84634627294922%2C%22east%22%3A-122.0649436850586%2C%22south%22%3A37.5611436946643%2C%22north%22%3A38.09265107862557%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D')


headers = {
    'Accept-Language': 'en-US,en-GB;q=0.9,en;q=0.8,pt-BR;q=0.7,pt;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}


response = requests.get(URL, headers=headers)
CHROME_PATH = Service('CHROME_PATH')
driver = webdriver.Chrome(service=CHROME_PATH)
data = response.text

soup = BeautifulSoup(data, "html.parser")
#print(soup.prettify())


all_listings = soup.select(".list-card-top a")

link_lists = []
for link in all_listings:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_listings.append(f"https://www.zillow.com{href}")
    else:
        all_listings.append(href)


all_address = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address]

all_price = soup.select(".list-card-details li")
all_prices = [price.get_text().split("+")[0] for price in all_price if "$" in price.text]


print(len(link_lists))
for n in range(len(link_lists)):
    driver.get(GOOGLE_FORMS)

    time.sleep(3)

    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(link_lists[n])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit_button.click()

    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()