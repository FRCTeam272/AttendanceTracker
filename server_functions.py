import datetime
from dbo import HomeroomGroup, StudentEvent, Student, Event, Homeroom, Base, engine, Session
import json
    
session = Session()
Base.metadata.create_all(engine)
    

def add_student(name, homeroom_id):
    global session
    try:
        homeroom = session.query(Homeroom).filter(Homeroom.id == homeroom_id or Homeroom.name == homeroom_id).first()
        new_student = Student(name=name, homeroom_id=homeroom.id)
        session.add(new_student)
        session.commit()
        return new_student
    except Exception as e:
        session.rollback()
        raise e

def get_student(student_id):
    global session
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        return student
    except Exception as e:
        raise e
    
def get_students():
    global session
    try:
        students = session.query(Student).all()
        return students
    except Exception as e:
        raise e

def get_students_by_homeroom(homeroom_id):
    global session
    try:
        students = session.query(Student).filter(Student.homeroom_id == homeroom_id).all()
        return students
    except Exception as e:
        raise e
    
def add_homeroom(name, homeroom_group_name):
    global session
    try:
        group = session.query(HomeroomGroup).filter(HomeroomGroup.name == homeroom_group_name).first()
        new_homeroom = Homeroom(name=name, homeroom_group_id=group.id)
        session.add(new_homeroom)
        session.commit()
        return new_homeroom
    except Exception as e:
        session.rollback()
        raise e

def get_homeroom(homeroom_id):
    global session
    try:
        homeroom = session.query(Homeroom).filter(Homeroom.id == homeroom_id).first()
        return homeroom
    except Exception as e:
        raise e

def get_homerooms():
    global session
    try:
        homerooms = session.query(Homeroom).all()
        return homerooms
    except Exception as e:
        raise e

def add_event(name: str, multiplyer: float = 1.0):
    global session
    try:
        new_event = Event(name=name, multiplier=multiplyer)
        session.add(new_event)
        session.commit()
        return new_event
    except Exception as e:
        session.rollback()
        raise e

def get_event(query):
    global session
    try:
        event = session.query(Event).filter((Event.id == query) | (query == Event.name)).first()
        return event
    except Exception as e:
        raise e

def get_events():
    global session
    try:
        events = session.query(Event).all()
        return events
    except Exception as e:
        raise e

def add_student_event(student_id, event_id, reporter):
    global session
    try:
        new_student_event = StudentEvent(student_id=student_id, event_id=event_id, reporter=reporter)
        session.add(new_student_event)
        session.commit()
        return new_student_event
    except Exception as e:
        session.rollback()
        raise e

def get_student_event(student_id, event_id):
    global session
    try:
        student_event = session.query(StudentEvent).filter(StudentEvent.student_id == student_id, StudentEvent.event_id == event_id).first()
        return student_event
    except Exception as e:
        raise e

def get_student_events():
    global session
    try:
        student_events = session.query(StudentEvent).all()
        return student_events
    except Exception as e:
        raise e

def get_student_events_by_student(student_id):
    global session
    try:
        student_events = session.query(StudentEvent).filter(StudentEvent.student_id == student_id).all()
        return student_events
    except Exception as e:
        raise e
    
def get_student_events_by_event(event_id):
    global session
    try:
        student_events = session.query(StudentEvent).filter(StudentEvent.event_id == event_id).all()
        return student_events
    except Exception as e:
        raise e
    
def get_student_events_by_reporter(reporter):
    global session
    try:
        student_events = session.query(StudentEvent).filter(StudentEvent.reporter == reporter).all()
        return student_events
    except Exception as e:
        raise e
    
def get_student_events_by_hoomroom(homeroom_id):
    global session
    try:
        student_events = session.query(StudentEvent).join(Student).filter(Student.homeroom_id == homeroom_id).all()
        return student_events
    except Exception as e:
        raise e
    
def get_student_events_by_homeroom_group(homeroom_group_id):
    global session
    try:
        student_events = session.query(StudentEvent).join(Student).join(Homeroom).filter(Homeroom.homeroom_group_id == homeroom_group_id).all()
        return student_events
    except Exception as e:
        raise e

def add_home_room_group(name, image):
    global session
    try:
        new_homeroom_group = HomeroomGroup(name=name, image=image)
        session.add(new_homeroom_group)
        session.commit()
        return new_homeroom_group
    except Exception as e:
        session.rollback()
        raise e

class Comb_Student_Homeroom_HomeroomGroup:
    def __init__(self, student: Student, homeroom: Homeroom, homeroom_group: HomeroomGroup):
        self.student = student
        self.homeroom = homeroom
        self.homeroom_group = homeroom_group

def get_full_student_info(query, homeroom=''):
    global session
    try:
        if homeroom:
            homeroom = session.query(Homeroom).filter(Homeroom.name == homeroom).first()
            student = session.query(Student).filter(Student.homeroom_id == homeroom.id, (Student.id == query) | (Student.name.contains(query))).first()
            homeroom_group = session.query(HomeroomGroup).filter(HomeroomGroup.id == homeroom.homeroom_group_id).first()
            return Comb_Student_Homeroom_HomeroomGroup(student, homeroom, homeroom_group)
        student = session.query(Student).filter((Student.id == query) | (Student.name.contains(query))).first()
        # print(student.__dict__)
        # student = session.query(Student).filter(str(Student.id) == query or Student.name == query)
        homeroom = session.query(Homeroom).filter(Homeroom.id == student.homeroom_id).first()
        homeroom_group = session.query(HomeroomGroup).filter(HomeroomGroup.id == homeroom.homeroom_group_id).first()
        return Comb_Student_Homeroom_HomeroomGroup(student, homeroom, homeroom_group)
    except Exception as e:
        raise e

def indepth_report():
    report = {}
    for attendance in session.query(StudentEvent).order_by(StudentEvent.time_stamp).all():
            x = get_full_student_info(attendance.student_id)
            student = x.student
            homeroom = x.homeroom
            homeroom_group = x.homeroom_group
            event = get_event(attendance.event_id)
            if event.name not in report:
                report[event.name] = {}
            if homeroom_group.name not in report[event.name]:
                report[event.name][homeroom_group.name] = {}
            if homeroom.name not in report[event.name][homeroom_group.name]:
                report[event.name][homeroom_group.name][homeroom.name] = []
            
            report[event.name][homeroom_group.name][homeroom.name].append(student.name)
    return report

def report_events():
    global session

    def parse(x):
        try:
            return x[1]['total by group']
        except:
            return x[1]

    try:
        report = indepth_report()
        # total out that information for the report
        totals = {}
        for event in report:
            totals[event] = {}
            for group in report[event]:
                totals[event][group] = {}
                for homeroom in report[event][group]:
                    totals[event][group][homeroom] = len(report[event][group][homeroom])
                    
                totals[event][group]['total by group'] = sum(totals[event][group].values())
                
            totals[event]['total by event'] = sum([totals[event][group]['total by group'] for group in totals[event]])
        
        # sorts by the various totals
        for event in totals:
            sorted_groups = sorted(totals[event].items(), key=parse, reverse=True)
            totals[event] = dict(sorted_groups)

        return totals
    except Exception as e:
        raise e

def summary_report():

    def find(list, value):
        for i in list:
            if i.id == value:
                return i
        return None

    try:
        # load in all data
        student_events = session.query(StudentEvent).all()
        students = session.query(Student).all()
        homerooms = session.query(Homeroom).all()
        homeroom_groups = session.query(HomeroomGroup).all()
        events = session.query(Event).all()
        
        results = {}
        for i in homeroom_groups:
            results[i.name] = 0
        
        for i in student_events:
            student = find(students, i.student_id)
            homeroom = find(homerooms, student.homeroom_id)
            group = find(homeroom_groups, homeroom.homeroom_group_id)
            event = find(events, i.event_id)
            results[group.name] += 1 * event.multiplier

        return results
    except Exception as e:
        raise e
        

if __name__ == "__main__":
    def pretty_print(d):
        print(json.dumps(d, indent=4))  
    
    pretty_print(summary_report())
    
    pass
