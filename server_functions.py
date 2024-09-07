from dbo import StudentEvent, Student, Event, Homeroom, Base, engine, Session

session = Session()

def add_student(first_name, last_name, homeroom_id):
    global session
    try:
        new_student = Student(first_name=first_name, last_name=last_name, homeroom_id=homeroom_id)
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
    
def add_homeroom(name):
    global session
    try:
        new_homeroom = Homeroom(name=name)
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

def get_event(event_id):
    global session
    try:
        event = session.query(Event).filter(Event.id == event_id).first()
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