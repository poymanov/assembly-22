from app import app
from flask import jsonify


@app.route('/api/v1/')
def index():
    return jsonify(status='ok')
