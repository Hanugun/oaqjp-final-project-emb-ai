"""
This is Flask web application for emotion detection
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle GET requests for emotion detection.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function to get the emotion scores
    result = emotion_detector(text_to_analyze)

    # Check if the result is None, indicating an invalid or empty input
    if result['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return jsonify({'response': response_text})

@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
