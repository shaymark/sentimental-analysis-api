from textblob import TextBlob

def analyze_sentiment(text) -> dict:
    """
    Analyze sentiment using TextBlob
    Returns sentiment polarity (-1 to 1) and subjectivity (0 to 1)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Convert polarity to label
    if polarity > 0:
        label = "POSITIVE"
    elif polarity < 0:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    
    # Convert polarity to score (0 to 1 scale)
    score = abs(polarity)
    
    return {"label": label, "score": round(score, 4)}

    