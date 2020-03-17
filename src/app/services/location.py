from app.models import db, Location


def get_all():
    return db.session.query(Location).all()


def get_by_id(location_id):
    return db.session.query(Location).get(location_id)
