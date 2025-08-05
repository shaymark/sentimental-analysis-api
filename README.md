# Sentiment Analysis API

A FastAPI-based sentiment analysis service that uses the DistilBERT model to analyze the sentiment of text input.

## Features

- RESTful API for sentiment analysis
- Uses Hugging Face Transformers with DistilBERT model
- Returns sentiment label and confidence score
- Deployed on Render

## API Endpoints

### GET /
Returns a welcome message

### POST /analyze-sentiment
Analyzes the sentiment of provided text.

**Request Body:**
```json
{
  "text": "I love this movie!"
}
```

**Response:**
```json
{
  "sentiment": {
    "label": "POSITIVE",
    "score": 0.9876
  }
}
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. The API will be available at `http://localhost:8000`

## Deployment

This application is configured for deployment on Render using the `render.yaml` configuration file. 