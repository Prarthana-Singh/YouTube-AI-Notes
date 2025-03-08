
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi #Used to fetch the transcript of a YouTube video.
from urllib.parse import urlparse, parse_qs #Used to extract the video ID from a YouTube URL.
import time

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page Configuration
st.set_page_config(page_title="YouTube AI Notes", page_icon="📄", layout="wide")

# Sidebar
with st.sidebar:
    st.title("📌 Menu")
    st.subheader("🎯 How It Works")
    st.markdown("""
    1. **Copy the YouTube Video Link** (Right-click & select 'Copy link')
    2. **Paste the link & click 'Generate AI Notes'**
    3. **AI extracts the transcript** 🎥
    4. **Generates concise, structured notes**📄
    """)

    # st.subheader("🔗 Why Copy Link Address?")
    # st.markdown("""
    # - **Pasting the URL directly from the address bar might not work.**
    # - **Why?** Because YouTube URLs contain extra parameters (like playlists or timestamps) that can break the extraction process.
    # - **Solution?** Always **right-click the video & select 'Copy link address'** before pasting. ✅
    # """)

    st.subheader("👩‍💻 About the Creator")
    st.markdown("""
    **Prarthana** – AI Enthusiast & Data Scientist in the making.  
    - Follow me on [GitHub](https://github.com/Prarthana-Singh)  
    - Connect on [LinkedIn](https://linkedin.com/in/prarthanasingh)
    """)

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #FFFFFF;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #F4D03F;
        }
        .stTextInput>div>div>input {
            background-color: #1E1E1E;
            color: #FFFFFF;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #F4D03F;
            color: black;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #FFD700;
        }
        .summary-card {
            background-color: #1E1E1E;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #AAAAAA;
        }
    </style>
""", unsafe_allow_html=True)


# Extract Video ID from YouTube URL
# def extract_video_id(youtube_url):
#     parsed_url = urlparse(youtube_url) # ParseResult(scheme='https', netloc='www.youtube.com', path='/watch', params='', query='v=O0GNrvO7wD0', fragment='')
#     video_id = parse_qs(parsed_url.query).get("v")
#     return video_id[0] if video_id else None


def extract_video_id(video_url):
    parsed_url = urlparse(video_url)  # URL ko parse karna
    query_params = parse_qs(parsed_url.query)  # Query parameters extract karna

    # ✅ Try to get video ID from "v"
    video_id = query_params.get("v", [None])[0]

    # ✅ If "v" is not found, check for "si" (shortened URL case)
    if not video_id and "youtu.be" in parsed_url.netloc:
        video_id = parsed_url.path.lstrip("/")  # Remove leading "/"

    return video_id


# Fetch YouTube Transcript
def extract_transcript_details(video_id):
    try:
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([i["text"] for i in transcript_text])
    except Exception:
        return None




# Generate Summary with Gemini AI
def generate_gemini_content(transcript_text):
    prompt = """You are an AI-based YouTube video summarizer. 
    Extract key points from the transcript and summarize the video into concise, structured notes within 250 words. Here is the transcript:\n"""

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt + transcript_text)
    return response.text


# UI Layout
st.markdown("<div class='title'>YouTube AI Notes Converter</div>", unsafe_allow_html=True)
st.markdown("🎥 **Convert YouTube Videos into AI-generated Notes!**")

# Copy Link Address Warning
st.warning("⚠️ **Important:** Always 'Copy Link' from YouTube before pasting!")

youtube_link = st.text_input("📌 Enter YouTube Video Link:")

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",  use_column_width=True)
    else:
        st.error("⚠️ Invalid YouTube link! Please enter a correct URL.")

# Button to Generate Notes
if st.button("✨ Generate AI Notes"):
    if not youtube_link:
        st.warning("🔴 Please enter a valid YouTube link.")
    elif not video_id:
        st.error("⚠️ Could not extract video ID. Please check the URL.")
    else:
        with st.spinner("🔄 Fetching transcript and generating notes..."):
            time.sleep(2)
            transcript_text = extract_transcript_details(video_id)

        if not transcript_text:
            st.error("❌ Transcripts are disabled for this video.")
        else:
            with st.spinner("✨ AI is summarizing the video..."):
                time.sleep(2)
                summary = generate_gemini_content(transcript_text)

            st.markdown("<div class='summary-card'><h2>📑 AI-Generated Notes:</h2>", unsafe_allow_html=True)
            st.write(summary)
            st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>✨ Made with ❤️ by Prarthana ✨</div>", unsafe_allow_html=True)
