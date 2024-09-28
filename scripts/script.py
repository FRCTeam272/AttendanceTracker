import requests
import sqlite3 as sql
from glob import glob
import os
import time
import webbrowser
import pyautogui

good = "../qrcodes/A1/_index.html"
with open(good, 'r') as f:
    good = f.read()
print(good)

for i in glob("../qrcodes/*"):
    files = glob(i + "/*.png")
    files = [i.split('\\')[-1] for i in files]
    files.sort(key=lambda x: int(x.split('.')[0]))
    title = i.split('\\')[-1]
    print(files)
    with open(i + "/_index.html", 'w') as f:
        f.write(good.replace("{TARGET}", str(files)).replace("{TITLE}", title))

for i in glob("../qrcodes/*/*.html"):
    pass
    webbrowser.open_new_tab("file://" + os.path.abspath(i))
    time.sleep(5)  # Give some time to switch to the browser window
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    print(i)
# domain = "https://jake-attendance-tracker-860c7b78dcfb.herokuapp.com/"
# for i in range(599,601):
#     try:
#         response = requests.get(domain + "/get/qrcode/student/{student_id}?query=" + str(i))
#         with open(f"../qrcodes/{i}.png", "wb") as f:
#             f.write(response.content)
#             print(f"{i}/600 {response.status_code}")
#             time.sleep(.1)
#     except:
#         pass
#     time.sleep(.1)