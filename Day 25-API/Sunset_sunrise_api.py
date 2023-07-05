import requests
import datetime
import smtplib
import time
import os

MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

MY_LAT = -22.762648
MY_LONG = -47.842731

# Todo 1: API ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Todo 2: API my position
#response = requests.get('https://api.sunrise-sunset.org/json?lat=51.507351&lng=-0.127758&formatted=0')
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
my_position = (sunrise, sunset)

time_now = datetime.datetime.now().hour


while True:
    time.sleep(60)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        if time_now >= sunrise or time_now <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="destinatary_email",
                                    msg=f"Subject:Look up\n\nISS is over your head.")

# "ericksonleon@gmail.com"

