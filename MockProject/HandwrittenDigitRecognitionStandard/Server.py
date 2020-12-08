
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import base64
import numpy as np
from keras.models import model_from_json
from skimage.transform import resize
from skimage.io import imread

app = Flask(__name__)
CORS(app)

images_folder = "images"
classes = [chr(c) for c in range(ord('a'), ord('z') + 1)]

image_index = 1
input_size = 32

# # using for CNN Model
# f = open('model_cnn.json')
# json_content = f.read()
# f.close()
# model = model_from_json(json_content)
# model.load_weights('model_cnn_weights.h5')

# using for MLP Model
f = open('model_mlp.json')
json_content = f.read()
f.close()
model = model_from_json(json_content)
model.load_weights('model_mlp_weights.h5')

@app.route('/images/save', methods=['POST'])
def save_image():
    global image_index
    img_path = os.path.join(images_folder, str(image_index) + ".png")
    image_index += 1
    image_data = request.json['image_data']
    image_data = image_data[22:]                   # remove header padding
    f = open(img_path, 'wb')
    f.write(base64.b64decode(image_data))
    f.close()
    return jsonify('OK')

@app.route('/images/recognize', methods=['POST'])
def recognize():
    img_path = "web_images.png"
    image_data = request.json['image_data']
    image_data = image_data[22:]                   # remove header padding
    f = open(img_path, 'wb')
    f.write(base64.b64decode(image_data))
    f.close()

    img = imread(img_path)
    img = img[:, :, -1]
    img = resize(img, (input_size, input_size), preserve_range=True)
    X = img.astype('float32') / 255.0

    # X = X.reshape((1, input_size, input_size, 1))   # using for CNN Model
    X = X.reshape((1, input_size * input_size)) # using for MLP Model

    y = model.predict(X)[0]
    print('Input {} , output : {}'.format(img_path, classes[np.argmax(y)]))

    os.remove(img_path)
    return jsonify(classes[np.argmax(y)])

@app.route('/')
def mainPage():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=False)