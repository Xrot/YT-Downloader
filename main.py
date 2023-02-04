import os
from pytube import YouTube

def download_video(url):
    # Create a YouTube object from the given URL
    yt = YouTube(url)

    # Find the highest available video quality in .webm format
    best_video_quality = 0
    best_video_stream = None
    for stream in yt.streams.filter(mime_type="video/webm"):
        if int(stream.resolution.strip('p')) > best_video_quality:
            best_video_quality = int(stream.resolution.strip('p'))
            best_video_stream = stream

    # Find the highest available audio quality in .webm format
    best_audio_quality = 0
    best_audio_stream = None
    for stream in yt.streams.filter(mime_type="audio/webm"):
        if int(stream.abr.strip('kbps')) > best_audio_quality:
            best_audio_quality = int(stream.abr.strip('kbps'))
            best_audio_stream = stream

    # Download the video and audio in the best quality
    default_download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    if best_video_stream:
        best_video_stream.download(default_download_dir, filename=f"{yt.title} (Video).{best_video_stream.subtype}")
    else:
        print("No suitable video stream found.")

    if best_audio_stream:
        best_audio_stream.download(default_download_dir, filename=f"{yt.title} (Audio).{best_audio_stream.subtype}")
    else:
        print("No suitable audio stream found.")

# Prompt the user to enter the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Call the download_video function with the given URL
download_video(url)