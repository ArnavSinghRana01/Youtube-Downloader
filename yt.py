import streamlit as st

# Function to download YouTube video based on the selected option
def download_youtube_video(url, download_type):
    try:
        # Add your logic to retrieve video information and download
        if download_type == 'audio':
            st.success("Audio downloaded successfully!")
        elif download_type == 'highest_resolution':
            st.success("Highest resolution video downloaded successfully!")
        elif download_type == 'lowest_resolution':
            st.success("Lowest resolution video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Set page config
st.set_page_config(page_title="YouTube Video Downloader", page_icon="▶️", layout="wide")

# Sidebar with author information
st.sidebar.title("About Author")
st.sidebar.write("""
Hey, I'm Arnav Singh Rana. I created this website to make it easy for you to download YouTube videos and Audios. 
Feel free to explore and let me know if you have any feedback!
""")

# Contact Us section with emojis
st.sidebar.header("Contact Us 📧")

# GitHub logo with link
github_profile_url = "https://github.com/ArnavSinghRana01"
github_logo = "https://img.icons8.com/ios-glyphs/30/000000/github.png"
st.sidebar.markdown(f"<a href='{github_profile_url}' style='color: #ffffff;'><img src='{github_logo}' style='vertical-align: middle;'> GitHub</a>", unsafe_allow_html=True)

# LinkedIn logo with link
linkedin_profile_url = "https://www.linkedin.com/in/arnav-singh-rana-a76508263"
linkedin_logo = "https://img.icons8.com/ios-glyphs/30/000000/linkedin-circled.png"
st.sidebar.markdown(f"<a href='{linkedin_profile_url}' style='color: #ffffff;'><img src='{linkedin_logo}' style='vertical-align: middle;'> LinkedIn</a>", unsafe_allow_html=True)

# Main content area
st.title("▶️ YouTube Audio & Video Downloader")

# Input box for URL
path = st.text_input('Enter URL of any YouTube video')

# Dropdown for download type
option = st.selectbox('Select type of download', ('audio', 'highest_resolution', 'lowest_resolution'))





# Download button
if st.button("Download"): 
    download_youtube_video(path, option)

# View button
if st.button("View"): 
    # Assuming 'path' is the path to the downloaded video
    st.video(path)
