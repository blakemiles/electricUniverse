import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import json
import youtube_dl

# Function to get list of video IDs from a channel
def get_video_ids(youtube, channel_id):
    video_ids = []
    request = youtube.search().list(part="id", channelId=channel_id, maxResults=50, type="video")
    
    while request is not None:
        response = request.execute()
        video_ids += [item['id']['videoId'] for item in response['items']]
        request = youtube.search().list_next(request, response)

    return video_ids

# Function to download the transcript and save it to a file
def download_transcripts(video_ids, output_dir):
    for video_id in video_ids:
        try:
            # Retrieve the available transcripts
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
            # Save the transcript as a json file
            with open(os.path.join(output_dir, f'{video_id}.json'), 'w', encoding='utf-8') as file:
                json.dump(transcript, file, ensure_ascii=False, indent=4)
            
            print(f"Downloaded transcript for video ID: {video_id}")
        except (TranscriptsDisabled, NoTranscriptFound):
            print(f"Transcript not available for video ID: {video_id}")

# Your Google API key
api_key = 'AIzaSyBKVzoAJmjkMQUUud0BgYb6yDS4AaEh-N8'

# The YouTube channel ID you want to scrape
channel_id = 'UCvHqXK_Hz79tjqRosK4tWYA'

# Path to directory where you want to save transcripts
output_directory = 'Users/blakemiles/electricUniverse'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set up the YouTube API client
from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)

# Get list of video IDs from the channel
video_ids = get_video_ids(youtube, channel_id)

# Download the transcripts
download_transcripts(video_ids, output_directory)