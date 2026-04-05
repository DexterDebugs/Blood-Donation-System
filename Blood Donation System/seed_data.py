#Faker lib used to insert sample test data of our choice

import random
from faker import Faker
from database import SessionLocal, engine
from models import Donor, Base

fake = Faker('en_IN')        # Indian names
cities = ["Delhi", "Mumbai", "Hyderabad", "Bangalore", "Chennai", 
          "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
          "Kanpur", "Nagpur", "Visakhapatnam", "Kochi", "Bhopal",
          "Indore", "Coimbatore", "Chandigarh", "Surat", "Patna"]
blood_type = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

db = SessionLocal()     # ← open once before loop

for i in range(500):
    name = fake.name() # generates a name
    city = random.choice(cities)
    blood_group = random.choice(blood_type)
    phone_number = fake.phone_number()
    ##Creating a donor object
    donor = Donor (
        name = name,
        blood_group = blood_group,
        phone = phone_number,
        city = city,
        is_available = random.random() < 0.8
    )
    db.add(donor)  # add each donor

## addding to the session
# loop here
db.commit()
db.close()