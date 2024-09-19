import requests
import random

random.seed(42)  # Set seed for reproducibility
student_ids = list(map(lambda x: random.randint(1, 600), range(1, 6)))
print(student_ids)

for student_id in student_ids:
    response = requests.get(f"http://localhost:5000/get/qrcode/student/{student_id}")
    if response.status_code == 200:
        print(f"QR Code for student {student_id}")
        with open(f"qrcode_student_{student_id}.png", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to get QR Code for student {student_id}, status code: {response.status_code}")

for i in range(1, 3):
    response = requests.get(f"http://localhost:5000/get/qrcode/event/{i}")
    if response.status_code == 200:
        print(f"QR Code for event i")
        with open(f"qrcode_event_{i}.png", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to get QR Code for student {student_id}, status code: {response.status_code}")
