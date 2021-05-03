import requests
from datetime import datetime
from twilio.rest import Client
TWILIO_ACCOUNT_SID = "AC273ce47769f77c7dd77e0fc8a78dc2e7"
TWILIO_AUTH_TOKEN = ""

API_KEY = ""
MY_LAT = "25.211549"
MY_LONG = "85.514542"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

time_now = datetime.now()
hour = time_now.hour

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an Umbrella!",
        from_="+14133411508",
        to='+917857942538'
    )
print(message.status)


