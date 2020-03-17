from app.models import db, EventType


def get_all():
    return db.session.query(EventType).all()


def get_by_id(type_id):
    return db.session.query(EventType).get(type_id)
