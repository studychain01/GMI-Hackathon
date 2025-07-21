# 🎙️ Chardikala AI Platform

A comprehensive AI-powered platform that combines multiple cutting-edge technologies to provide text chat, video analysis, audio transcription, and document-to-podcast conversion capabilities.

## 🌟 Features

### 🗣️ **Text Chatbot**
- **Conversational AI**: Chat with a friendly AI assistant powered by OpenAI GPT-3.5-turbo
- **Conversation History**: Maintains chat history across sessions
- **Smart Responses**: Context-aware conversations with memory
- **Settings Panel**: Clear chat history and manage conversation settings

### 🎥 **Video Chat with Gemini**
- **Visual Analysis**: Upload videos and chat about their content using Google's Gemini AI
- **Real-time Processing**: Advanced video understanding and analysis
- **Interactive Q&A**: Ask questions about what's happening in videos
- **Multiple Formats**: Support for MP4, AVI, MOV, MKV, WEBM formats

### 📝 **Audio Transcription**
- **Speech-to-Text**: Convert video/audio files to text using Google Speech-to-Text
- **Multiple Formats**: Support for MP4, AVI, MOV, MKV, MP3, WAV, M4A
- **High Accuracy**: Professional-grade transcription with punctuation
- **File Processing**: Automatic text extraction and formatting

### 🎙️ **Notes to Podcast**
- **Document Conversion**: Transform PDF and TXT files into engaging podcasts
- **Voice Synthesis**: Multiple voice options using Google Cloud Text-to-Speech
- **Customizable Settings**: Adjust speaking speed and choose from various voices
- **Instant Download**: Generate and download high-quality MP3 audio files

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Cloud account with API keys
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd GMI-Hackathon
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account.json
   ```

4. **Set up Google Cloud credentials**
   - Download your Google Cloud service account JSON file
   - Update the path in the code files or set the environment variable

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure

```
GMI-Hackathon/
├── main.py                          # Homepage with quick chat
├── pages/
│   ├── 1.Chatbot.py                # Full chatbot interface
│   ├── 2.AudioTranscription.py     # Speech-to-text conversion
│   ├── 3.Chat_with_Video.py        # Video analysis with Gemini
│   ├── 4.Notes_to_Podcast.py       # Document to podcast conversion
│   └── 5.Transcribing_notes.py     # Additional transcription features
├── requirements.txt                 # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## 🛠️ Technologies Used

### **AI & Machine Learning**
- **OpenAI GPT-3.5-turbo**: Text generation and conversation
- **Google Gemini AI**: Video analysis and understanding
- **Google Speech-to-Text**: Audio transcription
- **Google Cloud Text-to-Speech**: Voice synthesis

### **Web Framework**
- **Streamlit**: Interactive web application framework
- **Session State Management**: Persistent user sessions

### **File Processing**
- **PyPDF2**: PDF text extraction
- **OpenCV**: Video processing and frame extraction
- **Pillow**: Image processing

### **Cloud Services**
- **Google Cloud Platform**: Speech and text-to-speech APIs
- **Google AI Studio**: Gemini API access

## 🎯 Usage Guide

### **Text Chatbot**
1. Navigate to the "Chatbot" page
2. Start typing your questions or messages
3. The AI will respond with helpful information
4. Use the sidebar to clear chat history or adjust settings

### **Video Chat with Gemini**
1. Go to the "Video Chat" page
2. Upload a video file (MP4, AVI, MOV, MKV, WEBM)
3. Wait for Gemini to process the video
4. Ask questions about the video content
5. Get detailed analysis and insights

### **Audio Transcription**
1. Visit the "Audio Transcription" page
2. Upload an audio or video file
3. Click "Transcribe Audio" to process
4. View the extracted text transcript
5. Download the transcript as a text file

### **Notes to Podcast**
1. Navigate to "Notes to Podcast"
2. Upload a PDF or TXT document
3. Choose your preferred voice and speed
4. Click "Generate Podcast"
5. Listen to the preview and download the MP3 file

## 🔧 Configuration

### **API Keys Setup**

#### **OpenAI API**
1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Generate an API key
3. Add to your `.env` file:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   ```

#### **Google Cloud Setup**
1. Create a Google Cloud project
2. Enable the following APIs:
   - Speech-to-Text API
   - Text-to-Speech API
3. Create a service account and download the JSON key
4. Set the credentials path in your code or environment

#### **Gemini API**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Generate a Gemini API key
3. Add to your `.env` file:
   ```env
   GEMINI_API_KEY=your-gemini-key-here
   ```

## 📦 Dependencies

```
openai>=1.0.0
streamlit>=1.28.0
python-dotenv>=1.0.0
opencv-python>=4.8.0
pillow>=10.0.0
numpy>=1.24.0
google-generativeai>=0.3.0
PyPDF2>=3.0.0
google-cloud-texttospeech>=2.0.0
```

## 🎨 Features in Detail

### **Multi-Page Navigation**
- **Responsive Design**: Works on desktop and mobile
- **Session Management**: Maintains state across page navigation
- **Intuitive Interface**: Easy-to-use sidebar navigation

### **Advanced AI Integration**
- **Context Awareness**: AI remembers conversation history
- **Multi-Modal Processing**: Handles text, audio, video, and documents
- **Real-time Processing**: Instant responses and analysis


## 🚀 Deployment

### **Local Development**
```bash
streamlit run main.py
```




**Chardikala - High Spirits** 