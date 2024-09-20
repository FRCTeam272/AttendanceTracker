from fastapi import Response
from fastapi.responses import FileResponse
import server_functions as sf

import qrcode
import pyqrcode
from PIL import Image
import io
from PIL import ImageDraw, ImageFont

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
def get_student_qr_code(query: str, homeroom = ''):
    try:
        container = sf.get_full_student_info(query, homeroom)
        display_text = f"{container.student.name} - {container.homeroom.name}"
        qr_img = create_qr_code(container.student.id, center_image=container.homeroom_group.image, additional_text=display_text)
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
        qr_img = create_qr_code(container.id, additional_text=container.name)
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        qr_img = buffer.getvalue()
        return Response(qr_img, media_type="image/png")
    except Exception as e:
        return {"Error": str(e)}

def create_qr_code(display_text, center_image=None, additional_text=None):
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
    if additional_text:
        # Create a new image with extra space for the text
        new_height = height + 50  # Adjust the height to fit the text
        new_img = Image.new("RGB", (width, new_height), "white")
        new_img.paste(img, (0, 0))

        # Draw the text at the bottom of the image
        draw = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()
        # text_width, text_height = draw.textsize(additional_text, font=font)
        text_x = (width - 50) / 2
        text_y = height - (80) / 2
        draw.text((text_x, text_y), additional_text, fill="black", font=font)

        img = new_img
    return img

@app.get("/get/report")
def get_report():
    try:
        student_events = sf.report_events()
        return student_events
    except Exception as e:
        return {"Error": str(e)}

@app.get("/get/indepth_report")
def indepth_report():
    try:
        student_events = sf.indepth_report()
        return student_events
    except Exception as e:
        return {"Error": str(e)}