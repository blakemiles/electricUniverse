from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re

# Function to extract video ID from URL
def get_video_id_from_url(url):
    # Regular expression to find the YouTube video ID
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)
    return None

# Prompt the user for a YouTube URL
url_input = input("Enter the YouTube URL: ")

# Extract the video ID from the URL
video_id = get_video_id_from_url(url_input)

if not video_id:
    print("Invalid YouTube URL. Please ensure it's correct and try again.")
else:
    try:
        # Retrieve the available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Select the desired transcript
        transcript = transcript_list.find_transcript(['en'])  # Assuming you want English transcripts

        # Fetch the transcript
        transcript = transcript.fetch()

        # Initialize the formatter
        formatter = TextFormatter()

        # Format the transcript as text
        text_transcript = formatter.format_transcript(transcript)

        # Output the transcript to a text file
        with open(f"{video_id}_transcript.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text_transcript)

        print(f"The transcript for video ID {video_id} has been saved to {video_id}_transcript.txt")

    except Exception as e:
        print(f"An error occurred: {e}")