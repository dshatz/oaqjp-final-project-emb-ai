import requests

def emotion_detector(text_to_analyze):
    resp = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyze } }
    )
    json = resp.json()
    valid = True
    if resp.status_code == 400 or "emotionPredictions" not in json:
        valid = False
        json = {'emotionPredictions': 
        [{
            'emotion': {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}, 
            'target': '',
            'emotionMentions': None, 
            'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}
        ]}        
    emotions = json["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions.keys(), key=lambda d: emotions[d]) if valid else None
    return emotions
