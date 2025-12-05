# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage, AIMessage
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# # --------------------------
# # SET YOUR GOOGLE API KEY
# # --------------------------
# # os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"

# # --------------------------
# # LOAD MODEL
# # --------------------------
# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",  # use gemini-1.5-pro if upgraded
#     temperature=0.7
# )

# # --------------------------
# # STREAMLIT UI
# # --------------------------
# st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
# st.title("🤖 Gemini Powered ChatGPT App")

# # initialize session state for chat history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # Display chat messages
# for msg in st.session_state.history:
#     if isinstance(msg, HumanMessage):
#         st.chat_message("user").markdown(msg.content)
#     else:
#         st.chat_message("assistant").markdown(msg.content)

# # Chat input box
# user_input = st.chat_input("Ask me anything...")

# if user_input:
#     # add user message
#     human_msg = HumanMessage(user_input)
#     st.session_state.history.append(human_msg)
#     st.chat_message("user").markdown(user_input)

#     # get model response
#     resp = model.invoke(st.session_state.history)
#     ai_msg = AIMessage(resp.content)

#     # add bot reply
#     st.session_state.history.append(ai_msg)
#     st.chat_message("assistant").markdown(resp.content)

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from gtts import gTTS
import tempfile
from dotenv import load_dotenv

load_dotenv()

# LOAD MODEL
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

st.set_page_config(page_title="Gemini Chatbot 🔊", page_icon="🤖")
st.title("🤖 Gemini Chatbot with Voice Output 🔊")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat
for msg in st.session_state.history:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    st.chat_message(role).markdown(msg.content)

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    user_msg = HumanMessage(user_input)
    st.session_state.history.append(user_msg)
    st.chat_message("user").markdown(user_input)

    # Gemini response
    resp = model.invoke(st.session_state.history)
    bot_reply = resp.content
    bot_msg = AIMessage(bot_reply)
    st.session_state.history.append(bot_msg)

    # Show text
    st.chat_message("assistant").markdown(bot_reply)

    # Convert to speech
    tts = gTTS(bot_reply, lang="en")

    # Save temp audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        audio_path = fp.name
        tts.save(audio_path)

    # Play audio in Streamlit
    st.audio(audio_path, format="audio/mp3")

