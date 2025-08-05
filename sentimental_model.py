from transformers import pipeline

# load the model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text) -> dict:
    result = sentiment_pipeline(text)[0]
    return {"label": result["label"], "score": round(result["score"], 4)}

    