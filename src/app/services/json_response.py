from app.schemas import ParticipantSchema, LocationSchema, EventSchema, EventTypeSchema, EventCategorySchema


def build_new_participant(participant, participant_password):
    response = build_participant(participant)
    response['password'] = participant_password

    return response


def build_participant(participant):
    return ParticipantSchema().dump(participant)


def build_auth_participant(participant, access_token):
    response = build_participant(participant)
    response['access_token'] = access_token

    return response


def build_locations(locations):
    return LocationSchema(many=True).dump(locations)


def build_location(location):
    return LocationSchema().dump(location)


def build_events(events):
    return EventSchema(many=True).dump(events)


def build_event(event):
    return EventSchema().dump(event)


def build_event_types(event_types):
    return EventTypeSchema(many=True).dump(event_types)


def build_event_type(event_type):
    return EventTypeSchema().dump(event_type)


def build_event_categories(event_categories):
    return EventCategorySchema(many=True).dump(event_categories)


def build_event_category(event_category):
    return EventCategorySchema().dump(event_category)


def build_error():
    return dict(status='error')


def build_success():
    return dict(status='success')
