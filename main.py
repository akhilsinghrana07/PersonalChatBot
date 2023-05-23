import streamlit as st

from backend import Chatbot

import streamlit as st


def main():
    # Set page width and center the content
    st.set_page_config(layout="centered")

    # Apply CSS styles
    st.markdown(
        """
        <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        .user-bubble {
            background-color: #DCF8C6;
            color: #000000;
            padding: 10px 15px;
            border-radius: 10px;
            max-width: 70%;
            align-self: flex-end;
            margin-bottom: 10px;
        }
        .bot-bubble {
            background-color: #F1F0F0;
            color: #000000;
            padding: 10px 15px;
            border-radius: 10px;
            max-width: 70%;
            align-self: flex-start;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Hi! I'm Alex Your Personal Chatbot")
    # Add an image of your chatbot in the sidebar
    st.sidebar.image("https://www.insegment.com/blog/wp-content/uploads/2020/11/chatbot-marketing.gif", use_column_width=True)
    # Add description and additional information
    st.sidebar.markdown("This chatbot was created by Akhil Singh Rana using the OpenAI API.")
    st.sidebar.markdown("It utilizes the OpenAI text-davinci-003 model for generating responses.")
    st.sidebar.markdown("Feel free to ask any questions or have a conversation with the chatbot.")

    chatbot = Chatbot()
    chatbot = Chatbot()

    # Create a container for the chat bubbles
    chat_container = st.container()

    with chat_container:
        # Create a section for the chat bubbles
        st.markdown('<div class="chat-container" id="chat-container"></div>', unsafe_allow_html=True)

    user_input = st.text_input("User Input")

    if st.button("Send"):
        bot_response = chatbot.get_response(user_input)
        add_chat_bubble(user_input, "user-bubble")
        add_chat_bubble(bot_response, "bot-bubble")
        user_input = ""


def add_chat_bubble(content, bubble_class):
    st.markdown(
        f'<div class="{bubble_class}">{content}</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()