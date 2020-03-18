from app import app
from flask import jsonify
import app.services.json_response as json_response
import app.services.location as locations_service


@app.route('/api/v1/locations', methods=['GET'])
def locations():
    return jsonify(json_response.build_locations(locations_service.get_all()))


@app.route('/api/v1/locations/<location_id>', methods=['GET'])
def location(location_id):
    location_item = locations_service.get_by_id(location_id)

    if location_item is None:
        result = json_response.build_error()
        status = 404
    else:
        result = json_response.build_location(location_item)
        status = 200

    return jsonify(result), status
