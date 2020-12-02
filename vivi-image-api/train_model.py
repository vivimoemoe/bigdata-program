import tensorflow as tf
from tensorflow import keras
from PIL import Image


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names=['T-shirt/top','Trouser','Pullover','Dress','Coat',
             'Sandal','Shirt','Sneaker','Bag','Ankle boot']
new_im = Image.fromarray(train_images[0])
new_im.save('1.png')
print(train_images[0].shape)

train_images=train_images/255.0
test_images=test_images/255.0

model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation=tf.nn.relu),
    keras.layers.Dense(10,activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_images,train_labels,epochs=10)

model.save('model.h5')

model = keras.models.load_model('model.h5')
prediction = model.predict_classes([test_images[0]])
print(test_images[0])