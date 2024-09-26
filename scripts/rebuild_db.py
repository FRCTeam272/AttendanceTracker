import sqlite3 as sql
# import dbo
import requests
import time

domain = "https://jake-attendance-tracker-860c7b78dcfb.herokuapp.com"
connection = None
try:
    connection = sql.connect('../database.db')
except:
    connection = sql.connect('../database.db')
class HomeroomGroup:
    def __init__(self, id, name, image):
        self.id = id
        self.image = image
        self.name = name
class Homeroom:
    def __init__(self, id, name, homeroom_group_name):
        self.id = id
        self.name = name
        self.homeroom_group_name = homeroom_group_name
class Student:
    def __init__(self, id, name, homeroom_id):
        self.id = id
        self.name = name
        self.homeroom_id = homeroom_id

homeroom_groups = []
homerooms = []

# dbo.session.execute("DELETE FROM homerooms")



for row in connection.execute("SELECT * FROM homeroom_groups"):
    group = HomeroomGroup(*row)
    homeroom_groups.append(row[1])
    response = requests.post(f"{domain}/add/home_room_group?group_name={group.name}", files={"image": group.image})
    print("HOMEROOM GROUP", response.text)
    time.sleep(1)
for row in connection.execute("SELECT * FROM homerooms"):
    homeroom = Homeroom(*row)
    homeroom_group = homeroom_groups[homeroom.homeroom_group_name - 1]
    homerooms.append(homeroom)
    response = requests.post(f"{domain}/add/home_room?name={homeroom.name}&homeroom_group_name={homeroom_group}")
    print("HOMEROOMS", response.text)
    time.sleep(1)
for row in connection.execute("SELECT * FROM students"):
    student = Student(*row)
    homeroom = homerooms[student.homeroom_id - 1]
    response = requests.post(f"{domain}/add/student?name={student.name}&homeroom_name={homeroom.name}")
    print("STUDENTS", response.text)
    time.sleep(1)