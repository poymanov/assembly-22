from app import app
from flask import jsonify
import app.services.json_response as json_response
import app.services.event_types as event_types_service


@app.route('/api/v1/types', methods=['GET'])
def event_types():
    return jsonify(json_response.build_event_types(event_types_service.get_all()))


@app.route('/api/v1/types/<type_id>', methods=['GET'])
def event_type(type_id):
    event_type_item = event_types_service.get_by_id(type_id)

    if event_type_item is None:
        result = json_response.build_error()
        status = 404
    else:
        result = json_response.build_event_type(event_type_item)
        status = 200

    return jsonify(result), status
