import streamlit as st

def main():
    st.title("Streamlit Chat App")

    # Add a clickable chat icon
    st.markdown(
        """
        <style>
            .chat-icon {
                cursor: pointer;
                font-size: 24px;
                color: #3498db;
            }
        </style>
        """
    , unsafe_allow_html=True)

    if st.button("", key="chat-btn"):
        # If the button is clicked, show the chat pop-up
        st.markdown(
            """
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); display: flex; justify-content: center; align-items: center;">
                <div style="background: #fff; padding: 20px; border-radius: 10px; width: 400px; height: 400px;">
                    <h2>Chat Popup</h2>
                    <textarea style="width: 100%; height: 200px; margin-bottom: 10px;"></textarea>
                    <button onclick="document.getElementById('chat-popup').style.display='none'">Close</button>
                </div>
            </div>
            """
        , unsafe_allow_html=True)

if __name__ == "__main__":
    main()
