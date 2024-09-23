import dbo
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
import sqlalchemy

# Add columns to the table
dbo.session.execute(sqlalchemy.text('ALTER TABLE events ADD COLUMN multiplier FLOAT'))