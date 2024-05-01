from googleapiclient.discovery import build
from textblob import TextBlob

API_KEY = 'AIzaSyAXGeXxfcAOsPOCg_2wSaUdLYTwHWYCy-I'

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

num_comments = 100

# Video ID of the YouTube video
video_id = 'sLK26nrQg_c'

# Request comments for the video
response = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText',
    maxResults=num_comments,
    order="relevance"
).execute()

print(response)

sentiment_score = 0

# Print the comments
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    print(comment)
    blob = TextBlob(comment)
    sentiment_score += blob.sentiment.polarity

print('Sentiment score: ', sentiment_score)
