from app.models import db, EventCategory


def get_all():
    return db.session.query(EventCategory).all()


def get_by_id(type_id):
    return db.session.query(EventCategory).get(type_id)