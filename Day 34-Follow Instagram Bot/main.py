from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = 'your_email'
PASSWORD = 'your_password'


# Todo Step 1 - Get Your Instagram Credentials

CHROME_DRIVER_PATH = Service('C:/Development/chromedriver.exe')


#Todo Step 2 - Create a Class

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=path)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        email = self.driver.find_element(By.NAME, 'username')
        password = self.driver.find_element(By.NAME, 'password')

        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(5)
        self.driver.get('https://www.instagram.com/page')

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, './/*[contains(text(), "followers")]/spa')
        followers.send_keys(Keys.ENTER)

        time.sleep(2)
        modal = self.driver.find_elements(By.XPATH, '//*[@id="mount_0_0_VJ"]/div/div/div/div[2]/div/div/'
                                                    'div[1]/div/div[2]/div/div/div/div/div')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR, 'li button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


# call the three methods
bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()