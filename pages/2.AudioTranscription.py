import streamlit as st
from dotenv import load_dotenv
from google.cloud import speech
from google.protobuf import wrappers_pb2
import os
import tempfile

st.set_page_config(page_title="Video to Notes", page_icon="🎥", layout="wide")
st.title("🎥 Video to Notes")
st.markdown("---")

load_dotenv()

class VideoToNotes:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sehajpunitsingh/Desktop/Code/APIKeys/studychain-backend-e47e269395bb.json"
        self.client = speech.SpeechClient()
    
    def transcribe_audio(self, audio_file_path):
        """Transcribe audio file and return transcript"""
        try:
            # Read the audio file
            with open(audio_file_path, "rb") as audio_file:
                content = audio_file.read()
            
            audio = speech.RecognitionAudio(content=content)

            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.MP3,
                sample_rate_hertz=48000,
                language_code="en-US",
                model="latest_long",
                audio_channel_count=2,
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            )

            # Detect speech in the audio file
            response = self.client.recognize(config=config, audio=audio)

            # Combine all transcript lines into a single paragraph
            full_transcript = ""
            for result in response.results:
                transcript_line = result.alternatives[0].transcript
                full_transcript += transcript_line + " "
            
            # Clean up the transcript
            full_transcript = full_transcript.strip()
            
            return full_transcript
            
        except Exception as e:
            return f"Error transcribing audio: {str(e)}"

# Initialize the video to notes processor
if 'audio_processor' not in st.session_state:
    st.session_state.audio_processor = VideoToNotes()

# Sidebar for file upload
with st.sidebar:
    st.header("📁 Upload Video/Audio")
    
    uploaded_file = st.file_uploader(
        "Choose a video or audio file",
        type=['mp4', 'avi', 'mov', 'mkv', 'mp3', 'wav', 'm4a'],
        help="Upload a video or audio file to transcribe"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.markdown(f"**Size:** {uploaded_file.size / 1024 / 1024:.2f} MB")
        st.markdown(f"**Type:** {uploaded_file.type}")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📹 File Preview")
    if uploaded_file is not None:
        # Show video if it's a video file
        if uploaded_file.type.startswith('video'):
            st.video(uploaded_file)
        else:
            st.audio(uploaded_file)
    else:
        st.info("👆 Upload a video or audio file to get started")
        st.markdown("""
        **Supported formats:**
        - **Video:** MP4, AVI, MOV, MKV
        - **Audio:** MP3, WAV, M4A
        
        **What happens:**
        1. Upload your file
        2. Click 'Transcribe' button
        3. Get the transcript as notes
        """)

with col2:
    st.subheader("📝 Transcription")
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{uploaded_file.name.split(".")[-1]}') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            temp_file_path = tmp_file.name
        
        # Transcribe button
        if st.button("🎙️ Transcribe Audio", type="primary"):
            with st.spinner("Transcribing audio..."):
                transcript = st.session_state.audio_processor.transcribe_audio(temp_file_path)
                
                if transcript.startswith("Error"):
                    st.error(transcript)
                else:
                    st.success("✅ Transcription complete!")
                    
                    # Display transcript
                    st.markdown("### 📄 Transcript:")
                    st.text_area("Transcript", transcript, height=200)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Transcript",
                        data=transcript,
                        file_name=f"{uploaded_file.name.split('.')[0]}_transcript.txt",
                        mime="text/plain"
                    )
        
        # Clean up temp file
        try:
            os.unlink(temp_file_path)
        except:
            pass
    else:
        st.info("Upload a file to start transcription")

# Footer
st.markdown("---")
st.markdown("""
### 💡 Tips:
- For best results, use clear audio with minimal background noise
- Longer files may take more time to process
- The transcript will be saved as a text file
""")