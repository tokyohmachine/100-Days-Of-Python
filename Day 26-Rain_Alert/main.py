import requests
from twilio.rest import Client
import os

# END_POINT = 'https://api.openweathermap.org/data/2.5/onecall'
# API_KEY = 'b5d67c648c7bda10e6cd461c2a84019c'
#
# parameters = {
#     "lat": -22.762648,
#     "lng": -47.842731,
#     "appid": API_KEY,
#       "exclude": "current, minutely, daily",
# }

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?lat=-22.118191&lon=-43.209370&exclude=current,minutely,daily&appid=b5d67c648c7bda10e6cd461c2a84019c')
response.raise_for_status()
data = response.json()
weather_data = data["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Today is going to rain, don't forget to bring an umbrella ☔ ",
        from_='+12567436658',
        to='+phone'
    )

    print(message.status)

