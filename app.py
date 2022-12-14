from detect import detector
import json
from flask_cors import CORS, cross_origin
from flask import (
    Flask, request, jsonify
)

app = Flask(__name__)
cors = CORS(app)


@app.route('/detect', methods=['POST', 'OPTIONS'])
@cross_origin()
def predict():
    # possible inputs: "dog_car.jpeg","dog_cat.jpg","horse_truck.png","plane_bird.webp"

    # read key "id" from request body
    id = request.json['id']

    dictionaryOfresults = detector("images/" + id)
    return jsonify({'message': 'success', 'results': dictionaryOfresults})


@app.route('/')
@cross_origin()
def home():
    return """<div>
    <h1>Welcome!</h1>
    <p>This is a flask API that serves the /detect endpoint for detecting objects in a video</p>
    <p>Send a POST request to /detect with a file named 'file' to detect objects in the image</p>
    <p>The frontend for this API can be found <a targe="_blank" href="https://play-classify-score.vercel.app/">here</a></p>
    </div>"""


if __name__ == '__main__':
    app.run(debug=True)
