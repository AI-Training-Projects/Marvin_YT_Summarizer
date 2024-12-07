import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from marvin import ai_fn

load_dotenv()

#load OPENAI_API_KEY from .env file
openai_api_key = os.getenv('MARVIN_OPENAI_API_KEY')

@ai_fn
def summarize_video(text: str) -> str:
    """
    Summarize the provided text
    """

video_url = input("Enter the video url: ")
video_id = video_url.split("watch?v=")[-1]
print("Fetching transcript...")

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
transcript_text = " ".join([entry['text'] for entry in transcript])

print("Summarizing...")
summary = summarize_video(transcript_text)

print("Summary of the video:")
print(summary)

# Examples to try