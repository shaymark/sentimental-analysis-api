from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from sentimental_model import analyze_sentiment

app = FastAPI()

# Mount static folder to serve the HTML and JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

class TextInput(BaseModel):
    text: str
    
@app.get("/")
async def read_root():
    return {"message": "welcome to the sentiment analysis API"}

@app.post("/analyze-sentiment")
def analyze_sentiment_endpoint(text_input: TextInput):
    result = analyze_sentiment(text_input.text)
    return {"sentiment": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)