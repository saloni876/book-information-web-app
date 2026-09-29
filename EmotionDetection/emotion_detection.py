import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=myobj, headers=headers)

    format_res = response.json()
    emotion_extract = format_res["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotion_extract, key=emotion_extract.get)

    return {
        "anger": emotion_extract["anger"],
        "disgust": emotion_extract["disgust"],
        "fear": emotion_extract["fear"],
        "joy": emotion_extract["joy"],
        "sadness": emotion_extract["sadness"],
        "dominant_emotion": dominant_emotion
    }
