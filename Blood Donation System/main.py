##Actual heart of the backend - main.py
'''
1.Creates the FastAPI app → starts the server that listens for requests
2.Defines routes → like /donors/search — what happens when Streamlit calls that URL
3.Queries the database → using the session from database.py and the model from models.py
'''

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db     ##database file nunchi get_db function theesko
from models import Donor        ##models file nunchi tables thechko
from pydantic import BaseModel  ##creates a form template - tells FastAPI exactly what to expect (receive) 
from typing import Optional

app = FastAPI()         ##Creates your application, like switching the server on
@app.get("/donors/search")       ##decorator - it tells FastAPI "when someone calls this URL, run the function below it"

##without depends, we have to manually open and close a session in every function

def search_donors(blood_group: str, city: str = None, name: str = None, db: Session = Depends(get_db)):##parameters
    ##It's telling FastAPI:
    ##"Before running this function, first run get_db() and inject whatever it returns as db"

    query = db.query(Donor)     ##Goes to the donor table

    query = query.filter(Donor.blood_group == blood_group)      ##Same as SQL WHERE
    query = query.filter(Donor.is_available == True)

    if city:        ##Only filter by city if user actually typed one (it's optional)
        query = query.filter(Donor.city.ilike(f"%{city}%"))        

    if name:
        query = query.filter(Donor.name.ilike(f"%{name}%"))     ##Case insensitive name search

    results = query.limit(15).all()     ##Maximum 15 results, return them all
    return results
    
##Post request -- adding registration forms to add donors

class DonorCreate(BaseModel):
    name: str
    blood_group: str
    phone: str
    city: str
    is_available: bool
    last_donation_date: Optional[str] = None

@app.post("/donors/register")

def register_donor(donor: DonorCreate, db: Session = Depends(get_db)):
    ##Create new donor
    new_donor = Donor(name = donor.name, blood_group = donor.blood_group, phone = donor.phone, city = donor.city, is_available =  donor.is_available, last_donation_date = donor.last_donation_date)
    ##add and commit changes
    db.add(new_donor)
    db.commit()
    db.refresh(new_donor)
    ## return the object
    return new_donor