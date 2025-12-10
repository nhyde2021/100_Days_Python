import requests
import smtplib



API_KEY = "24139b4aa701f6a28f02229e60ec680d"
MY_LAT = "38.365012"
MY_LON = "-82.456523"

MY_EMAIL = "neil.hyde17@gmail.com"
MY_PASSWORD = "qjsxsneuwleyqzko"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters, verify=False)
response.raise_for_status()
weather_data = response.json()

umbrella_needed = False

for period in weather_data["list"]:
    if period["weather"][0]["id"] < 700:
        umbrella_needed = True

if umbrella_needed:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="smtp_test_nch@yahoo.com",
            msg="Subject:Precipitation Incoming!\n\nGrab that umbrella, it's going down!"
        )