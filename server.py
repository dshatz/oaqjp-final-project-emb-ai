from flask import Flask, render_template
from EmotionDetection.emotion_detection import emotion_detector
from flask import request

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion():
    result = emotion_detector(request.args.get("textToAnalyze"))
    return (f"For the given statement, the system response is "
    f"'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, "
    f"'fear': {result['fear']}, "
    f"'joy': {result['joy']} and"
    f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}")

@app.route('/')
def home():
   return render_template('index.html')