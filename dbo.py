import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    homeroom_id = Column(Integer, ForeignKey('homerooms.id'), nullable=False)

class Homeroom(Base):
    __tablename__ = 'homerooms'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
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
    new_homeroom = Homeroom(name="Jake's House")
    session.add(new_homeroom)
    session.commit()

    new_student = Student(name="Jake Gadaleta", homeroom_id=new_homeroom.id)
    session.add(new_student)
    session.commit()

    new_event = Event(name="Test Event")
    session.add(new_event)
    session.commit()

    new_student_event = StudentEvent(student_id=new_student.id, event_id=new_event.id, reporter="Jake Gadaleta")
    session.add(new_student_event)
    session.commit()

    session.close()