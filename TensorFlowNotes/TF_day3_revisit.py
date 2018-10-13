%matplotlib inline
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix

from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets("data/MNIST/", one_hot=True)

print("Size of: ")
print("-Training-set:\t\t{}".format(len(data.train.labels)))
print("-Test-set:\t\t{}".format(len(data.train.labels)))
print("-Validation-set:\t\t{}".format(len(data.validation.labels)))

#argmax() not a tf operation; need not called by Session.run()
data.test.cls = np.array([label.argmax() for label in data.test.labels])	
img_size = 28
img_size_flat = img_size*img_size
img_shape = (img_size, img_size)
num_classes = 10

x = tf.placeholder([None, img_size_flat])
y_true = tf.placeholder([None, num_classes])
weights = tf.Variable(tf.zeros([img_size_flat, num_classes]))		#(size of feature vector, # classes)
biases = tf.Variable(tf.zeros([num_classes]))		#(, # classes)

logits = tf.matmul(x, weights) + biases
y_pred = tf.nn.softmax(logits)
y_pred_cls = tf.argmax(y_pred, axis=1)

#softmax的输出向量[Y1，Y2,Y3...]和样本的实际标签做一个交叉熵
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_true)		#math behind?
#预测越准确，结果的值越小（别忘了前面还有负号），最后求一个平均，得到我们想要的loss
cost = tf.reduce_mean(cross_entropy)	
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost);
#https://blog.csdn.net/mao_xiao_feng/article/details/53382790

# accuracy evaluation for classifier: eva # correct samples predicted 
correct_prediction = tf.equal(y_pred, y_true_cls)	#rtn: A Tensor of type bool.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))		#numeric tensor required by reduce_mean(), not boolean!

session = tf.Session()
#Returns an Op that initializes global variables, which is run by run() 
# first operation to run after session establishment --> init graph tensors
session.run(tf.global_variables_initizalizer())

batch_size = 100

# this operator for iterative, batch training 
def optimize(num_iteration):
	for i in range(num_iterations):
		x_batch, y_true_batch = data.train.next_batch(batch_size)	#iterative, each batch modifies a bit of the weights upon previous training result; an epoch is a continuous process! :) 
		feed_dict_train = {x:x_batch, y_true: y_true_batch}
		session.run(optimizer, feed_dict=feed_dict_train)	#feed_dict:A dictionary that maps graph elements to values; so that optimizer could work on
		#calling sequence logit: optimizer->cost->cross_entropy->logits(involve graph variables)

		
feed_dict_test = {x: data.test.images, y_true: data.test.labels, y_true_cls: data.test.cls}	
def print_accuracy():
	acc = session.run(accuracy, feed_dict=feed_dict_test)	#variables in feed_dict is those needed by the operator inside run()
	print("Accuracy on test-set: {0:.1%}".format(acc))		

#thus, Session.run() parameter: operations + variables (set via feed_dict())

optimize(num_iterations=1000)
print_accuracy()


