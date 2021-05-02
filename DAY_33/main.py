import time

import requests
from datetime import datetime
import smtplib

MY_LAT = "25.211549"
MY_LONG = "85.514542"
my_email = "jalltrades12@gmail.com"
password = "@#Jack098"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def pos_within_margin():
    if 5 >= float(MY_LAT) - iss_latitude >= -5 and 5 >= float(MY_LONG) - iss_longitude >= -5:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_dark():
    if sunrise >= time_now.hour >= sunset:
        return True
    return False

def send_main():
    if pos_within_margin() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Go watch The ISS\n\nThe ISS can be sighted now"
            )

while True:
    send_main()
    time.sleep(60)
