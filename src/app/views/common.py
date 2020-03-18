from app import app
from flask import jsonify, render_template


@app.route('/api/v1')
def api_index():
    return jsonify(status='ok', version='1.0')


@app.route('/')
def index():
    return render_template('docs.html')
