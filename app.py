from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 This allows requests from your frontend (localhost)

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    # ... do your PDF processing ...
    return jsonify({"education": "...", "work_experience": "..."})
