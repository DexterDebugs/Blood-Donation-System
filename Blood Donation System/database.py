from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
'''
**What this means**
SQLAlchemy is a Python library that talks to the databases. 'create engine' is a function
from it that creates a **connection** to your PostgreSQL database - like dialing a phone number to call the database.

declarative_base is a function that creates a base class for your database models. Think of it like a blueprint template
— later when you define what a "Donor" looks like in Python, it will inherit from this base. Every table you create in 
Python will be built on top of this.
'''

DATABASE_URL = "postgresql://postgres:3251@localhost:5432/blood_donation_db"

engine = create_engine(DATABASE_URL)        ##Setting up connection using the URL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) ##creates a session(time) whenever you want to query the data. 
##autocommit = false means donot save the changes automatically, wait until confirmation.
##autoflush = false means dont send queries to the db until said
##bind = engine means use the specific road(engine) to access the DB
Base = declarative_base()       ##blueprint for all tables

def get_db():           ## A function that opens a session, hands it to FastAPI, then closes it automatically when done
    db = SessionLocal()
    try:
        yield db        ##query the DB
    finally:
        db.close()      ##close session NO MATTER WHAT

