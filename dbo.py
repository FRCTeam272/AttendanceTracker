import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, BLOB, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    homeroom_id = Column(Integer, ForeignKey('homerooms.id'), nullable=False)


class HomeroomGroup(Base):
    __tablename__ = 'homeroom_groups'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    image = Column(BLOB, nullable=True)

class Homeroom(Base):
    __tablename__ = 'homerooms'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    homeroom_group_id = Column(Integer, ForeignKey('homeroom_groups.id'), nullable=False)


class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    # date = Column(String, nullable=False)
    # location = Column(String, nullable=False)

class StudentEvent(Base):
    __tablename__ = 'student_events'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    time_stamp = Column(DateTime, default=datetime.datetime.now)
    reporter = Column(String, nullable=False)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Example of creating an SQLite database and adding a student
if __name__ == "__main__":
    # Add a new student
    img = None
    with open('Logo.png', 'rb') as f:
        img = f.read()
    new_homeroom_group = HomeroomGroup(name="Test Group", image=img)
    session.add(new_homeroom_group)
    session.commit()

    new_homeroom = Homeroom(name="Jake's House", homeroom_group_id=new_homeroom_group.id)
    session.add(new_homeroom)
    session.commit()

    jake = Student(id=20171260, name="Jake Gadaleta", homeroom_id=new_homeroom.id)
    session.add(jake)
    session.commit()

    ryan = Student(id=20211260, name="Ryan Gadaleta", homeroom_id=new_homeroom.id)
    session.add(ryan)
    session.commit()

    
    new_homeroom_group = HomeroomGroup(name="Test Group 2")
    session.add(new_homeroom_group)
    session.commit()

    new_homeroom = Homeroom(name="Mick's Apartment", homeroom_group_id=new_homeroom_group.id)
    session.add(new_homeroom)
    session.commit()

    mick = Student(id=20151112, name="Mick Gadaleta", homeroom_id=new_homeroom.id)
    session.add(mick)
    session.commit()

    new_event = Event(name="Test Event")
    session.add(new_event)
    session.commit()

    new_student_event = StudentEvent(student_id=jake.id, event_id=new_event.id, reporter="Jake")
    session.add(new_student_event)
    session.commit()

    new_student_event = StudentEvent(student_id=ryan.id, event_id=new_event.id, reporter="Ryan")
    session.add(new_student_event)

    new_student_event = StudentEvent(student_id=mick.id, event_id=new_event.id, reporter="Ryan")
    session.add(new_student_event)
    session.commit()

    session.close()