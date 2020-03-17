from app import app
from flask import jsonify, request
import app.services.participant as participants_service
import app.services.json_response as json_response


@app.route('/api/v1/register', methods=['POST'])
def register():
    participant_password = participants_service.generate_password(8)
    participant_id = participants_service.create(request.args, participant_password)

    if participant_id is None:
        result = json_response.build_error()
    else:
        participant = participants_service.get_by_id(participant_id)
        result = json_response.build_new_participant(participant, participant_password)

    return jsonify(result)


@app.route('/api/v1/login', methods=['POST'])
def login():
    participant_id = participants_service.login(request.args)

    if participant_id is None:
        result = json_response.build_error()
    else:
        participant = participants_service.get_by_id(participant_id)
        access_token = participants_service.create_participant_access_token(participant_id)
        result = json_response.build_auth_participant(participant, access_token)

    return jsonify(result)


@app.route('/api/v1/profile/<participant_id>', methods=['GET'])
def profile(participant_id):
    participant = participants_service.get_by_id(participant_id)

    if participant is None:
        result = json_response.build_error()
    else:
        result = json_response.build_participant(participant)

    return jsonify(result)
