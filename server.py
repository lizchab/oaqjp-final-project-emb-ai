from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    
    if not text_to_analyze:
        return jsonify({'error': 'No text provided'}), 400
    
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

@app.route('/')
def index():
    return "Welcome to the Emotion Detection API! Use POST /emotionDetector with JSON: {'text': 'your text here'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
