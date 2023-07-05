import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


response = requests.get(url= "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=64HXACBZRGRMJLXM")
response.raise_for_status()
data = response.json()

data_list = [value for (key,value) in data.items()]
yesterday = data["Time Series (Daily)"]["2022-04-13"]
yesterday_close = yesterday["4. close"]


today = data["Time Series (Daily)"]["2022-04-14"]
today_close = today["4. close"]


diff = abs(float(yesterday_close) - float(today_close))
up_down = None
if diff > 3:
    up_down = "🔺"
else:
    up_down = "🔻"

if float(yesterday_close) > 3:
    print("Get news")

diff_percentage = (diff / float(yesterday_close)) * 100
print(diff_percentage)


if abs(diff_percentage) > 3:
    response1 = requests.get(url="https://newsapi.org/v2/everything?q=TSLA&from=2022-04-13&sortBy=popularity&"
                                 "apiKey=d4d83d1625c440628d59799645ad7cbc")
    response1.raise_for_status()
    data_articles = response1.json()

    get_news = data_articles["articles"][:3]

    new_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in get_news]
    print(new_list)

    TWILIO_SID = os.getenv('TWILIO_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')


    for article in new_list:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {up_down} \n{diff_percentage}% \n{new_list}",
            from_='+12567436658',
            to='+phone'
        )


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
