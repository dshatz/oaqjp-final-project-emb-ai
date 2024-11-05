import requests

def emotion_detector(text_to_analyze):
    json = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyze } }
    ).json()
    emotions = json["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions.keys(), key=lambda d: emotions[d])
    return emotions
