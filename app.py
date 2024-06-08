from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def finesse_prompt(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    finessed_prompt = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return finessed_prompt

@app.route('/finesse', methods=['POST'])
def finesse():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    finessed_prompt = finesse_prompt(prompt)
    return jsonify({"finessed_prompt": finessed_prompt})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
