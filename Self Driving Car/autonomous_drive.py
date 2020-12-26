import cv2
from flask import Flask

import numpy as np

import socketio

import eventlet.wsgi
import eventlet

from io import BytesIO
import base64

from PIL import Image

from keras.models import load_model

import matplotlib.image as mpimg

sio = socketio.Server()
app = Flask(__name__)
model = None

speed_limit = 15

def img_preprocess(img):
    img = img[60:135, :, :]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 127.5 - 1

    return img


@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])

    img = Image.open(BytesIO(base64.b64decode(data['image'])))
    img = np.asarray(img)
    img = img_preprocess(img)

    img = np.array([img])

    steering_angle = float(model.predict(img))

    throttle = 1.0 - speed / speed_limit

    send_control(steering_angle, throttle)


@sio.on('connect')
def connect(sid, environ):
    print("connect")
    send_control(0, 1)


def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })


if __name__ == '__main__':
    model = load_model('model-002.h5')

    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
