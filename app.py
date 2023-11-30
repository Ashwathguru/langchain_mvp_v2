import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
import os
import sys
import datetime
import openai
import streamlit as st
from audio_recorder_streamlit import audio_recorder
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from gtts import gTTS
import base64
from datetime import datetime
# import API key from .env file
openai.api_key = st.secrets["OPENAI_API_KEY"]

def streamlit_menu():
    selected = option_menu(
        menu_title="IT Service Management",  # required
        options=["Home", "ReportGPT", "WikiGPT"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        },
    )
    return selected

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        st.error(f"Failed to load Lottie animation. Status code: {r.status_code}")
        return None
    try:
        return r.json()
    except ValueError as e:
        st.error(f"Error parsing Lottie JSON: {e}")
        return None

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

def get_answer_csv(query: str) -> str:
    file = "raw.csv"
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    answer = agent.run(query)
    return answer

def transcribe(audio_file):
    transcript = openai.Audio.transcribe("whisper-1", audio_file, language="en")
    return transcript

def save_audio_file(audio_bytes, file_extension):
    """
    Save audio bytes to a file with the specified extension.

    :param audio_bytes: Audio data in bytes
    :param file_extension: The extension of the output audio file
    :return: The name of the saved audio file
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"audio_{timestamp}.{file_extension}"

    with open(file_name, "wb") as f:
        f.write(audio_bytes)

    return file_name

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = transcribe(audio_file)

    return transcript["text"]

def text_to_speech(text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # Format with milliseconds
    filename = f"output_{timestamp}.mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filename)
    st.info(filename)
    # Convert audio data to base64
    audio_base64 = base64.b64encode(open(filename, 'rb').read()).decode('utf-8')
    # Generate a data URI for the audio
    audio_uri = f"data:audio/mp3;base64,{audio_base64}"

    # Display the audio player using HTML and JavaScript
    audio_code = f"""
    <audio autoplay controls>
        <source src="{audio_uri}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """
    st.markdown(audio_code, unsafe_allow_html=True)

def reportsGPT():
    st.title("ReportGPT")
    tab1, tab2 = st.tabs(["Speak", "Chat"])

    # Record Audio tab
    with tab1:
        audio_bytes = audio_recorder()
        if audio_bytes:
            #option to replay audio
            #st.audio(audio_bytes, format="audio/wav")
            save_audio_file(audio_bytes, "mp3")
            audio_file_path = max(
                [f for f in os.listdir(".") if f.startswith("audio")],
                key=os.path.getctime,
            )
            # Transcribe the audio file
            transcript_text = transcribe_audio(audio_file_path)
            # Display the transcript
            st.header("Transcript")
            st.write(transcript_text)
            query=transcript_text
            response=get_answer_csv(query)
            st.write(response)
            text_to_speech(response)
            # Save the transcript to a text file
            with open("response.txt", "w") as f:
                f.write(response)
            # Provide a download button for the transcript
            st.download_button("Download Response", response,key='voice_download')

    #Chat Tab
    with tab2:
        query = st.text_area("Ask any question related to the tickets")
        button = st.button("Submit")
        if button:
            response=get_answer_csv(query)
            st.write(response)
            # Save the transcript to a text file
            with open("response.txt", "w") as f:
                f.write(response)
            # Provide a download button for the transcript
            st.download_button("Download Response", response,key='chat_download')

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
quickparts_logo = Image.open("images/quickparts_logo.JPG")

selected = streamlit_menu()

if selected == "Home":
    st.title(f"You have selected {selected}")
    # Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
    #st.set_page_config(page_title="QuickpartsGPT", page_icon=":tada:", layout="wide")
    # ---- HEADER SECTION ----
    with st.container():
        # Set up the layout using st.beta_columns
        col1, col2, col3 = st.columns([2, 6, 2])
        # Column 1: Logo (Top Left)
        col1.image(quickparts_logo, width=100, caption="")
        # Column 2: Title (Centered)
        with col2:
            st.header("IT Service Management")
            # Add a horizontal line to separate logo, title, and buttons
            st.markdown("<hr>", unsafe_allow_html=True)

        with col3:
            # Use custom HTML and CSS to style the buttons
            st.markdown(
                """
                <div style="display: flex; justify-content: flex-end;">
                    <button style="margin-right: 10px;">Reports</button>
                    <button>Wiki</button>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        # Split into 6 parts (3 on top, 3 on bottom)
        col_top1, col_top2, col_top3 = st.columns(3)
        col_bottom1, col_bottom2, col_bottom3 = st.columns(3)

        # Load an image in each box
        image1 = col_top1.image("images/ticket_status.JPG", use_column_width=True)
        image2 = col_top2.image("images/ticket_priority.JPG", use_column_width=True)
        image3 = col_top3.image("images/category_count.JPG", use_column_width=True)

        image4 = col_bottom1.image("images/ticket_count.JPG", use_column_width=True)
        image5 = col_bottom2.image("images/request_count.JPG", use_column_width=True)

        with col_bottom3:
            # Display the Lottie animation with st_lottie
            st_lottie(lottie_coding, height=300, key="coding")

            # Create a button to open the pop-up when clicked
            if st.button("Click to Open Pop-up", key="popup_button"):
                # Open a pop-up with additional content
                st.write("This is a pop-up!")
if selected == "ReportGPT":
    # Set up the working directory
    working_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(working_dir)
    # Run the main function
    reportsGPT()
if selected == "WikiGPT":
    st.title(f"You have selected {selected}")
