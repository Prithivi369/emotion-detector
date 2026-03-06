"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to detect emotions from the input text.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again."

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
