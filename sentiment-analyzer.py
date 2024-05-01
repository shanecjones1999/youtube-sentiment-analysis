from textblob import TextBlob

text = "I am so happy!"
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity
print("Sentiment Score:", sentiment_score)