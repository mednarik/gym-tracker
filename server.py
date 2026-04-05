from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/get_attr/<attr>")
def get_attr(attr):
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return str(data[attr])

@app.route("/write_attr", methods=["POST"])
def write_attr():
    body = request.get_json()
    text = body["text"]
    attr = body["attr"]
    
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data[attr] = text
    
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
    return jsonify({"success": True })
    

if __name__ == "__main__":
    app.run(debug=True)