from transformers import pipeline

def sentiment_analysis(text):
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_pipeline(text)
    print(f"Sentiment: {result[0]}")