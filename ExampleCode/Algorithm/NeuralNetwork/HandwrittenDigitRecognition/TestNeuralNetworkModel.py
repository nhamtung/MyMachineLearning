
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from keras.models import model_from_json

# Doc file va show image
img = misc.imread('5.jpg', flatten=True)
# img = misc.imread(sys.argv[1], flatten=True)
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()

# Dao nguoc mau sac cua image
img = 255 - img
plt.imshow(img, cmap=plt.get_cmap('gray'))
# plt.show()
#
# Scale image 28x28
img = misc.imresize(img, (28,28))
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
print(img.shape)

# Chuan hoa du lieu
img = img.reshape(-1).astype('float32')
img = img/255

# doc model tu file mnist.json va .h5
f = open('mnist.json')
json_content = f.read()
f.close()

model = model_from_json(json_content)
model.load_weights('mnist.h5')

# Du doan ket qua
X = np.array([img])
y = model.predict(X)
print('Digit : ', np.argmax(y[0]))