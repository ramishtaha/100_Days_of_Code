from datetime import datetime
import random
import smtplib
import pandas

PLACEHOLDER = "[NAME]"
my_email = "jalltrades12@gmail.com"
password = "@#Jack098"

birthdays_list = pandas.read_csv("birthdays.csv").to_dict(orient="records")
now = datetime.now()
for birthday_person in birthdays_list:
    try:
        if int(birthday_person["month"]) == now.month and int(birthday_person["day"] == now.day):
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as template:
                to_send = template.read().replace(PLACEHOLDER, birthday_person["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{to_send}"
                )
    except ValueError:
        pass
