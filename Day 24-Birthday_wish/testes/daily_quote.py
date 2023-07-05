import smtplib
import datetime as dt
import random


# Todo 1: Send a motivational quote via email on the current weekday
# use the datetime module to obtain the current day of the week
# open the quotes.txt file and obtain a list of quote
# use the random module to pick a random quote from your list
# use the smtplib to send the email to yourself
#"testcode812@yahoo.com"
#"rrgfhvkwiijiwfpm"

my_email = 'your_email'
password =  'your_password'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("Quotes/quotes.txt") as quote_file:
        data = quote_file.readlines()
        quote = random.choice(data)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="your-email",
                            msg=f"Subject:Today's quote\n\nHello,"
                                f"Try not to become a person of success, but rather try to become a person of value.-Albert Einstein.")





