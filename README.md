# Video Summary Generator

This Python script allows users to generate a summary of any YouTube video 
by providing the video's URL. The summary is generated using an AI model, 
and the transcript of the video is fetched using the youtube_transcript_api.

# REVISIONS: 
    Original:
    Updater: Rich Lysakowski
    Updated: 2024.12.06
    Updates: Added write to files functions to save outputs 
    TBD: 
        TODO: Capture key `YT Video Profile` metadata [see New_Features_WIP folder for ]

# Prerequisites

To run this script, you need the following libraries installed:

    os
    dotenv
    youtube_transcript_api
    marvin

Additionally, an API key for OpenAI is required. This key should be stored 
in a .env file under the variable name MARVIN_OPENAI_API_KEY.

You can find out more information about Marvin.AI here: 
    - https://www.askmarvin.ai/welcome/installation/

You can learn more about `youtube-transcript-api` here: 
    - https://github.com/jdepoix/youtube-transcript-api

## How to Use

Ensure that you have a .env file in your project directory with the 
OpenAI API key stored as MARVIN_OPENAI_API_KEY.

Run the script using a Python interpreter.

When prompted, enter the URL of the YouTube video you want to 
summarize.

The script will fetch the transcript of the video and process it.

The summary of the video will be displayed on the screen.
