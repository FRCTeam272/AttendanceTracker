from dbo import HomeroomGroup, StudentEvent, Student, Event, Homeroom, Base, engine, Session

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

def add_event(name):
    global session
    try:
        new_event = Event(name=name)
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

def get_full_student_info(query):
    global session
    try:

        student = session.query(Student).filter((Student.id == query) | (Student.name == query)).first()
        print(student.__dict__)
        # student = session.query(Student).filter(str(Student.id) == query or Student.name == query)
        homeroom = session.query(Homeroom).filter(Homeroom.id == student.homeroom_id).first()
        homeroom_group = session.query(HomeroomGroup).filter(HomeroomGroup.id == homeroom.homeroom_group_id).first()
        return Comb_Student_Homeroom_HomeroomGroup(student, homeroom, homeroom_group)
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    query = 1
    event = session.query(Event).filter((Event.id == query) |  (query == Event.name)).first()
    print(event.__dict__)    
    pass