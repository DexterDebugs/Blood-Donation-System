from sqlalchemy import Column, Integer, String, Boolean, Date, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class Donor(Base):      ##Base keeps track of all your tables
    '''You're telling SQLAlchemy:
    "Hey, register this Donor class as one of my database tables"'''
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    blood_group = Column(String(5), nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    city = Column(String(50))
    last_donation_date = Column(Date)
    is_available = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())