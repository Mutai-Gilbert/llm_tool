# LLM Tool: Finesse Your Prompts with AI

This project is a Flask-based API that uses a pre-trained GPT-2 model to finesse and enhance text prompts. The API accepts a prompt via a POST request and returns a more refined version of the text using the power of large language models (LLMs).

## Features

- **Prompt Finessing**: Enhance your text prompts using a pre-trained GPT-2 model.
- **Easy Integration**: Simple REST API for seamless integration with other applications.
- **Scalable**: Can be deployed on various platforms such as AWS, GCP, or Heroku.

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. You'll also need `pip` to install the required packages.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Mutai-Gilbert/llm_tool.git
    cd llm_tool
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application**:
    ```bash
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000/finesse`.

### Usage

Send a POST request to the `/finesse` endpoint with a JSON payload containing your prompt. For example:

```bash
curl -X POST http://127.0.0.1:5000/finesse -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'
