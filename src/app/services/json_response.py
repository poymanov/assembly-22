from app.schemas import ParticipantSchema, LocationSchema


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


def build_error():
    return dict(status='error')
