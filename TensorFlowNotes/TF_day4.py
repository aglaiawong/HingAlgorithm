%matplotlib inline
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import math

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import InputLayer, InputLayer
from tensorflow.python.keras.layers import Reshape, MaxPooling2D
from tensorflow.python.keras.layers import InputLayer, InputLayer

from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets('data/MNIST/', one_hot=True)

'''
Data types of MNIST data set
data.train/ data.test
<class 'tensorflow.contrib.learn.python.learn.datasets.mnist.DataSet'>
data.train.labels/ data.test.images
<class 'numpy.ndarray'> of shape: (55000, 784)
--> i.e. 55000 records/samples, each flattened to a size of 784
'''


# always use 'label' part to calculate the number of sample instances 
print("Size of:")
print("- Training-set:\t\t{}".format(len(data.train.labels)))
print("- Test-set:\t\t{}".format(len(data.test.labels)))
print("- Validation-set:\t{}".format(len(data.validation.labels)))

data.test.cls = np.argmax(data.test.labels, axis=1)
img_size = 28
img_size_flat = img_size * img_size
# This is used for plotting the images, (height, width)
img_shape = (img_size, img_size)
# This is used for reshaping in Keras, (height,width,depth)
img_shape_full = (img_size, img_size, 1)
# Number of colour channels for the images: 1 channel for gray-scale.
num_channels = 1
# Number of classes, one class for each of 10 digits.
num_classes = 10

#helper-function for plotting images 
'''
Function used to plot 9 images in a 3x3 grid, 
and writing the true and predicted classes below each image.
'''
def plot_images(images, cls_true, cls_pred=None):
    assert len(images) == len(cls_true) == 9
    
    # Create figure with 3x3 sub-plots.
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        # Plot image.
        ax.imshow(images[i].reshape(img_shape), cmap='binary')

        # Show true and predicted classes.
        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        # Show the classes as the label on the x-axis.
        ax.set_xlabel(xlabel)
        
        # Remove ticks from the plot.
        ax.set_xticks([])
        ax.set_yticks([])
    
    # Ensure the plot is shown correctly with multiple plots
    # in a single Notebook cell.
    plt.show()
	
#Plot a few images to see if data is correct
# Get the first images from the test-set.
images = data.test.images[0:9]		#a ndarray
# Get the true classes for those images.
cls_true = data.test.cls[0:9]
# Plot the images and labels using our helper-function above.
plot_images(images=images, cls_true=cls_true)

'''
Helper-function to plot example errors
Function for plotting examples of images from the test-set that have been mis-classified.
'''
def plot_example_errors(cls_pred):
	incorrect = (cls_pred!=data.test.cls)
	images = data.test.images[incorrect]
	cls_pred = cls_pred[incorrect]
	cls_true = data.test.cls[incorrect]
	
	plot_images(images=images[0:9], cls_true=cls_true[0:9], cls_pred=cls_pred[0:9])
	

#sequential modelling in Keras API: simple stacking 

# Start construction of the Keras Sequential model.
model = Sequential()
# Add an input layer which is similar to a feed_dict in TensorFlow.
# Note that the input-shape must be a tuple containing the image-size.
model.add(InputLayer(input_shape=(img_size_flat,))	#reverted x,y as in np array 
# The input is a flattened array with 784 elements,
# but the convolutional layers expect images with shape (28, 28, 1)
model.add(Reshape(img_shape_full)))

# First convolutional layer with ReLU-activation and max-pooling.
model.add(Conv2D(kernel_size=5, strides=1, filters=16, padding='same', activation='relu', name='layer_conv1'))
model.add(MaxPooling2D(pool_size=2, strides=2))

# Second convolutional layer with ReLU-activation and max-pooling.
model.add(Conv2D(kernel_size=5, strides=1, filters=36, padding='same',
                 activation='relu', name='layer_conv2'))
model.add(MaxPooling2D(pool_size=2, strides=2))

#下面程式碼建立平坦層, 將之前步驟已經建立的池化層2, 共有 36 個 7x7 維度的影像轉換成 1 維向量, 長度是 36x7x7 = 1764, 也就是對應到 1764 個神經元
model.add(Flatten())
model.add(Dense(128,activation='relu')
model.add(Dense(num_classes, activation='softmax'))

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	