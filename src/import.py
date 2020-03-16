from app.models import Location
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import csv

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
session = Session()

locations_data = csv.DictReader(open('import_data/locations.csv'))

for location in locations_data:
    session.add(Location(code=location.get('code'), title=location.get('title')))

session.commit()