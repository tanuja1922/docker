from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/call-a')
def call_a():
    try:
        # container_a is the service name in docker-compose
        response = requests.get("http://container_a:5000/hello")
        return jsonify({"Container A says": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
