"""Flask server to run emotion detection on input text using Watson NLP."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page with the text input form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def call_emotion_detector():
    """Process text input and return detected emotions and dominant emotion."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(debug=True)
