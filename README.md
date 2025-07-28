
# AI Story Generator Web App

This Flask-based web application allows users to generate personalized children's stories using Google Gemini AI, translate them into multiple languages, and even convert them into speech using gTTS. It stores generated stories in a PostgreSQL (or any SQLAlchemy-compatible) database for future reference.

## Features

- Generate AI-powered children’s stories based on:
  - Age (1–8)
  - Gender
  - Mood and interests
  - Story length and time of day
  - Additional custom inputs
- Multilingual support:
  - English (en)
  - Hindi (hi)
  - Marathi (mr)
- Text-to-speech output via gTTS
- Story translation using Deep Translator
- Story storage via SQLAlchemy ORM
- Secure configuration via .env file (API key & DB URI)

## Technologies Used

| Tool / Library         | Purpose                             |
|------------------------|-------------------------------------|
| Flask                  | Backend web framework               |
| SQLAlchemy             | ORM for database integration        |
| gTTS (Google TTS)      | Text-to-speech synthesis            |
| Google Gemini API      | AI story generation                 |
| Deep Translator        | Story translation (Google Translate)|
| Python Dotenv          | Manage API keys and DB secrets      |

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-story-generator.git
cd ai-story-generator
```

### 2. Set Up Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup .env File

Create a `.env` file in the root folder with:

```ini
API_KEY=your_gemini_api_key_here
DB_URI=sqlite:///stories.db  # or use PostgreSQL/MySQL URI
```

### 5. Run the Application
```bash
python app.py
```

Then open your browser and go to:  
http://localhost:5000

## API Endpoints

### /generate_story — POST

Request Body and further details should be documented here.
