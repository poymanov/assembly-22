from app.models import db, Location


def get_all():
    return db.session.query(Location).all()
