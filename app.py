import io
import os
from flask import Flask, request, jsonify, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from gtts import gTTS
from deep_translator import GoogleTranslator
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api_key = os.getenv("API_KEY")
if not api_key:
    raise EnvironmentError("API_KEY not found in .env")

genai.configure(api_key=api_key, transport="rest")

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0.3,
        "top_p": 0.7,
        "top_k": 30,
        "max_output_tokens": 700,
        "response_mime_type": "text/plain",
    }
)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    mood = db.Column(db.String(50), nullable=True)
    interests = db.Column(db.String(100), nullable=True)
    story_length = db.Column(db.String(50), nullable=True)
    time_of_day = db.Column(db.String(50), nullable=True)
    additional_data = db.Column(db.String(150), nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    try:
        data = request.json
        print("Received data:", data)

        if not data:
            raise ValueError("No data received from frontend.")

        required_fields = ['age', 'gender']
        for field in required_fields:
            if not data.get(field):
                raise ValueError(f"'{field}' is a required field and cannot be empty.")

        try:
            age = int(data['age'])
            if not (1 <= age <= 8):
                raise ValueError("Age must be between 1 and 8.")
        except ValueError:
            raise ValueError("Age must be a valid number between 1 and 8.")

        gender = data.get('gender', 'boy')
        mood = data.get('mood', 'happy')
        interests = data.get('interests', 'adventure')
        story_length = data.get('story_length', 'short')
        time_of_day = data.get('time_of_day', 'bedtime')
        additional_requests = data.get('additional', '')
        language = data.get('language', 'en')

        prompt = f"""Write a simple story for a {age}-year-old {gender}.
Mood: {mood}
Interests: {interests}
Story Length: {story_length}
Time of Day: {time_of_day}
Additional: {additional_requests}"""

        print("Prompt ready. Calling Gemini API...")

        response = model.generate_content(prompt)

        if not response:
            raise ValueError("Gemini returned no response.")

        try:
            story = response.text.strip()
        except AttributeError:
            story = "".join([part.text for part in response.parts]).strip()

        if not story:
            raise ValueError("Gemini returned an empty story.")

        print("Gemini response received.")

        if language in ['hi', 'mr']:
            story = GoogleTranslator(source='en', target=language).translate(story)

        new_story = Story(
            age=age,
            gender=gender,
            mood=mood,
            interests=interests,
            story_length=story_length,
            time_of_day=time_of_day,
            additional_data=additional_requests
        )
        db.session.add(new_story)
        db.session.commit()

        print("Story saved to DB.")

        return jsonify({'story': story})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({'error': str(e)}), 400

@app.route('/speak_story', methods=['POST'])
def speak_story():
    try:
        data = request.json
        story = data.get('story', '')
        language = data.get('language', 'en')

        if not story:
            raise ValueError("Story text is missing.")

        supported_languages = ['en', 'hi', 'mr']
        if language not in supported_languages:
            raise ValueError(f"Unsupported language: {language}")

        tts = gTTS(story, lang=language)
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        return Response(audio_bytes, mimetype="audio/mpeg")
    except Exception as e:
        print(" TTS ERROR:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
