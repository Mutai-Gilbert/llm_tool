# Existing API with LLM Tool Integration

This project is a Flask-based API with an integrated LLM tool that uses a pre-trained GPT-2 model to finesse and enhance text prompts. The API accepts a prompt via a POST request and returns a more refined version of the text using the power of large language models (LLMs).

## Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/existing_api.git
    cd existing_api
    ```

### Running the Application with Docker

1. **Build the Docker image**:
    ```bash
    docker-compose build
    ```

2. **Start the application**:
    ```bash
    docker-compose up
    ```

3. The API will be available at `http://localhost:5000/finesse`.

### Usage

Send a POST request to the `/finesse` endpoint with a JSON payload containing your prompt. For example:

```bash
curl -X POST http://localhost:5000/finesse -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'
