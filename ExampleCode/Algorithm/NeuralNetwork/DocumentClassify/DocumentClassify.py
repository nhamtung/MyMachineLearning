import os
import re
import numpy as np
import gensim
from gensim import models
from pyvi import ViTokenizer, ViPosTagger

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.utils import to_categorical

import tensorflow as tf

special_regex = r'.*[0-9()\[\]{}\+\-\*\'/.%~`@#$%^&*|,\\?―="].*'

def word_tokenize(sentence):
    words, postags = ViPosTagger.postagging(ViTokenizer.tokenize(sentence.lower()))
    filter_words = []
    for i in range(len(words)):
        if postags[i] not in ['N','V','A'] : continue
        if re.match(special_regex, words[i]): continue
        filter_words.append(words[i])
    return filter_words

topics = ['xahoi' , 'kinhdoanh', 'thethao']
topic_names = ['Xã hội', 'Kinh doanh', 'Thể thao']
num_classes = len(topics)

documents = []
labels = []

for i in range(len(topics)):
    fn = os.path.join(topics[i] + '.txt')
    f = open(fn, encoding='utf8')
    documents.extend(f.readlines()[:100])
    labels.extend([i]*100)
    f.close()

processed_docs = list(map(word_tokenize, documents))
dictionary = gensim.corpora.Dictionary(processed_docs)
dictionary.filter_extremes(no_below=3, no_above=0.5, keep_n=100000)
dict_size = len(dictionary)

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
tfidf = models.TfidfModel(bow_corpus)

X = []
Y = []
for i in range(len(processed_docs)):
    bow_vector = tfidf[bow_corpus[i]]
    wordvec = np.zeros(dict_size)
    for index, value in bow_vector:
        wordvec[index] = value
    X.append(wordvec)
    Y.append(to_categorical(labels[i], num_classes))

X_train = np.array(X[:70] + X[100:170] + X[200:270])
Y_train = np.array(Y[:70] + Y[100:170] + Y[200:270])
X_test = np.array(X[70:100] + X[170:200] + X[270:300])
Y_test = np.array(Y[70:100] + Y[170:200] + Y[270:300])

model = Sequential()
model.add(Dense(5, input_dim=dict_size, activation='sigmoid'))
model.add(Dense(num_classes, activation='softmax'))

adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-6)
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=adam)
model.fit(X_train, Y_train, epochs=500, shuffle=True)
_ , score = model.evaluate(X_test, Y_test)
print('score = ', score)

# text = """Chiều ngày 7/7, một cơn mưa rào bất ngờ đổ xuống xứ Huế giải nhiệt sau những ngày nắng nóng lên đến 40 độ C,
# thỏa mãn "cơn khát" mưa của người dân."""
# text = """Đúng như dự đoán, tuyển nữ Việt Nam đã không gặp khó khăn để có thể dội cơn mưa bàn thắng vào lưới Singapore,
# với tỷ số chung cuộc 10-0, ở lượt trận thứ 2 giải bóng đá nữ vô địch Đông Nam Á 2018. """
text = """Với hơn 23 năm có mặt tại thị trường Việt Nam, thương hiệu BMW đã trở thành biểu tượng của những trải nghiệm 
lái đầy phấn khích sau vô-lăng. Nhưng ít ai biết được, để có thành công đó là cả một quá trình kết hợp hoàn hào của 
tinh thần cống hiến, niềm đam mê và tính chuyên nghiệp trong việc tạo ra những chiếc BMW mới chất lượng hàng đầu. 
Sự kết hợp hoàn hảo đó trên các dòng xe thuộc gia đình BMW X là nền tảng giúp cho thương hiệu BMW có vị thế vững chắc 
trong trái tim khách hàng không chỉ tại Việt Nam mà còn trên toàn thế giới."""

processed_text = word_tokenize(text)
bow = dictionary.doc2bow(processed_text)
bow_vector = tfidf[bow]

wordvec = np.zeros(dict_size)
for index, value in bow_vector:
    wordvec[index] = value

predict = model.predict(np.array([wordvec]))
categ = np.argmax(predict[0])
print('Chủ đề : ', topic_names[categ])