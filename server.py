"""Flask server for emotion detection"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion():
    """Api endpoint for emotion detection"""
    result = emotion_detector(request.args.get("textToAnalyze"))
    if not result["dominant_emotion"]:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
    f"'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, "
    f"'fear': {result['fear']}, "
    f"'joy': {result['joy']} and"
    f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}")

@app.route('/')
def home():
    """UI route"""
    return render_template('index.html')
   