import datetime
import os
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, BINARY, create_engine
import sqlalchemy
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
    image = Column(sqlalchemy.LargeBinary, nullable=True) # large binary is used insted of BLOB for postgres compatibility

class Homeroom(Base):
    __tablename__ = 'homerooms'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    homeroom_group_id = Column(Integer, ForeignKey('homeroom_groups.id'), nullable=False)


class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    multiplier = Column(sqlalchemy.Float, default=1)
    # date = Column(String, nullable=False)
    # location = Column(String, nullable=False)

class StudentEvent(Base):
    __tablename__ = 'student_events'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    time_stamp = Column(DateTime, default=datetime.datetime.now)
    reporter = Column(String, nullable=False)

try:
    from dotenv import load_dotenv
    load_dotenv()
    engine = create_engine(
        os.environ.get(
            'DATABASE_URL', 
            'sqlite:///database.db'
        )
        .replace("postgres", "postgresql") # SQL Alchemy doesn't support postgres:// as of 2021 so well do this to make heroku happy
    )
except:
    engine = create_engine(
        os.environ.get(
            'DATABASE_URL', 
            'sqlite:///database.db'
        )
        .replace("postgres", "postgresql") # SQL Alchemy doesn't support postgres:// as of 2021 so well do this to make heroku happy
    )

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Example of creating an SQLite database and adding a student
if __name__ == "__main__":
    pass