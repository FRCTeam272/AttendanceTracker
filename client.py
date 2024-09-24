try:
    import requests
    import os
except:
    import os
    try:
        os.system("python -m pip install requests")
        import requests
    except:
        print("Could not install requests, please try again while conected to the internet")


domain = "https://jake-attendance-tracker-860c7b78dcfb.herokuapp.com"
def generate_end_point(student_id, event_id, reporter):
    return f"{domain}/add/attendance?student_id={student_id}&event_id={event_id}&reporter={reporter}"

def read_scanner_input():
    reporter = input("Enter reporter name (type): ")
    event_scan = input("Enter event (scan): ")
    while(True):
        student_scan = input("Ready To Scan Student: ")
        if student_scan:
            endpoint = generate_end_point(student_scan, event_scan, reporter)
            print(f"Endpoint: {endpoint}")
            try:
                response = requests.post(endpoint)
                if response.status_code == 200 or response.status_code == 201:
                    print("Success")
            except:
                print("Error: Could not connect to server, saving to a file")
                with open("backup.dat", "a+") as f:
                    f.write(f"{endpoint}\n")
            requests.post(endpoint)
        
def try_to_sync():
    try:
        with open("backup.dat", "r+") as f:
            for line in f:
                try:
                    response = requests.post(line)
                    if response.status_code == 200 or response.status_code == 201:
                        print("Success")
                except:
                    print("Error: Could not connect to server, will continue to write to file")
                    return
        print("All backups synced")
        os.remove("backup.dat")
    except:
        print("No backups found")    
    

        
if __name__ == "__main__":
    try:
        try_to_sync()
        read_scanner_input()
    except KeyboardInterrupt:
        print("Exiting...")