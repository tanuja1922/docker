from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Container B!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # expose to container network
