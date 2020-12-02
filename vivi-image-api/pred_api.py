# coding=utf8
import tensorflow as tf
from tensorflow.python.keras.backend import set_session

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import numpy as np
from tensorflow import keras
from PIL import Image
sess = tf.Session()
graph = tf.get_default_graph()

# IMPORTANT: models have to be loaded AFTER SETTING THE SESSION for keras!
# Otherwise, their weights will be unavailable in the threads after the session there has been set
set_session(sess)


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
def setup_app(app):
    global model, class_names
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    model = keras.models.load_model('model.h5')
   # All your initialization code
setup_app(app)


def pred(test_images):
    global graph
    global model
    with graph.as_default():
        set_session(sess)
        prediction = model.predict_classes(test_images)
        return class_names[prediction[0]]


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    upload_file = request.files['file']
    img = Image.open(upload_file)
    # print(img.shape)
    print()
    # img = img.reshape(28, 28, 1)
    test_images = np.array(img).reshape(1, 28, 28) / 255.0
    return pred(test_images)


if __name__ == "__main__":
    app.run()