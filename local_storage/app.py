import os
from flask import Flask, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = '/app/data'  # Container folder mapped to local storage
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Hello from Flask in Docker!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)
    return jsonify({"message": "File saved!", "path": save_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
