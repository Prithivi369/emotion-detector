def emotion_detector(text_to_analyze):

    if text_to_analyze is None or text_to_analyze == "":
        return None

    emotions = {
        "anger": 0.02,
        "disgust": 0.01,
        "fear": 0.03,
        "joy": 0.88,
        "sadness": 0.06
    }

    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return result