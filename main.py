import requests
import smtplib
from datetime import datetime
# use mylatlong website to find latitude and longitude of your location
# MY_LATITUDE = enter your latitude location
# MY_LONGITUDE = enter your longitude location


def position_check():
    if((MY_LONGITUDE-5<=iss_position[0] and iss_position[0]<=MY_LONGITUDE+5) and (MY_LATITUDE-5<=iss_position[1] and iss_position[1]<=MY_LATITUDE+5) ):
        return True
    else:
        return False




COORDINATES = {
    "lat" : MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "formatted" : 0

}

response = requests.get(url= "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_position = (float(data["iss_position"]["longitude"]), float(data["iss_position"]["latitude"]))
print(iss_position)


response = requests.get(url="https://api.sunrise-sunset.org/json", params=COORDINATES)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+5
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])+5
time_now = datetime.now().hour


if(position_check()):
    if(time_now>sunset or time_now<sunrise):
        # my_email = enter sender email
        # password = enter sender password

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user = my_email, password=password)
            # connection.sendmail(from_addr=my_email, to_addrs=enter receiver mail, msg="Subject:Look up\n\n The international "
            #                                                                                   "space staion is above your city.")





