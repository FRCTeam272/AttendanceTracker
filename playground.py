import dbo
import requests
from time import sleep
url = "https://jake-attendance-tracker-860c7b78dcfb.herokuapp.com"

for i in dbo.session.query(dbo.HomeroomGroup).all():
    print(i.__dict__)
    response = requests.post(f"{url}/add/home_room_group", data=i.__dict__)
    print(response.json())
    sleep(2)