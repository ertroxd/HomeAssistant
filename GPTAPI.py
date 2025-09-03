from flask import Flask, request, jsonify
from gpt4all import GPT4All
import os
# Pfad zu deinem Modell
MODEL_PATH = os.path.expanduser("~/models/ggml-gpt4all-j-v1.3-groovy.bin")

# Initialisiere das Modell
model = GPT4All(MODEL_PATH)

# Starte die Flask-App
app = Flask(__name__)

@app.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    
    if not user_prompt:
        return jsonify({"error": "Kein Prompt übergeben"}), 400

    response = model.chat(user_prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
