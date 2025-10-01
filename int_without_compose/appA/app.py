from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/call-b', methods=['GET'])
def call_b():
    try:
        # call Container B using its container name
        response = requests.get("http://containerB:5000/hello")
        return jsonify({"Container B says": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # different port
