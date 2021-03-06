from app import app
from flask import jsonify, request
import app.services.events as events_service
import app.services.json_response as json_response


@app.route('/api/v1/events/', methods=['GET'])
def events():
    return jsonify(json_response.build_events(events_service.get_all(request.args)))


@app.route('/api/v1/events/<event_id>', methods=['GET'])
def event(event_id):
    event_item = events_service.get_by_id(event_id)

    if event_item is None:
        result = json_response.build_error()
        status = 404
    else:
        result = json_response.build_event(event_item)
        status = 200

    return jsonify(result), status
