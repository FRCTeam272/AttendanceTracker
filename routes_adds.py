from fastapi import File, UploadFile
import server_functions as sf
from routes import app

@app.post("/add/home_room_group")
async def add_home_room_group(group_name: str, image: UploadFile = File(...)):
    try:
        image_data = await image.read()
        group = sf.add_home_room_group(group_name, image_data)
        return group.__dict__()
    except Exception as e:
        return {"Error": str(e)}

@app.post("/add/home_room")
def add_home_room(name: str, homeroom_group_name: str):
    try:
        homeroom = sf.add_home_room(name, homeroom_group_name)
        return homeroom.__dict__()
    except Exception as e:
        return {"Error": str(e)}

@app.post("/add/student")
def add_student(name: str, homeroom_name: str):
    try:
        student = sf.add_student(name, homeroom_name)
        return student.__dict__()
    except Exception as e:
        return {"Error": str(e)}

@app.post("/add/event")
def add_event(name: str):
    try:
        event = sf.add_event(name)
        return event.__dict__()
    except Exception as e:
        return {"Error": str(e)}

@app.post("/add/attendance")
def add_student_event(student_id: int, event_id: int, reporter: str):
    try:
        student_event = sf.add_student_event(student_id, event_id, reporter)
        return student_event.__dict__()
    except Exception as e:
        return {"Error": str(e)}
