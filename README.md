# ASTRA
ASTRA is a Python voice assistant that uses SpeechRecognition, pyttsx3, gTTS, pywhatkit, Wikipedia API, OpenCV, feedparser, and requests to perform tasks via voice commands. It can play YouTube videos, fetch news, tell jokes, open the camera, and provide real-time information like time and IP address.
# 🚀 ASTRA Voice Assistant  
**Second Year Python Group Project**

**ASTRA** is a Python-based voice assistant that interacts with users through natural voice commands. It performs real-time tasks such as playing YouTube music, telling time, fetching news, searching Wikipedia, opening the webcam, telling jokes, and more.

---

## 🎯 Features

- 🎵 Play YouTube videos/music using voice commands  
- ⏰ Get current time  
- 🌐 Wikipedia search  
- 📰 Fetch latest news using RSS feeds  
- 😂 Tell programming jokes  
- 📷 Open system webcam  
- 🌍 Fetch your IP address  
- 🔎 Perform Google searches  
- 💬 Conversational replies with basic humor

---

## 🧰 Libraries & APIs Used

- `speech_recognition` – for voice input  
- `pyttsx3` – offline text-to-speech  
- `gTTS` – Google Text-to-Speech  
- `pywhatkit` – YouTube playback and Google search  
- `wikipedia` – for summarizing queries  
- `opencv-python` (`cv2`) – to access webcam  
- `feedparser` – for parsing RSS news feeds  
- `pyjokes` – for programming jokes  
- `requests` – for IP lookup and HTTP requests  
- `GoogleNews` – *(optional/imported but not used)*

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install speechrecognition pyttsx3 gTTS pywhatkit wikipedia opencv-python feedparser pyjokes requests
## Project Structure
astra/
├── astra.py           # Main Python script
├── README.md          # Project documentation
└── requirements.txt   # (optional) Dependency list
