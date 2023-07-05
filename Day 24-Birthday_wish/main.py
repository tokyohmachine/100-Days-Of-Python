import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "MY_EMAIL"
PASSWORD = "PASSWORD"

# call the day and month and create a tuple
today = dt.datetime.now()
today_tuple = (today.day, today.month)

# read cvs with pandas
data = pandas.read_csv("birthdays.csv")

# create a dictionary comprehension
birth_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# for loop
if today_tuple in birth_dict:
    birth_person = birth_dict[today_tuple]

    # random the letters
    num = random.randint(1, 3)
    with open(f"./Letters_birth/letter_{num}.txt") as birth_letter:
        content = birth_letter.read()
        # replace names from letters with birthdays.csv
        content = content.replace("[NAME]", birth_person["name"])
        # send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"Subject:Happy Birthday then after\n\n{content}.")









