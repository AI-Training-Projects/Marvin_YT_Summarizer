"""
Extract the YouTube video title using the YouTube Data API.
Fetch the transcript and summarize it using Marvin.ai.
Write the title, summary, and full transcript to a Markdown file 
named {video_title}_transcript_summary_{datetime}.md in the current project folder.

SETUP: 
- Enter your YouTube Data API (as YOUTUBE_API_KEY) and OPENAI_API_KEY set in the .env file.

    https://github.com/jdepoix/youtube-transcript-api

# Install the required packages:
- pip install youtube_transcript_api marvin
"""

import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from marvin import ai_fn
from datetime import datetime
import requests

load_dotenv()

# Load OPENAI_API_KEY from .env file
openai_api_key = os.getenv("MARVIN_OPENAI_API_KEY")

@ai_fn
def summarize_video(text: str) -> str:
    """
    Summarize the provided text
    """

def get_video_title(video_id: str) -> str:
    """
    Get the title of the YouTube video using the YouTube Data API.
    """
    api_key = os.getenv("YOUTUBE_API_KEY")
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet"
    response = requests.get(url)
    data = response.json()
    return data["items"][0]["snippet"]["title"]

video_url = input("Enter the video URL: ")
video_id = video_url.split("watch?v=")[-1]

print("Fetching video title...")
video_title = get_video_title(video_id)

print("Fetching transcript...")
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
transcript_text = " ".join([entry["text"] for entry in transcript])

print("Summarizing...")
summary = summarize_video(transcript_text)

print("Summary of the video:")
print(summary)

# Write the title, summary, and full transcript to a Markdown file
current_datetime = datetime.now().strftime("%Y%m%d_%H%M")
markdown_filename = f"{video_title}_transcript_summary_{current_datetime}.md"

with open(markdown_filename, "w", encoding="utf-8") as md_file:
    md_file.write(f"# {video_title}\n\n")
    md_file.write(f"## Summary\n\n{summary}\n\n")
    md_file.write("## Full Transcript\n\n")
    md_file.write(transcript_text)

print(f"Markdown file '{markdown_filename}' has been created.")

# Generated by Rich Lysakowski