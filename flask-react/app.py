from flask import Flask, jsonify, render_template, request
from werkzeug import secure_filename
from flask_cors import CORS
import keras
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K
from keras.models import model_from_json
from keras.models import Sequential

import cv2
import numpy as np
import os
cwd = os.getcwd()

# mean and standard deviation of the MNIST train dataset
mean_px=33.31842
std_px=78.56749

def norm_input(x): return (x-mean_px)/std_px

def get_model_bn_do():
    model = Sequential([
        Lambda(norm_input, input_shape=(1,28,28)),
        Conv2D(32,(3,3), activation='relu'),
        BatchNormalization(axis=1),
        Conv2D(32,(3,3), activation='relu'),
        MaxPooling2D(),
        BatchNormalization(axis=1),
        Conv2D(64,(3,3), activation='relu'),
        BatchNormalization(axis=1),
        Conv2D(64,(3,3), activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(10, activation='softmax')
        ])
    model.compile(Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model
model = get_model_bn_do()
# load weights into new model
loaded_model.load_weights(cwd+'/mnist_final.h5')
#print("Succesfully loaded-rea model")

app = Flask(__name__)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def hello_flask():
	return 'hello flask'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      im_gray = cv2.imread(f.filename, cv.CV_LOAD_IMAGE_GRAYSCALE)
      sample=cv2.resize(im_gray,(28,28),interpolation = cv2.INTER_AREA)
      sample=image.img_to_array(sample)/255
      sample=np.expand_dims(sample,0)
      pred=model.predict(sample,batch_size=1)
      return pred

@app.route('/api/hello-world', methods=['GET'])
def say_hello():
	resObj = {
		'content': 'Hello, flask-react'
	}
	return jsonify(resObj)

app.run(host='0.0.0.0', port=80)
