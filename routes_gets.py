from fastapi import Response
from fastapi.responses import FileResponse
import server_functions as sf
from routes import app
import qrcode
import pyqrcode
from PIL import Image
import io

@app.get("/get/student/{query}")
def get_student(query: str):
    try:
        student = sf.get_full_student_info(query)
        values = student.__dict__
        # values.pop('_sa_instance_state')
        return values
        
    except Exception as e:
        return {"Error": str(e)}

@app.get(
        "/get/qrcode/student/{student_id}",
        responses={200: {"content": {"image/png": {}}}},
        response_class=Response
)
def get_student_qr_code(student_id: int):
    try:
        container = sf.get_full_student_info(student_id)
        qr_img = create_qr_code(container.student.id, center_image=container.homeroom_group.image)
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        qr_img = buffer.getvalue()
        return Response(qr_img, media_type="image/png")
    except Exception as e:
        return {"Error": str(e)}

@app.get(
        "/get/qrcode/event/{query}",
        responses={200: {"content": {"image/png": {}}}},
        response_class=Response
)
def get_event_qr_code(query: str):
    try:
        container = sf.get_event(query)
        qr_img = create_qr_code(container.id)
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        qr_img = buffer.getvalue()
        return Response(qr_img, media_type="image/png")
    except Exception as e:
        return {"Error": str(e)}

def create_qr_code(display_text, center_image=None):
    # Generate the qr code and save as png
    qrobj = pyqrcode.create(display_text)
    with open('test.png', 'wb') as f:
        qrobj.png(f, scale=10)

    # Now open that png image to put the logo
    img = Image.open('test.png')
    width, height = img.size

    if center_image:
        # How big the logo we want to put in the qr code png
        logo_size = 50

        # Open the logo image
        logo = Image.open(io.BytesIO(center_image))

        # Calculate xmin, ymin, xmax, ymax to put the logo
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        logo = logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(logo, (xmin, ymin, xmax, ymax))

    return img

@app.get("/get/report")
def get_report():
    try:
        student_events = sf.report_events()
        return student_events
    except Exception as e:
        return {"Error": str(e)}