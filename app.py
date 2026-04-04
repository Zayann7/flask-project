import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask App"

@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)