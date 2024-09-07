import requests

def generate_end_point(student_id, event_id, reporter):
    return f"http://127.0.0.1:5000/add/attendance?student_id={student_id}&event_id={event_id}&reporter={reporter}"

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
            except:
                print("Error: Could not connect to server, saving to a file")
                with open("backup.dat", "a+") as f:
                    f.write(f"{endpoint}\n")
            requests.post(endpoint)
        
        
if __name__ == "__main__":
    try:
        read_scanner_input()
    except KeyboardInterrupt:
        print("Exiting...")