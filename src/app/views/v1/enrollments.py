from app import app
from flask import jsonify
import app.services.enrollments as enrollments_service
from flask_jwt_extended import jwt_required, get_jwt_identity
import app.services.json_response as json_response


@app.route('/api/v1/enrollments/<event_id>', methods=['POST'])
@jwt_required
def add_participant(event_id):
    if enrollments_service.add_participant(event_id, get_jwt_identity()):
        result = json_response.build_success()
    else:
        result = json_response.build_error()

    return jsonify(result)


@app.route('/api/v1/enrollments/<event_id>', methods=['DELETE'])
@jwt_required
def delete_participant(event_id):
    if enrollments_service.delete_participant(event_id, get_jwt_identity()):
        result = json_response.build_success()
    else:
        result = json_response.build_error()

    return jsonify(result)