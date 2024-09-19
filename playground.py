from dbo import HomeroomGroup, StudentEvent, Student, Event, Homeroom, Base, engine, session
def get_full_student_info(query, homeroom=''):
    global session
    try:
        if homeroom:
            print(f"Querying for student in homeroom: {homeroom}")
            homeroom = session.query(Homeroom).filter(Homeroom.name == homeroom).first()
            student = session.query(Student).filter(Student.homeroom_id == homeroom.id, (Student.id == query) | (Student.name.contains(query))).first()
            homeroom_group = session.query(HomeroomGroup).filter(HomeroomGroup.id == homeroom.homeroom_group_id).first()
            return (student, homeroom, homeroom_group)    
        student = session.query(Student).filter((Student.id == query) | (Student.name.contains(query))).first()
        # print(student.__dict__)
        # student = session.query(Student).filter(str(Student.id) == query or Student.name == query)
        homeroom = session.query(Homeroom).filter(Homeroom.id == student.homeroom_id).first()
        homeroom_group = session.query(HomeroomGroup).filter(HomeroomGroup.id == homeroom.homeroom_group_id).first()
        return (student, homeroom, homeroom_group)
    except Exception as e:
        raise e

x = get_full_student_info('Lily C', "D1")
print(f'{x[0].name} {x[1].name}')  # This will print the student information for 'Lily C' if it exists in the database.