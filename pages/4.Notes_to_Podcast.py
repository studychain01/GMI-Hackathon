import streamlit as st
import os
from google.cloud import texttospeech
import PyPDF2
import io

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sehajpunitsingh/Desktop/Code/APIKeys/studychain-backend-e47e269395bb.json"

def extract_text_from_file(uploaded_file):
    """Extract text from uploaded PDF or TXT file"""
    try:
        if uploaded_file.type == "text/plain":
            # For TXT files
            return uploaded_file.getvalue().decode('utf-8')
        elif uploaded_file.type == "application/pdf":
            # For PDF files
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        else:
            return "Unsupported file type"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def synthesize_speech(text, voice_name="en-US-Standard-C", speed=1.0):
    """Synthesize speech from text using Google Cloud TTS"""
    try:
        client = texttospeech.TextToSpeechClient()
        
        # Convert text to SSML
        ssml = f"<speak>{text}</speak>"
        
        input_text = texttospeech.SynthesisInput(ssml=ssml)
        
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name=voice_name,
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=speed
        )
        
        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )
        
        return response.audio_content
        
    except Exception as e:
        st.error(f"Error synthesizing speech: {str(e)}")
        return None

# Streamlit UI
st.set_page_config(page_title="Notes to Podcast", page_icon="🎙️")
st.title("🎙️ Notes to Podcast")
st.markdown("Convert your documents into podcasts!")

# Sidebar for controls
with st.sidebar:
    st.header("🎤 Voice Settings")
    
    # Voice selection
    voice_options = {
        "Professional Female": "en-US-Standard-C",
        "Professional Male": "en-US-Standard-D",
        "Casual Female": "en-US-Neural2-F",
        "Casual Male": "en-US-Neural2-D"
    }
    
    selected_voice = st.selectbox(
        "Choose Voice",
        options=list(voice_options.keys())
    )
    
    # Speed control
    speed = st.slider("Speaking Speed", 0.5, 2.0, 1.0, 0.1)
    
    st.markdown("---")
    
    # File upload
    st.header("📁 Upload Document")
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['pdf', 'txt'],
        help="Upload PDF or TXT files to convert to podcast"
    )
    
    if uploaded_file is not None:
        file_size = len(uploaded_file.getvalue()) / (1024 * 1024)
        st.info(f"📄 {uploaded_file.name}")
        st.info(f"📏 Size: {file_size:.2f} MB")
    
    st.markdown("---")
    
    # Generate button
    if st.button("🎙️ Generate Podcast", type="primary"):
        if uploaded_file is not None:
            with st.spinner("Processing document..."):
                # Extract text
                text_content = extract_text_from_file(uploaded_file)
                
                if text_content and not text_content.startswith("Error"):
                    # Generate speech
                    voice_code = voice_options[selected_voice]
                    audio_content = synthesize_speech(text_content, voice_code, speed)
                    
                    if audio_content:
                        # Store in session state
                        st.session_state.audio_content = audio_content
                        st.session_state.text_content = text_content
                        st.success("✅ Podcast generated successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to generate audio")
                else:
                    st.error(f"Error processing file: {text_content}")
        else:
            st.error("Please upload a file first!")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📄 Document Content")
    
    if uploaded_file is not None:
        st.success(f"✅ {uploaded_file.name} uploaded")
        
        # Show file info
        st.info(f"**Type:** {uploaded_file.type}")
        st.info(f"**Size:** {len(uploaded_file.getvalue()) / (1024 * 1024):.2f} MB")
        
        # Show extracted text
        if 'text_content' in st.session_state:
            st.text_area("Extracted Text", st.session_state.text_content[:1000] + "..." if len(st.session_state.text_content) > 1000 else st.session_state.text_content, height=300)
        else:
            st.info("Upload a file and click 'Generate Podcast' to see the extracted text")
    else:
        st.info("👆 Upload a PDF or TXT file to get started")
        st.markdown("""
        **Supported formats:**
        - PDF files (.pdf)
        - Text files (.txt)
        
        **How it works:**
        1. Upload your document
        2. Choose voice and speed
        3. Generate podcast
        4. Download audio file
        """)

with col2:
    st.subheader("🎙️ Podcast Audio")
    
    if 'audio_content' in st.session_state:
        st.success("🎵 Podcast generated!")
        
        # Audio player
        st.audio(st.session_state.audio_content, format="audio/mp3")
        
        # Download button
        st.download_button(
            label="📥 Download Podcast",
            data=st.session_state.audio_content,
            file_name=f"{uploaded_file.name.split('.')[0]}_podcast.mp3",
            mime="audio/mpeg"
        )
        
        # Audio info
        st.info(f"**Voice:** {selected_voice}")
        st.info(f"**Speed:** {speed}x")
        st.info(f"**Format:** MP3")
        
    else:
        st.info("🎵 Audio will appear here after generation")
        st.markdown("""
        **Features:**
        - Multiple voice options
        - Adjustable speaking speed
        - High-quality MP3 output
        - Instant audio preview
        - Easy download
        """)

# Footer
st.markdown("---")
st.markdown("""
**Powered by Google Cloud Text-to-Speech**
- Professional voice synthesis
- Multiple voice options
- High-quality audio output
""")