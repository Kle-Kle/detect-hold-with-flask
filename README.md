# Flask REST API

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s are
commonly used to expose Machine Learning (ML)  models to other services. This folder contains an example REST API
created using Flask to expose the YOLOv5s model from [PyTorch Hub](https://pytorch.org/hub/ultralytics_yolov5/).

## Requirements

[Flask](https://palletsprojects.com/p/flask/) is required. Install with:

```shell
$ pip install Flask
```

## Run

After Flask installation run:

```shell
$ python3 restapi.py --port 5000 --model hold
```

Then use [curl](https://curl.se/) to perform a request:

```shell
$ curl -X POST -F image=@tests/test1.jpg 'http://localhost:5000/v1/object-detection/hold'
```

The model inference results are returned as a JSON response:

```json
[
  {'class': 0,
  'confidence': 0.8671640754,
  'name': 'hold',
  'xmax': 227.6498565674,
  'xmin': 137.6468048096,
  'ymax': 312.0726623535,
  'ymin': 242.4343566895},
 {'class': 0,
  'confidence': 0.8606841564,
  'name': 'hold',
  'xmax': 519.2680664062,
  'xmin': 432.5866699219,
  'ymax': 186.9302215576,
  'ymin': 112.3675079346},
 {'class': 0,
  'confidence': 0.8373295665,
  'name': 'hold',
  'xmax': 528.4312133789,
  'xmin': 400.2341308594,
  'ymax': 93.1273040771,
  'ymin': 0.0}
]
```

An example python script to perform inference using [requests](https://docs.python-requests.org/en/master/) is given
in `example_request.py`
