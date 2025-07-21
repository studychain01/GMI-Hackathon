from openai import OpenAI
import streamlit as st 
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Chardikala AI Platform", page_icon="🎙️", layout="wide")
st.title("🎙️ Chardikala AI Platform")
st.markdown("---")

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

class Chatbot: 
    def __init__(self):
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.interaction = [
            {"role":"system", "content":"You are a helpful and friendly chatbot. Your name is Chardikala-Bot"},
        ]
    
    def chat(self, user_message):
        self.interaction.append({"role":"user", "content":user_message})

        try: 
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.interaction, 
                max_tokens=1000
            )

            assistant_response = response.choices[0].message.content 

            self.interaction.append({"role": "assistant", "content": assistant_response})

            return assistant_response 

        except Exception as e:
            return f"Error: {str(e)}"

# Welcome section
st.header("Welcome to Chardikala AI Platform! 🤖")
st.markdown("""
This platform offers multiple AI-powered features:

### 🗣️ **Text Chatbot**
- Have conversations with our friendly AI assistant
- Get help, ask questions, or just chat!
- Full conversation history and chat interface

### 🎥 **Video Chat with Gemini**
- Upload videos and chat with them using Google's Gemini AI
- Get visual analysis and insights from your video content
- Ask questions about what's happening in the video
- Real-time video processing and analysis

### 📝 **Audio Transcription**
- Upload video/audio files and convert them to text
- Get accurate transcriptions using Google Speech-to-Text
- Perfect for meeting notes, lectures, and interviews
- Support for multiple audio/video formats

### 🎙️ **Notes to Podcast**
- Upload PDF or TXT documents and convert them to podcasts
- Choose from multiple voices and speaking speeds
- Generate high-quality MP3 audio using Google Cloud TTS
- Instant audio preview and download

---
""")

# Quick chat interface on homepage
st.subheader("💬 Quick Chat")
st.markdown("Try our chatbot right here on the homepage:")

if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chatbot.chat(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Navigation info
st.markdown("---")
st.markdown("""
### 📱 Navigation
Use the sidebar to navigate between different features:
- **🏠 Home** - This page with quick chat and platform overview
- **🗣️ Chatbot** - Full chatbot interface with conversation history and settings
- **📝 Audio Transcription** - Convert video/audio files to text transcripts using Google Speech-to-Text
- **🎥 Video Chat** - Upload videos and chat with them using Google's Gemini AI for visual analysis
- **🎙️ Notes to Podcast** - Convert PDF/TXT documents to podcasts with voice synthesis and download
""")
            
        