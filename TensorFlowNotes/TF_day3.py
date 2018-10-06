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
y_pred = tf.nn.softmax(logits)
y_pred_cls = tf.argmax(y_pred, axis=1)	#take argmax along each column

# logit = [num_samples, num_class]
# at (i,j) = likelihood of i'th sample input belonging to j'th class
# thus, for each row, it's the sample's probability across all classes FOR A SINGLE SAMPLE 

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_true)
#requirement for labels: each row of valid probability distribution (i.e. all sum to one); otherwise, gradient computation incorrect --> i.e. probability for a SINGLE sample to be in any one of the class should sum to 1

#measure the PROB ERROR in discrete classification where classes are mutually exclusive (i.e. image is labeled with one and only one label)
cost = tf.reduce_mean(cross_entropy)		
# take the average of the cross-entropy for all the image classifications.

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)
correct_prediction = tf.equal(y_pred_cls, y_true_cls)	#a vector of booleans whether the predicted class equals the true class of each image.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

session = tf.Session()		#A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated.
session.run(tf.global_variables_initializer())


'''
There are 50.000 images in the training-set. It takes a long time to calculate the gradient of the model using all these images. We therefore use Stochastic Gradient Descent which only uses a small batch of images in each iteration of the optimizer.
'''

batch_size = 100

def optimize(num_iterations):
	for i in range(num_iterations):
		x_batch, y_true_batch = data.train.next_batch(batch_size)
		feed_dict_train = {x: x_batch, y_true: y_true_batch}	#zip each pair as an element in dict
		
		# Run the optimizer using this batch of training data.
        # TensorFlow assigns the variables in feed_dict_train
        # to the placeholder variables and then runs the optimizer.
		# noted placeholder var are all GLOBAL variable 
		session.run(optimizer, feed_dict=feed_dict_train)		#optimizer as graph fragment
		
feed_dict_test = {x: data.test.images, y_true: data.test.labels, y_true_cls: data.test.cls}
# x, y_true and y_true_cls are all defined previously 

def print_accuracy():
	acc = session.run(accuracy, feed_dict=feed_dict_test)
	print("Accuracy on test-set: {0:.1%}".format(acc))

# plotting the confusion matrix
def print_confusion_matrix():
	cls_true = data.test.cls
	cls_pred = session.run(y_pred_cls, feed_dict=feed_dict_test)
	
	# text confusion matrix
	cm = confusion_matrix(y_true=cls_true, y_pred=cls_pred)
	print(cm)
	
	plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
	# image confusion matrix
	
    # Make various adjustments to the plot.
    plt.tight_layout()
    plt.colorbar()
    tick_marks = np.arange(num_classes)
    plt.xticks(tick_marks, range(num_classes))
    plt.yticks(tick_marks, range(num_classes))
    plt.xlabel('Predicted')
    plt.ylabel('True')
    
    plt.show()	
	
'''

'''

def plot_weights():
    # Get the values for the weights from the TensorFlow variable.
    w = session.run(weights)
    
    # Get the lowest and highest values for the weights.
    # This is used to correct the colour intensity across
    # the images so they can be compared with each other.
    w_min = np.min(w)
    w_max = np.max(w)

    # Create figure with 3x4 sub-plots,
    # where the last 2 sub-plots are unused.
    fig, axes = plt.subplots(3, 4)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        # Only use the weights for the first 10 sub-plots.
        if i<10:
            # Get the weights for the i'th digit and reshape it.
            # Note that w.shape == (img_size_flat, 10)
            image = w[:, i].reshape(img_shape)

            # Set the label for the sub-plot.
            ax.set_xlabel("Weights: {0}".format(i))

            # Plot the image.
            ax.imshow(image, vmin=w_min, vmax=w_max, cmap='seismic')

        # Remove ticks from each sub-plot.
        ax.set_xticks([])
        ax.set_yticks([])
        
    # Ensure the plot is shown correctly with multiple plots
    # in a single Notebook cell.
    plt.show()
	

optimize(num_iterations=1000)
print_accuracy()
plot_example_errors()

plot_weights()
print_confusion_matrix()
session.close()












