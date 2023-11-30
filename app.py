import streamlit as st

def main():
    st.title("Streamlit Chat App with Images")

    # Load and display 4 images in a 2x2 grid on the landing page
    image1 = st.image("image.png", caption="Image 1", use_column_width=True)
    image2 = st.image("image.png", caption="Image 2", use_column_width=True)

    col1, col2 = st.beta_columns(2)
    image3 = col1.image("image.png", caption="Image 3", use_column_width=True)
    image4 = col2.image("image.png", caption="Image 4", use_column_width=True)

    # Add a clickable chat icon in the bottom right corner
    st.markdown(
        """
        <style>
            .chat-icon {
                cursor: pointer;
                font-size: 24px;
                color: #3498db;
                position: fixed;
                bottom: 20px;
                right: 20px;
            }
        </style>
        """
    , unsafe_allow_html=True)

    if st.button("💬", key="chat-btn", class_="chat-icon"):
        # If the button is clicked, show the chat pop-up
        st.markdown(
            """
            <div id="chat-popup" style="position: fixed; bottom: 0; right: 0; padding: 20px; width: 400px; height: 400px; background: #fff; border-top-left-radius: 10px;">
                <h2>Chat Popup</h2>
                <textarea style="width: 100%; height: 200px; margin-bottom: 10px;"></textarea>
                <button onclick="document.getElementById('chat-popup').style.display='none'">Close</button>
            </div>
            <script>
                document.getElementById("chat-popup").addEventListener("click", function(event) {
                    event.stopPropagation();
                });
            </script>
            """
        , unsafe_allow_html=True)

if __name__ == "__main__":
    main()
