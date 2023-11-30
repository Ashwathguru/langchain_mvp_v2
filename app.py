import streamlit as st

def main():
    st.title("Streamlit Chat App")

    # Add a clickable chat symbol in the bottom right corner
    st.markdown(
        """
        <style>
            .chat-btn {
                position: fixed;
                bottom: 20px;
                right: 20px;
                cursor: pointer;
                font-size: 24px;
                color: #3498db;
                background-color: #fff;
                border: 2px solid #3498db;
                border-radius: 50%;
                padding: 10px;
            }
        </style>
        """
    , unsafe_allow_html=True)

    st.markdown(
        """
        <div class="chat-btn" id="chat-btn">&#x1F4AC;</div>
        """
    , unsafe_allow_html=True)

    # Use JavaScript to handle the chat symbol click event and open the pop-up
    st.markdown(
        """
        <script>
            document.getElementById("chat-btn").addEventListener("click", function() {
                // Open a full-screen pop-up
                const popup = window.open("", "ChatPopup", "width=100%,height=100%");
                popup.document.write(`
                    <div style="text-align: center; padding: 20px;">
                        <h2>Chat Popup</h2>
                        <p>This is your chat popup content.</p>
                        <button onclick="window.close()">Close</button>
                    </div>
                `);
            });
        </script>
        """
    , unsafe_allow_html=True)

if __name__ == "__main__":
    main()
