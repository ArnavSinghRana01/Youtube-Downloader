import streamlit as st
from pytube import YouTube

# Function to download YouTube audio and show progress
def download_youtube_audio(url):
    try:
        st.info("Fetching video information...")
        yt = YouTube(url)

        # Fetch the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download audio
        st.info("Downloading audio...")
        audio_file_path = "downloaded_audio.mp3"
        audio_stream.download(output_path=".", filename="downloaded_audio")
        st.success("Audio downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Set page config
st.set_page_config(page_title="YouTube Audio Downloader", page_icon="🎵", layout="wide")

# Main content area
st.title("🎧 YouTube Audio Downloader")

# Input box for URL
url = st.text_input('Enter URL of any YouTube video')

# Download button
if st.button("Download Audio"):
    download_youtube_audio(url)
