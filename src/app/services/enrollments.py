from app.models import db, Enrollment
import app.services.events as events_service
import app.services.participant as participants_service
import datetime


def add_participant(event_id, participant_id):
    event = events_service.get_by_id(event_id)

    if event is None or len(event.participants) >= event.seats:
        return False

    participant = participants_service.get_by_id(participant_id)

    if participant is None:
        return False

    existed_enrollment = get_by_event_id_and_participant_id(event_id, participant_id)

    if existed_enrollment is not None:
        return False

    enrollment = Enrollment(event_id=event_id, participant_id=participant_id,
                            timestamp=datetime.datetime.now())

    db.session.add(enrollment)
    db.session.commit()

    return True


def delete_participant(event_id, participant_id):
    event = events_service.get_by_id(event_id)

    if event is None or len(event.participants) >= event.seats:
        return False

    participant = participants_service.get_by_id(participant_id)

    if participant is None:
        return False

    existed_enrollment = get_by_event_id_and_participant_id(event_id, participant_id)

    if existed_enrollment is None:
        return False

    db.session.delete(existed_enrollment)
    db.session.commit()

    return True


def get_by_event_id_and_participant_id(event_id, participant_id):
    return db.session.query(Enrollment).filter(Enrollment.event_id == event_id,
                                               Enrollment.participant_id == participant_id).first()
