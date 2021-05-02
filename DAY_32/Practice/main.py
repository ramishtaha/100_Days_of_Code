import datetime as dt
import random
import smtplib

my_email = "jalltrades12@gmail.com"
password = "@#Jack098"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="trixterthe@gmail.com",
            msg=f"Subject:Quote of the Day\n\n{random_quote}"
        )
