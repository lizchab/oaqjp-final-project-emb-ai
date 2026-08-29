"""
Flask web application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """
    Handle emotion detection requests.
    Expects a parameter 'textToAnalyze' (GET or POST).
    Returns a string with the dominant emotion or an error message.
    """
    text = request.args.get('textToAnalyze') or request.form.get('textToAnalyze')
    if not text:
        return "Invalid input! Please provide text to analyze."

    result = emotion_detector(text)
    if result and result.get('dominant_emotion'):
        return f"The dominant emotion is: {result['dominant_emotion']}"
    else:
        return f"Error: {result.get('error', 'Unknown error')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)