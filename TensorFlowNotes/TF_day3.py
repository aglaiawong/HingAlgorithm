'''
Linear regression
'''

%matplotlib inline
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix

from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets("data/MNIST/", one_hot=True)	# path for storage
# read_data_sets: for extracting the data from .gz 

print("Size of: ")
print("-Training-set:\t\t{}".format(len(data.train.labels)))
print("-Test-set:\t\t{}".format(len(data.train.labels)))
print("-Validation-set:\t\t{}".format(len(data.validation.labels)))

#convert one-hot to numerics (not used in following)
data.test.cls = np.array([label.argmax() for label in data.test.labels])

# We know that MNIST images are 28 pixels in each dimension.
img_size = 28
# Images are stored in one-dimensional arrays of this length.
img_size_flat = img_size * img_size
# Tuple with height and width of images used to reshape arrays.
img_shape = (img_size, img_size)
# Number of classes, one class for each of 10 digits.
num_classes = 10

#define placeholder
x = tf.placeholder(tf.float32, [None, img_size_flat])
y_true = tf.placeholder(tf.float32, [None, num_classes])

#model parameters: tf.Variables
weights = tf.Variable(tf.zeros([img_size_flat, num_classes]))
#tf.Variable maintain value/state across run();
#variables other than tf.Variable cleaned at each call to run()
biases = tf.Variable(tf.zeros([num_classes]))		#why init them into zero? 

logits = tf.matmul(x,weights) + biases


