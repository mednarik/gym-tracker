from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/get_attr/<attr>")
def get_attr(attr):
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return str(data[attr])

if __name__ == "__main__":
    app.run(debug=True)