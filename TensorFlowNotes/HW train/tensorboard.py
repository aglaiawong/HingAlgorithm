:#-*-coding:utf-8-*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

plotdata = {"batchsize":[], "loss":[]}
def moving_average(a,w=10):
	if len(a) < w:
		return a[:]
	return [val if idx<w else sum(a[(idx-w):idx])/w for idx, val in enumerate(a)]

#generate analog data
train_X = np.linspace(-1,1,100)
train_Y = 2*train_X + np.randn(*train_X.shape)*0.3

plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.legend()
plt.show()

tf.reset_default_graph()

X = tf.placeholder("float")
Y = tf.placeholder("float")

W=tf.Variable(tf.random_normal([1]),name="weight")
b=tf.Variable(tf.zeros([1]), name="bias")

z = tf.multiply(X,W)+b
tf.summary.histogram('z',z)

cost = tf.reduce_mean(tf.square(Y-z))
tf.summary.sclar('loss_function', cost)
learning_rate = 0.01

#GD
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()
training_epochs = 20
display_step = 2

with tf.Session() as sess:
	sess.run(init)
	merged_summary_op = tf.summary.merge_all()
	summary_writer = tf.summary.FileWriter('log/mnist_with_summaries', sess.graph)

for epoch in range(training_epoths):
	for (x,y) in zip(train_X, train_Y):
		sess.run(optimizer, feed_dict={X:x, Y:y})

	summary_str = sess.run(merged_summary_op, feed_dict={X:x, Y:y});
	summary_writer.add_summary(summary_str, epoch);






