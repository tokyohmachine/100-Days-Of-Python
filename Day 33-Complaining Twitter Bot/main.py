from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


# Todo: Step 1 - Setup Your Twitter Account


PROMISED_DOWN = 200
PROMISE_UP = 10
CHROME_DRIVER_PATH = Service('C:/Development/chromedriver.exe')
TWITTER_EMAIL = 'your_email'
TWITTER_PASSWORD = 'your_password'


#Todo: Step 2 - Create a Class


class InternetSpeedTwitterBot:
    def __init__(self,path):
        self.driver = webdriver.Chrome(service=path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go_button.click()

        sleep(60)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')


        sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]')

        password.send_keys(TWITTER_PASSWORD)

        sleep(3)
        password.send_keys(Keys.ENTER)

        sleep(5)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div')

        message = f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for ' \
                  f'{PROMISED_DOWN}DOWN/{PROMISE_UP}up.'
        tweet.send_keys(message)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


# call the two methods
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


# Todo: Step 4 - Building a Twitter Bot to Tweet at your Internet Provider