import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "MY_EMAIL"
PASSWORD = "PASSWORD"


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    n = random.randint(1, 3)
    with open(f"./Letters_birth/letter_{n}.txt") as letter:
        lines = letter.read()
        lines = lines.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy Birthday\n\n{lines}.")
























