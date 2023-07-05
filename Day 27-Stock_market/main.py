import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
# NEWS_ENDPOINT = "d4d83d1625c440628d59799645ad7cbc"
# API_KEY= '64HXACBZRGRMJLXM'

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": API_KEY,
# }


response = requests.get(url= "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=64HXACBZRGRMJLXM")
response.raise_for_status()
data = response.json()

data_list = [value for (key, value) in data.items()]
price_yesterday = data["Time Series (Daily)"]["2022-04-12"]
close_price = price_yesterday["4. close"]


price_today = data["Time Series (Daily)"]["2022-04-13"]
close_price_today = price_today["4. close"]



#TODO 3. - Find the positive difference between 1 and 2
difference = abs(float(close_price) - float(close_price_today))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# TODO 4. - percentage difference between closing price yesterday and closing price the day before yesterday.
percentage_diff = (difference / float(close_price)) * 100
print(percentage_diff)


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_diff) > 1:
    response1 = requests.get(url="https://newsapi.org/v2/everything?q=TSLA&from=2022-04-13&sortBy=popularity&"
                                 "apiKey=d4d83d1625c440628d59799645ad7cbc")
    response1.raise_for_status()
    data = response1.json()

    get_news = data["articles"][:3]



    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    new_list = [f"Headline:{article['title']}. \nBrief: {article['description']}" for article in get_news]


# TODO 9. - Send each article as a separate message via Twilio.
    TWILIO_SID = os.getenv('TWILIO_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

    for article in new_list:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body= f"{STOCK_NAME}: {up_down} {percentage_diff}% {new_list}",
            from_='+12567436658',
            to='+phone'
        )

        print(message.status)

