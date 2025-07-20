import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Chatbot", page_icon="🗣️", layout="wide")
st.title("🗣️ Chardikala Chatbot")
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

# Initialize chatbot
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Chat Settings")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.chatbot.interaction = [
            {"role":"system", "content":"You are a helpful and friendly chatbot. Your name is Chardikala-Bot"},
        ]
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Ask me anything!
    - I remember our conversation
    - Use the clear button to start fresh
    """)

# Main chat interface
st.markdown("### 💬 Start a conversation with Chardikala-Bot")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot.chat(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Show conversation stats
#if st.session_state.messages:
#    st.markdown("---")
#    col1, col2, col3 = st.columns(3)
#    with col1:
#        st.metric("Total Messages", len(st.session_state.messages))
#    with col2:
#        user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
#        st.metric("Your Messages", user_messages)
#    with col3:
#        assistant_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
#        st.metric("Bot Responses", assistant_messages) 