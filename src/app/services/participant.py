from app.models import db, Participant
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import string
import random


def create(participant_data, password):
    for item in ['name', 'email', 'location', 'about']:
        if item not in participant_data or len(participant_data[item]) == 0:
            return None

    email = participant_data['email']

    if get_by_email(email) is not None:
        return None

    name = participant_data['name']
    location = participant_data['location']
    about = participant_data['about']

    if password is None:
        password = generate_password(8)

    participant = Participant()
    participant.name = name
    participant.email = email
    participant.location = location
    participant.about = about
    participant.password = generate_password_hash(password)

    db.session.add(participant)
    db.session.commit()

    return participant.id


def login(participant_data):
    for item in ['email', 'password']:
        if item not in participant_data or len(participant_data[item]) == 0:
            return None

    email = participant_data['email']
    password = participant_data['password']

    participant = db.session.query(Participant).filter(Participant.email == email).first()
    if participant and check_password_hash(participant.password, password):
        return participant.id
    else:
        return None


def create_participant_access_token(participant_id):
    return create_access_token(identity=participant_id)


def get_by_id(participant_id):
    return db.session.query(Participant).filter(Participant.id == participant_id).first()


def get_by_email(email):
    return db.session.query(Participant).filter(Participant.email == email).first()


def generate_password(size):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))
