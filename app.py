import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="QuickpartsGPT", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
quickparts_logo = Image.open("images/quickparts_logo.JPG")

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
    image6 = col_bottom3.empty()
    image6.lottie(lottie_coding, width=200, height=200)
    
    # Create a button to open the pop-up when the Lottie animation is clicked
    if st.button("Click to Open Pop-up", key="lottie_button"):
        # Open a pop-up with additional content
        st.write("Pop-up Content Goes Here!")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
