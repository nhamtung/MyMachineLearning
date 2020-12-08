import os
import numpy as np
from random import random, randint, shuffle
from skimage.transform import rotate, resize
from skimage.io import imread
from keras.utils import to_categorical

input_size = 32
images_folder = "images"
num_img_per_class = 2000
train_factor = 0.7

min_scale = 0.75
max_scale = 1.35


def gen_img(img_path):
    img = imread(img_path)
    img = img[:, :, -1]
    rotation = 20 * random() - 10
    img = rotate(img, rotation, preserve_range=True)
    img_size = len(img)
    hscan = np.max(img, axis=0)
    x1 = np.min(np.where(hscan > 0))
    x2 = np.max(np.where(hscan > 0))

    vscan = np.max(img, axis=1)
    y1 = np.min(np.where(vscan > 0))
    y2 = np.max(np.where(vscan > 0))

    dx, dy = x2 - x1, y2 - y1
    min_size = max(dx, dy, int(img_size / max_scale))
    max_size = int(img_size / min_scale)
    new_size = randint(min_size, max_size)
    offset_x = randint(0, new_size - dx)
    offset_y = randint(0, new_size - dy)
    new_img = np.zeros((new_size, new_size), dtype=np.uint8)
    new_img[offset_y:offset_y + dy, offset_x:offset_x + dx] = img[y1:y2, x1:x2]
    return new_img


classes = [chr(c) for c in range(ord('a'), ord('z') + 1)]
num_classes = len(classes)

map_img_paths = {}

for class_name in classes:
    sub_folder = os.path.join(images_folder, class_name)
    img_files = [f for f in os.listdir(sub_folder) if f.lower().endswith('.jpg') or f.lower().endswith('.png')]
    map_img_paths[class_name] = [os.path.join(sub_folder, f) for f in img_files]

data = []

for i in range(len(classes)):
    class_name = classes[i]
    img_list = map_img_paths[class_name]

    print('Generate images for class ', class_name)

    for j in range(num_img_per_class):
        img = gen_img(img_list[j % len(img_list)])
        img = resize(img, (input_size, input_size), preserve_range=True)
        img = img.astype('uint8')
        data.append((img, i))

shuffle(data)
Ntrain = int(len(data) * train_factor)

train_data = data[:Ntrain]
test_data = data[Ntrain:]

Xtrain = np.array([item[0] for item in train_data], dtype=np.uint8)
Ytrain = np.array([to_categorical(item[1], num_classes) for item in train_data], dtype=np.uint8)

Xtest = np.array([item[0] for item in test_data], dtype=np.uint8)
Ytest = np.array([to_categorical(item[1], num_classes) for item in test_data], dtype=np.uint8)

print("Xtrain: ")
print(Xtrain)
print("Ytrain: ")
print(Ytrain)
print("Xtest: ")
print(Xtest)
print("Ytest: ")
print(Ytest)

# Xtrain.tofile('Xtrain.np')
# Ytrain.tofile('Ytrain.np')
# Xtest.tofile('Xtest.np')
# Ytest.tofile('Ytest.np')

