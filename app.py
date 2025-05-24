from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyse = request.args.get('textToAnalyze')

    input_json = jsonify({ "raw_document": { "text": text_to_analyse } })
    response = requests.post(URL, input_json, headers=HEADERS)
    return jsonify(response.json()), response.status_code


if __name__ == "__main__":
    app.run(debug=True)