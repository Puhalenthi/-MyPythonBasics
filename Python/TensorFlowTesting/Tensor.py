import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(xtrainingdata, ytrainingdata), (xtestingdata, ytestingdata) = mnist.load_data()

xtrainingdata = xtrainingdata/255
xtestingdata = xtestingdata/255

plt.imshow(xtrainingdata[0])

mlmodel = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(196, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
])

