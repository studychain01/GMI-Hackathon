from openai import OpenAI
import streamlit as st 
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Chatbot", page_icon="🎙️")
st.title("Chatbot")

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

if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chatbot.chat(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
            
        