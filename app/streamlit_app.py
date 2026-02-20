import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- CONFIGURATION ---
# Make sure FastAPI is running on port 8000
BACKEND_URL = os.getenv("BASE_URL") + "/chat"

st.set_page_config(page_title="Tech-Support AI", page_icon="🤖", layout="centered")

# --- UI STYLING ---
st.title("🤖 Tech-Support Ticketing System")
st.markdown("""
Welcome! I am your automated assistant. My name is TechBot. Describe your issue below, 
and I'll help you classify the ticket and provide an instant solution.
""")

# --- SIDEBAR (Project Info) ---
with st.sidebar:
    st.header("Project Info")
    st.info("""
    **Model:** DistilBERT + Gemini 2.5-flash
    **Developer:** Baltasar Djata
    **Backend:** FastAPI
    """)
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- CHAT HISTORY INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "metadata" in message:
            st.caption(f"Intent: {message['metadata']['intent']} | Confidence: {message['metadata']['confidence']}")

# --- CHAT INPUT & LOGIC ---
if prompt := st.chat_input("How can I help you today?"):
    # 1. Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Call FastAPI Backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(BACKEND_URL, json={"query": prompt})
                if response.status_code == 200:
                    data = response.json()
                    
                    bot_response = data["response"]
                    metadata = {
                        "intent": data["intent"],
                        "confidence": data["confidence"]
                    }

                    # Display assistant response
                    st.markdown(bot_response)
                    st.caption(f"🔍 System Note: Detected **{metadata['intent']}** ({metadata['confidence']*100:.2f}%)")
                    
                    # Save to history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": bot_response,
                        "metadata": metadata
                    })
                else:
                    st.error("Failed to connect to Backend.")
            except Exception as e:
                st.error(f"Error: {str(e)}")