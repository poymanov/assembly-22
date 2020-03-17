from app.models import db, Event, Location


def get_all(params):
    query = db.session.query(Event)

    for param in params:
        if param not in ['type_id', 'location_id']:
            return []

    if 'type_id' in params.keys():
        query = query.filter(Event.type_id == params['type_id'])

    if 'location_id' in params.keys():
        query = query.filter(Event.locations.any(Location.id == params['location_id']))

    return query.all()


def get_by_id(event_id):
    return db.session.query(Event).get(int(event_id))
