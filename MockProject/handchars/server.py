import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import base64

app = Flask(__name__)
CORS(app)

images_folder = "images"
image_index = 1

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
    c = 'a' # Test
    return jsonify(c)

@app.route('/')
def mainPage():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=False)