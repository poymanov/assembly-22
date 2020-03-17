from app.models import Location, EventType, EventCategory, Event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import csv
import datetime

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
session = Session()

locations_data = csv.DictReader(open('import_data/locations.csv'))
event_types_data = csv.DictReader(open('import_data/event_types.csv'))
event_categories_data = csv.DictReader(open('import_data/event_categories.csv'))
events_data = csv.DictReader(open('import_data/events.csv'))

for location in locations_data:
    session.add(Location(code=location.get('code'), title=location.get('title')))

session.commit()

for event_type in event_types_data:
    session.add(EventType(code=event_type.get('code'), title=event_type.get('title')))

session.commit()

for event_category in event_categories_data:
    session.add(EventCategory(code=event_category.get('code'), title=event_category.get('title')))

session.commit()

for event_item in events_data:
    event_type = session.query(EventType).filter(EventType.code == event_item.get('type')).first()

    locations_list = event_item.get('location').split(', ')
    locations = session.query(Location).filter(Location.code.in_(locations_list)).all()

    categories_list = event_item.get('category').split(', ')
    categories = session.query(EventCategory).filter(EventCategory.code.in_(categories_list)).all()

    date_time_template = '{} {}'.format(event_item.get('date'), event_item.get('time'))
    date_time = datetime.datetime.strptime(date_time_template, '%d.%m.%Y %H:%M')

    event = Event()
    event.title = event_item.get('title')
    event.description = event_item.get('description')
    event.date = date_time.date()
    event.time = date_time.time()
    event.address = event_item.get('address')
    event.seats = event_item.get('seats')
    event.type = event_type
    event.locations = locations
    event.categories = categories

    session.add(event)

session.commit()
