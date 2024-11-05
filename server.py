from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector/<text>")
def emotion(text):
    result = emotion_detector(text)
    return (f"For the given statement, the system response is"
    f"'anger': {result['anger']},"
    f"'disgust': {result['disgust']},"
    f"'fear': {result['fear']},"
    f"'joy': {result['joy']} and"
    f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}")
