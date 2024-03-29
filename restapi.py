# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Run a Flask REST API exposing one or more YOLOv5s models
"""

import argparse
import io

from ast import literal_eval
import base64

import torch
from flask import Flask, request
from PIL import Image

app = Flask(__name__)
models = {}

DETECTION_URL = "/v1/object-detection/<model>"


@app.route(DETECTION_URL, methods=["POST"])
def predict(model):
    im_str = request.form['image']
    im_bytes = base64.b64decode(im_str)
    im = base64.b64decode(im_bytes)
    im = Image.open(io.BytesIO(im_bytes))
    if model in models:
        holds = models[model](im, size=640)  # reduce size=320 for faster inference
        jsonArray = holds.pandas().xyxy[0].to_json(orient="records")
        results = {
            'success': True,
            'results': literal_eval(jsonArray)
        }
        return results
    
    if request.method != "POST":
        return

    # if request.files.get("image"):
    #     # Method 1
    #     # with request.files["image"] as f:
    #     #     im = Image.open(io.BytesIO(f.read()))

    #     # Method 2
    #     im_file = request.files["image"]
    #     im_bytes = im_file.read()
    #     im = Image.open(io.BytesIO(im_bytes))

    #     if model in models:
    #         holds = models[model](im, size=640)  # reduce size=320 for faster inference
    #         jsonArray = holds.pandas().xyxy[0].to_json(orient="records")
    #         results = {
    #             'success': True,
    #             'results': literal_eval(jsonArray)
    #         }
    #         return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    parser.add_argument('--model', nargs='+', default=['yolov5s'], help='model(s) to run, i.e. --model yolov5n yolov5s')
    opt = parser.parse_args()

    for m in opt.model:
        models[m] = torch.hub.load("ultralytics/yolov5", 'custom', '/workspace/detect-hold-with-flask/hold.pt', force_reload=True, skip_validation=True)

    app.run(host="0.0.0.0", port=opt.port)  # debug=True causes Restarting with stat