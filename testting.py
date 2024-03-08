import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

clothe_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images,test_labels) = clothe_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser' , 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

tes_loss, tes_acc = model.evaluate(test_images, test_labels,verbose=2)

print('Test accuracy:', tes_acc)
