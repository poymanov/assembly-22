from app import app
from flask import jsonify
import app.services.json_response as json_response
import app.services.event_categories as event_categories_service


@app.route('/api/v1/categories', methods=['GET'])
def event_categories():
    return jsonify(json_response.build_event_categories(event_categories_service.get_all()))


@app.route('/api/v1/categories/<category_id>', methods=['GET'])
def event_category(category_id):
    category = event_categories_service.get_by_id(category_id)

    if category is None:
        result = json_response.build_error()
        status = 404
    else:
        result = json_response.build_event_category(category)
        status = 200

    return jsonify(result), status
