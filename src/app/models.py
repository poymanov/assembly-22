from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

events_categories_association = db.Table('events_categories',
                                         db.Column('event_id', db.Integer, db.ForeignKey('events.id')),
                                         db.Column('category_id', db.Integer, db.ForeignKey('event_categories.id'))
                                         )
events_locations_association = db.Table('events_locations',
                                        db.Column('event_id', db.Integer, db.ForeignKey('events.id')),
                                        db.Column('location_id', db.Integer, db.ForeignKey('locations.id'))
                                        )


class Participant(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(255))
    location = db.Column(db.String(255), nullable=False)
    about = db.Column(db.String(255), nullable=False)


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)

    events = db.relationship(
        'Event', secondary=events_locations_association, back_populates='locations'
    )


class EventType(db.Model):
    __tablename__ = 'event_types'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)

    events = db.relationship('Event', back_populates='type')


class EventCategory(db.Model):
    __tablename__ = 'event_categories'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)

    events = db.relationship(
        'Event', secondary=events_categories_association, back_populates='categories'
    )


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255))
    type_id = db.Column(db.Integer, db.ForeignKey('event_types.id'), nullable=False)

    type = db.relationship('EventType', uselist=False, back_populates='events')

    categories = db.relationship(
        'EventCategory', secondary=events_categories_association, back_populates='events'
    )

    locations = db.relationship(
        'Location', secondary=events_locations_association, back_populates='events'
    )
