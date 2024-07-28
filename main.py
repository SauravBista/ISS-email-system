import requests
from datetime import datetime
import smtplib
# to run code every 60 seconds
import time

MY_LAT = 1 # your latitude
MY_LONG = 2 # your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 < iss_latitude <= MY_LAT+5 and MY_LONG-5<=iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    current_hour = time_now
    if int(current_hour) < sunrise or int(current_hour) > sunset:
        return True





# to keep this code running forever
while True:
    # wait for 60 seconds
    time.sleep(60)
    # then run this code
    if is_iss_overhead() and is_night():
        my_email = ""
        password = ""
        connection = smtplib.SMTP("")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="",
                            msg="Subject:ISS is Near\n\nLook Up!")
