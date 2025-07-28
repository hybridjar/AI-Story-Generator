# AI Story Generator Web App

This Flask-based web application allows users to generate personalized children's stories using Google Gemini AI, translate them into multiple languages, and even convert them into speech using gTTS. It stores generated stories in a PostgreSQL (or any SQLAlchemy-compatible) database for future reference.

# Features
# Generate AI-powered children’s stories based on:

Age (1–8)
Gender
Mood, Interests
Story length and time of day
Additional inputs

# Multilingual support:

English (en)
Hindi (hi)
Marathi (mr)
Text-to-speech output via gTTS 
Story storage via SQLAlchemy ORM
API Key and DB credentials loaded from .env

# Technologies Used

Tool / Library                          	Purpose
Flask	                                    Backend web framework
SQLAlchemy	                              ORM for database integration
gTTS (Google TTS)	                        Text-to-speech synthesis
Google Gemini API	                        AI story generation
Deep Translator	                          Story translation (via Google Translate)
Python Dotenv	                            Manage API keys and DB secrets

# Getting Started

# 1. Clone the Repository
bash

git clone https://github.com/your-username/ai-story-generator.git
cd ai-story-generator

# 2. Set Up Virtual Environment (Optional but Recommended)
bash

python -m venv venv
source venv/bin/activate  

# 3. Install Dependencies
bash

pip install -r requirements.txt

# 4. Setup .env File
Create a .env file in the root folder with the following:
ini

API_KEY=your_gemini_api_key_here
DB_URI=sqlite:///stories.db  # or use PostgreSQL/MySQL URI

# 5. Run the Application
bash

python app.py

Visit http://localhost:5000 in your browser.

# API Endpoints
/generate_story — POST

# Request Body (JSON):
json

{
  "age": 5,
  "gender": "boy",
  "mood": "excited",
  "interests": "space, robots",
  "story_length": "long",
  "time_of_day": "bedtime",
  "additional": "Include a talking cat",
  "language": "hi"
}

# Response:

json

{
  "story": "एक बार की बात है, एक छोटा लड़का था..."
}

/speak_story — POST

# Request Body (JSON):
json

{
  "story": "Once upon a time...",
  "language": "en"
}
# Response: audio/mpeg stream.

# File Structure
bash

ai-story-generator/
│
├── app.py                 
├── templates/
│   └── form.html          
├── static/                
├── .env                   
├── requirements.txt       
└── README.md               

# Environment Variables (.env)

API_KEY – Your Gemini API Key (Google Generative AI)
DB_URI – SQLAlchemy database URI (e.g., SQLite or PostgreSQL)

# Notes

-Gemini model used: gemini-2.0-flash via REST transport
-Translation supported: 'en', 'hi', 'mr'
-Age limit is strictly 1 to 8 years to ensure child-appropriate content
-App runs in debug=True mode by default – not suitable for production

# To-Do for Production

-Add user authentication
-Use a WSGI server (like Gunicorn or uWSGI)
-Enable logging
-Use proper input sanitization
-Set debug=False before deployment

# Author
Anubhav Kumar
Delhi, India
LinkedIn | anubhavkumar11908@gmail.com
