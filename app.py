import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Enable CORS so the frontend (which might be hosted elsewhere) can make requests to this backend
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/chat', methods=['POST'])
def chat():
    if not GROQ_API_KEY or GROQ_API_KEY == "YOUR_GROQ_API_KEY_HERE":
        return jsonify({"error": "Groq API key is not configured on the server."}), 500

    data = request.json
    if not data or 'messages' not in data:
        return jsonify({"error": "Invalid request. 'messages' is required."}), 400

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": data['messages'],
        "temperature": 0.5,
        "max_tokens": 150
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to connect to Groq API: {str(e)}"}), 502

if __name__ == '__main__':
    # Run the app locally on port 5000
    app.run(debug=True, port=5000)
