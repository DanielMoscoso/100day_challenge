import requests
from datetime import datetime
import time
import smtplib

# MY_LAT = 51.507351  # Your latitude
# MY_LONG = -0.127758  # Your longitude
MY_LAT = -0.3898  # Your latitude
MY_LONG = -107.1416  # Your longitude

my_email = ""
password = ""


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        # print("It is above.")  # Debugging
        # print(f"ISS latitude: {iss_latitude}, longitude: {iss_longitude}")  # Debugging
        return True
    else:
        print("It is not above.")  # Debugging
        # print(f"ISS latitude: {iss_latitude}, longitude: {iss_longitude}")  # Debugging
        return False


while is_overhead():
    # Your position is within +5 or -5 degrees of the ISS position.
    # if is_overhead():
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

    if time_now.hour >= sunset and time_now.hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # This is what makes the mail secure (encrypted).
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="",
                                msg="Subject:ISS overhead!!\n\nLook up!")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
    time.sleep(60)
