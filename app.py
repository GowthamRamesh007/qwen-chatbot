import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
import re  # 🧼 For cleaning <think> tags
import os

# Set Streamlit page config
st.set_page_config(page_title="Chatbot", layout="centered")
st.title("💬 Chatbot powered by Qwen")

# ✅ Set environment variables from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_BASE_URL"] = st.secrets["OPENAI_BASE_URL"]

# Initialize session state for storing the conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the model
@st.cache_resource(show_spinner=False)
def get_model():
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key or not base_url:
        raise ValueError("OPENAI_API_KEY or OPENAI_BASE_URL is missing")

    return ChatOpenAI(
        model="qwen/qwq-32b:free",
        temperature=0.0,
        streaming=True,
        api_key=api_key,
        base_url=base_url,
    )

model = get_model()

# Chat input
user_input = st.chat_input("Type your message...")
if user_input:
    # Display user message
    st.chat_message("user").write(user_input)

    # Store user message
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Display assistant message area
    with st.chat_message("assistant"):
        response_text = st.empty()
        full_response = ""

        try:
            # Stream and collect the response
            for chunk in model.stream(st.session_state.messages):
                full_response += chunk.content or ""

            # 🧼 Clean out <think>...</think> tags
            full_response = re.sub(r"<think>.*?</think>", "", full_response, flags=re.DOTALL)

            # Display cleaned response
            response_text.markdown(full_response.strip())
        except Exception as e:
            st.error(f"Error: {e}")

        # Store assistant response (cleaned)
        st.session_state.messages.append(HumanMessage(content=full_response.strip()))
