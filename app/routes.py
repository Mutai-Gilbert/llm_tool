from flask import Flask, request, jsonify
from .llm_tool import finesse_prompt

app = Flask(__name__)

@app.route('/finesse', methods=['POST'])
def finesse():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    finessed_prompt = finesse_prompt(prompt)
    return jsonify({"finessed_prompt": finessed_prompt})

# Existing routes
# @app.route('/existing_endpoint', methods=['GET'])
# def existing_endpoint():
#     ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
